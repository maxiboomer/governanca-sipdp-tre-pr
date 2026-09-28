#!/usr/bin/env python3
"""
Monitoramento ANPD: Anonimização e Pseudonimização

Detecta publicações do Guia de Anonimização e Pseudonimização da ANPD
através de 4 fontes: balanço da agenda, regulamentações, notícias e
documentos técnicos/orientativos (onde o Guia será publicado).

Estado persistente: references/_meta/monitor_state_anpd.json
Log de rodadas: references/_meta/relatorio-monitoramento.md

v3 (2026-09-28) — corrige falso positivo crônico da v1 e instabilidade da v2:
  - v1 bug: `changed = changed if changed else True` forçava mudança em TODA
    rodada; hash era sobre HTML bruto (ruído dinâmico do CDN gov.br).
  - gov.br alterna entre variante "shell JS" (~137KB) e "completa" (~320KB):
    noticias agora usa ?b_start=0 (sempre completa) + detecção de shell.
  - Hash computado sobre HTML NORMALIZADO (sem <script>/<style>/comentários/
    tokens CSRF/whitespace) — verificado estável em 3+ fetches consecutivos.
  - agenda: hash instável (tabela JS) → sinal = data "Modificado em".
  - Fonte NOVA: Documentos Técnicos e Orientativos (vetor principal de
    publicação do Guia; contém baseline das keywords dos estudos de 2023).
  - Alerta de keyword só quando surge CONTEXTO NOVO vs. baseline armazenado
    (a página de documentos técnicos sempre contém "anonimização" dos
    estudos de 2023 — não é alerta).
  - Hashes prefixados 'v3:' — hash sem prefixo = sem baseline (não é mudança).
  - Verificação de vault com caminho correto; log único por rodada.

Limitação conhecida: a listagem de notícias e a tabela da agenda são
carregadas via JavaScript — o script (stdlib, sem browser) vê apenas o
envelope server-rendered (data "Modificado em", contagens, texto estático).
A verificação profunda dessas páginas cabe ao agente (web_extract) quando
este script sinalizar mudança.
"""

import json
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# --- Configuração ---
VAULT_ROOT = Path(__file__).resolve().parents[2]
STATE_FILE = VAULT_ROOT / "references" / "_meta" / "monitor_state_anpd.json"
LOG_FILE = VAULT_ROOT / "references" / "_meta" / "relatorio-monitoramento.md"

# Locais onde normas ANPD curadas podem existir (build do repo + vault llm-wiki)
VAULT_NORMAS_DIRS = [
    VAULT_ROOT / "skills" / "governanca-sipdp-tre-pr" / "references" / "normas",
    Path("/root/llmwiki/llm-wiki/wiki/normas"),
]

HASH_VERSION = "v3"

# Fontes de monitoramento
# signal: "hash" = detecção por hash normalizado | "modificado" = por data
# "Modificado em" (agenda tem variantes de renderização que flapam o hash)
SOURCES = {
    "agenda": {
        "url": "https://www.gov.br/anpd/pt-br/assuntos/regulacao/agenda-regulatoria-1/agenda-regulatoria-2025-2026",
        "desc": "Balanço da Agenda Regulatória 2025-2026",
        "signal": "modificado",
    },
    "regulamentacoes": {
        "url": "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd",
        "desc": "Página de Regulamentações",
        "signal": "hash",
    },
    "noticias": {
        # ?b_start=0 contorna o cache CDN que às vezes serve um shell JS vazio
        "url": "https://www.gov.br/anpd/pt-br/assuntos/noticias?b_start=0",
        "desc": "Página de Notícias",
        "signal": "hash",
        "shell_check": True,
    },
    "documentos_tecnicos": {
        "url": "https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos",
        "desc": "Documentos Técnicos e Orientativos (vetor de publicação do Guia)",
        "signal": "hash",
    },
}

# Palavras-chave para detecção (com e sem acento)
KEYWORDS = ["anonimização", "pseudonimização", "anonimizacao", "pseudonimizacao"]


def get_page_content(url, timeout=25):
    """Baixa HTML de uma página com user-agent amigável."""
    req = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; HermesANPD/3.0)"}
    )
    try:
        with urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="ignore")
    except HTTPError as e:
        return f"[HTTP {e.code}]"
    except URLError:
        return "[URL_ERROR]"
    except Exception as e:
        return f"[ERROR: {type(e).__name__}]"


def is_error(content):
    return content.startswith(("[HTTP", "[ERROR", "[URL_ERROR"))


