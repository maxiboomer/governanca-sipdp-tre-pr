#!/usr/bin/env python3
"""
Monitoramento ANPD: Anonimização e Pseudonimização

Detecta publicações do Guia de Anonimização e Pseudonimização da ANPD
através de 3 fontes: balanço da agenda, regulamentações e notícias.

Estado persistente: references/_meta/monitor_state_anpd.json
Log de rodadas: references/_meta/relatorio-monitoramento.md
"""

import json
import hashlib
import re
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# --- Configuração ---
VAULT_ROOT = Path(__file__).resolve().parents[2]
STATE_FILE = VAULT_ROOT / "references" / "_meta" / "monitor_state_anpd.json"
LOG_FILE = VAULT_ROOT / "references" / "_meta" / "relatorio-monitoramento.md"

# Fontes de monitoramento
SOURCES = {
    "balanço_agenda": {
        "url": "https://www.gov.br/anpd/pt-br/assuntos/regulacao/agenda-regulatoria-1/agenda-regulatoria-2025-2026",
        "desc": "Balanço da Agenda Regulatória 2025-2026",
        "type": "page",
    },
    "regulamentacoes": {
        "url": "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd",
        "desc": "Página de Regulamentações",
        "type": "page",
    },
    "noticias": {
        "url": "https://www.gov.br/anpd/pt-br/assuntos/noticias",
        "desc": "Página de Notícias",
        "type": "page",
    },
}

# Palavras-chave para detecção
KEYWORDS = ["anonimização", "pseudonimização", "anonimizacao", "pseudonimizacao"]


def get_page_content(url, timeout=10):
    """

 HTML de uma página com user-agent amigável."""
    req = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; HermesANPD/1.0)"}
    )
    try:
        with urlopen(req, timeout=timeout) as response:
            content = response.read().decode("utf-8", errors="ignore")
            return content
    except HTTPError as e:
        return f"[HTTP {e.code}]"
    except URLError:
        return "[URL_ERROR]"
    except Exception as e:
        return f"[ERROR: {type(e).__name__}]"


def compute_hash(text):
    """Computa hash SHA-256 do texto."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_page_info(content, keywords):
    """
    Extrai informações relevantes da página.
    Retorna: (title, items_count, keyword_matches)
    """
    if "[HTTP" in content or "[ERROR" in content or "[URL_ERROR" in content:
        return None, 0, []
    
    # Tentar extrair título
    title_match = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else None
    
    # Contar links na página
    links = re.findall(r'<a[^>]*href="([^"]*)"', content)
    items_count = len(links)
    
    # Encontrar palavras-chave
    keyword_matches = []
    text_lower = content.lower()
    for kw in keywords:
        if kw in text_lower:
            # Encontrar contexto
            idx = text_lower.find(kw)
            start = max(0, idx - 50)
            end = min(len(content), idx + 100)
            context = content[start:end].replace('\n', ' ')
            keyword_matches.append({"keyword": kw, "context": context})
    
    return title, items_count, keyword_matches


def get_state():
    """Carrega estado persistente."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"sources": {}, "last_run": None, "detected": False}


def save_state(state):
    """Salva estado persistente."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def log_change(change_type, details):
    """Registra mudança no relatorio-monitoramento.md."""
    if not LOG_FILE.exists():
        # Cria arquivo inicial se não existe
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("---\ntitle: Relatório de Monitoramento Normativo\ntype: metadata\n---\n\n# Relatório de Monitoramento Normativo\n\n")
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Inserir no topo do conteúdo principal (após a 1ª linha vazia)
    first_blank = None
    for i, line in enumerate(lines):
        if line.strip() == "" and i > 0:
            first_blank = i
            break
    
    log_entry = f"""
## Rodada {datetime.now().strftime('%Y-%m-%d %H:%M')}

### {change_type}
{details}

"""
    
    if first_blank:
        lines.insert(first_blank + 1, log_entry)
    else:
        lines.append(log_entry)
    
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    print(f"=== Monitor ANPD: Anonimização e Pseudonimização ===")
    print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Carrega estado anterior
    state = get_state()
    print(f"Estado anterior: last_run={state.get('last_run', 'never')}")
    print(f"Detecção registrada: {state.get('detected', False)}")
    print()
    
    # Verifica cada fonte
    changes_detected = []
    state["sources"] = {}
    
    for source_name, source_config in SOURCES.items():
        print(f"Verificando: {source_config['desc']}...")
        
        content = get_page_content(source_config["url"])
        title, items_count, keyword_matches = extract_page_info(content, KEYWORDS)
        current_hash = compute_hash(content)
        
        # Verifica se houve mudança
        prev_hash = state.get("sources", {}).get(source_name, {}).get("hash")
        changed = prev_hash != current_hash
        changed = changed if changed else True  # Primeiro run sempre é mudança
        
        source_state = {
            "hash": current_hash,
            "title": title,
            "items_count": items_count,
            "last_seen": datetime.now().isoformat(),
            "changed": changed,
            "keyword_matches": len(keyword_matches),
        }
        state["sources"][source_name] = source_state
        
        print(f"  Hash: {current_hash[:16]}...")
        print(f"  Título: {title}")
        print(f"  Items: {items_count}")
        print(f"  Keyword matches: {len(keyword_matches)}")
        print(f"  Mudança detectada: {changed}")
        print()
        
        if changed and source_config.get("type") == "page":
            changes_detected.append({
                "source": source_name,
                "desc": source_config["desc"],
                "title": title,
                "items_count": items_count,
                "keyword_matches": len(keyword_matches),
            })
    
    # Registra rodadas
    state["last_run"] = datetime.now().isoformat()
    
    # Registra mudança se houver alterações
    if changes_detected:
        details = []
        for change in changes_detected:
            details.append(
                f"- {change['desc']}: título='{change['title']}' "
                f"items={change['items_count']} keywords={change['keyword_matches']}"
            )
        
        log_entry = "\n".join(details)
        log_change("Mudanças detectadas", log_entry)
        
        print(f"=== MUDANÇA DETECTADA ===")
        print(f"Novo conteúdo encontrado em {len(changes_detected)} fonte(s):")
        for change in changes_detected:
            print(f"  - {change['desc']}")
        print()
        log_change("ANPD Guia de Anonimização", log_entry)
    
    # Salva estado
    save_state(state)
    print(f"Estado salvo em: {STATE_FILE}")
    print(f"Rodada registrada em: {LOG_FILE}")
    
    # Verifica se o Guia já está no vault
    vault_normas = VAULT_ROOT / "normas"
    guide_detected = False
    if vault_normas.exists():
        for f in vault_normas.glob("*anonimizacao*"):
            if "anpd" in f.stem and "estudo" in f.stem:
                guide_detected = True
                break
    
    print()
    print(f"Guia/Estudos ANPD no vault: {guide_detected}")
    
    if guide_detected and len(changes_detected) == 0:
        print("=== CONCLUSÃO: Sem novas publicações desde a última verificação ===")
    elif changes_detected:
        print("=== CONCLUSÃO: Alterações detectadas — verificar manualmente ===")
    else:
        print("=== CONCLUSÃO: Nenhuma alteração significativa detectada ===")


if __name__ == "__main__":
    main()