def normalize_html(html):
    """
    Remove conteúdo dinâmico que muda a cada request (scripts, estilos,
    comentários, tokens CSRF, whitespace), devolvendo texto estável para hash.
    """
    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    # Tokens CSRF do Plone (mudam a cada request)
    text = re.sub(r"_authenticator[^\"'\s>]*", " ", text)
    # Mensagens de status de portal inseridas por query string
    text = re.sub(r"portal_status_message[^\"'\s>]*", " ", text)
    # Colapsa whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compute_hash(text):
    """Computa hash SHA-256 versionado do texto normalizado."""
    return f"{HASH_VERSION}:{hashlib.sha256(text.encode('utf-8')).hexdigest()}"


def extract_page_info(content, keywords):
    """
    Extrai sinais da página sobre HTML normalizado.
    Retorna: (modificado, items_count, keyword_matches)
      modificado: data "Modificado em DD/MM/AAAA HH:MM" ou None
      keyword_matches: [{"keyword", "context"}]
    """
    normalized = normalize_html(content)
    text_only = re.sub(r"<[^>]+>", " ", normalized)
    text_only = re.sub(r"\s+", " ", text_only).strip()

    # Data de modificação (sinal semântico estável das páginas gov.br)
    mod = re.search(r"Modificado em\s*(\d{2}/\d{2}/\d{4}\s*\d{2}:\d{2})", text_only)
    modificado = re.sub(r"\s+", " ", mod.group(1)) if mod else None

    # Contar links na página normalizada
    items_count = len(re.findall(r'<a[^>]*href="([^"]*)"', normalized))

    # Palavras-chave com contexto (para diff contra baseline)
    text_lower = text_only.lower()
    keyword_matches = []
    for kw in keywords:
        m = re.search(re.escape(kw), text_lower)
        if m:
            start = max(0, m.start() - 70)
            end = min(len(text_only), m.end() + 130)
            context = text_only[start:end].strip()
            keyword_matches.append({"keyword": kw, "context": context})

    return modificado, items_count, keyword_matches


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


def log_round(section_title, details):
    """Registra UMA rodada no relatorio-monitoramento.md (inserida no topo)."""
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("---\ntitle: Relatório de Monitoramento Normativo\ntype: metadata\n---\n\n# Relatório de Monitoramento Normativo\n\n")

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_blank = None
    for i, line in enumerate(lines):
        if line.strip() == "" and i > 0:
            first_blank = i
            break

    log_entry = f"\n## Rodada {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n### {section_title}\n{details}\n\n"

    if first_blank:
        lines.insert(first_blank + 1, log_entry)
    else:
        lines.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def check_vault_for_studies():
    """Verifica se normas/estudos ANPD de anonimização já estão curados no vault."""
    found = []
    for d in VAULT_NORMAS_DIRS:
        if not d.exists():
            continue
        for f in d.glob("*anonimizacao*"):
            if "anpd" in f.stem:
                found.append(str(f))
    return sorted(set(found))


def kw_set(matches):
    """Chave estável de uma lista de keyword matches (para diff de baseline)."""
    return {f"{m['keyword']}::{re.sub(r'[^a-z0-9á-úà-ùâ-ûã-õç ]', '', m['context'].lower())[:120]}" for m in matches}


def main():
    print("=== Monitor ANPD: Anonimização e Pseudonimização (v3) ===")
    print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    state = get_state()
    prev_sources = state.get("sources", {}) or {}
    print(f"Estado anterior: last_run={state.get('last_run', 'never')}")
    print(f"Detecção registrada: {state.get('detected', False)}")
    print()

    new_sources = {}
    changed_sources = []
    new_keyword_hits = []

    for source_name, cfg in SOURCES.items():
        print(f"Verificando: {cfg['desc']}...")

        content = get_page_content(cfg["url"])

        if is_error(content):
            print(f"  ERRO de fetch: {content}")
            print()
            new_sources[source_name] = {
                "error": content, "last_seen": datetime.now().isoformat(), "changed": False,
            }
            continue

        modificado, items_count, keyword_matches = extract_page_info(content, KEYWORDS)
        current_hash = compute_hash(normalize_html(content))

        # Detecção de shell JS (variante sem conteúdo server-rendered)
        unreliable = False
        if cfg.get("shell_check") and modificado is None:
            unreliable = True

        prev = prev_sources.get(source_name, {}) or {}
        prev_hash = prev.get("hash")
        prev_mod = prev.get("modificado")
        prev_kws = prev.get("keyword_contexts", [])

        # --- Sinal de mudança ---
        if cfg["signal"] == "modificado":
            if prev_mod is None:
                changed, note = False, "sem baseline (estabelecendo agora)"
            elif modificado is None:
                changed, note = False, "data Modificado em ausente neste fetch"
            elif modificado != prev_mod:
                changed, note = True, f"Modificado em: {prev_mod} → {modificado}"
            else:
                changed, note = False, f"Modificado em estável ({modificado})"
        else:  # signal == hash
            if unreliable:
                changed, note = False, "variante shell JS (sem Modificado em) — sem detecção nesta rodada"
            elif not str(prev_hash or "").startswith(f"{HASH_VERSION}:"):
                changed, note = False, "sem baseline v3 (estabelecendo agora)"
            elif prev_hash != current_hash:
                changed, note = True, "hash normalizado diverge do baseline"
            else:
                changed, note = False, "estável"

        # --- Keywords NOVAS vs. baseline ---
        current_kw_keys = kw_set(keyword_matches)
        prev_kw_keys = set(prev_kws)
        fresh = [m for m in keyword_matches
                 if f"{m['keyword']}::{re.sub(r'[^a-z0-9á-úà-ùâ-ûã-õç ]', '', m['context'].lower())[:120]}" not in prev_kw_keys]
        has_baseline_kws = bool(prev_kw_keys) or prev.get("last_seen") is not None

        new_sources[source_name] = {
            "hash": current_hash,
            "modificado": modificado,
            "items_count": items_count,
            "keyword_contexts": sorted(current_kw_keys),
            "last_seen": datetime.now().isoformat(),
            "changed": changed,
            "keyword_matches": len(keyword_matches),
        }

        print(f"  Hash: {current_hash[:22]}...")
        print(f"  Modificado em: {modificado or 'n/d'}")
        print(f"  Items (links): {items_count}")
        print(f"  Keywords: {len(keyword_matches)} no total, {len(fresh)} nova(s) vs. baseline")
        if keyword_matches and not fresh and has_baseline_kws:
            print(f"    (baseline conhecida — ex.: estudos ANPD 2023 já curados)")
        print(f"  Mudança: {changed} ({note})")
        print()

        if changed:
            changed_sources.append({
                "desc": cfg["desc"],
                "note": note,
                "modificado": modificado,
                "items_count": items_count,
            })
        if fresh:
            new_keyword_hits.append({"source": cfg["desc"], "matches": fresh})

    state["sources"] = new_sources
    state["last_run"] = datetime.now().isoformat()
    # 'detected' reflete a rodada atual (não é flag histórica)
    state["detected"] = bool(new_keyword_hits)

    # --- Log (UMA entrada por rodada) ---
    if new_keyword_hits:
        details = []
        for hit in new_keyword_hits:
            for m in hit["matches"]:
                details.append(f"- **{hit['source']}** — keyword `{m['keyword']}` NOVA: \"{m['context']}\"")
        log_round("PALAVRA-CHAVE NOVA DETECTADA (verificar publicação do Guia)", "\n".join(details))
    elif changed_sources:
        details = [f"- {c['desc']}: {c['note']} (modificado={c['modificado'] or 'n/d'}, items={c['items_count']})" for c in changed_sources]
        details.append("- Nota: mudança sem keyword nova de anonimização/pseudonimização — verificar manualmente (notícias/agenda são JS; usar web_extract).")
        log_round("Mudanças de conteúdo detectadas", "\n".join(details))
    else:
        log_round(
            "Sem alterações",
            "- Nenhuma das 4 fontes mudou desde o baseline; nenhuma keyword nova de anonimização/pseudonimização.\n"
            "- Baselines: agenda (Modificado em), regulamentações/documentos técnicos/notícias (hash normalizado v3).",
        )

    save_state(state)
    print(f"Estado salvo em: {STATE_FILE}")
    print(f"Rodada registrada em: {LOG_FILE}")

    # Estudos ANPD já curados no vault
    vault_files = check_vault_for_studies()
    print()
    print(f"Estudos ANPD de anonimização no vault: {len(vault_files)} arquivo(s)")
    for vf in vault_files:
        print(f"  - {vf}")

    # --- Conclusão ---
    print()
    if new_keyword_hits:
        print("=== PALAVRA-CHAVE NOVA DETECTADA — VERIFICAR PUBLICAÇÃO DO GUIA ===")
        for hit in new_keyword_hits:
            for m in hit["matches"]:
                print(f"  - {hit['source']}: {m['keyword']} → \"{m['context'][:120]}\"")
    elif changed_sources:
        print("=== MUDANÇA DE CONTEÚDO DETECTADA — verificar manualmente ===")
        for c in changed_sources:
            print(f"  - {c['desc']} ({c['note']})")
    else:
        print("=== CONCLUSÃO: Sem alterações — Guia de Anonimização/Pseudonimização ainda não publicado ===")

    return 0


if __name__ == "__main__":
    sys.exit(main())
