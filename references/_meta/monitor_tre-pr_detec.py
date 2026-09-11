#!/usr/bin/env python3
"""
Script de detecção leve para monitoramento normativo TRE-PR (via browser_exec)

Função: Verificar se há NOVAS normas nas fontes oficiais.
Se não houver mudanças → retorna [SILENT] (economiza tokens).
Se houver → lista as mudanças e o job do agente processa.

Usa browser_exec (não urllib) para evitar HTTP 403.
"""

import json
import hashlib
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --- Configuração ---
VAULT_ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = VAULT_ROOT / "raw"
NORMAS_DIR = VAULT_ROOT / "normas"

# Estado persistente
STATE_FILE = VAULT_ROOT / "references" / "_meta" / "monitor_tre-pr_state.json"
LOG_FILE = VAULT_ROOT / "references" / "_meta" / "relatorio-monitoramento.md"

# Fontes oficiais (URLs base)
SOURCES = {
    "tre-pr_resolucoes": "https://www.tre-pr.jus.br/legislacao/compilada/resolucoes-tre-pr/2026",
    "tre-pr_ins": "https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2026",
    "tre-pr_nts": "https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026",
    "tre-pr_portarias_dg": "https://www.tre-pr.jus.br/legislacao/compilada/portarias-da-diretoria-geral-tre-pr/2026",
    "tre-pr_portarias_presidencia": "https://www.tre-pr.jus.br/legislacao/compilada/portarias-da-presidencia-tre-pr/2026",
    "tse_legislacao": "https://www.tse.jus.br/legislacao",
}


def fetch_via_browser(url, timeout=30):
    """
    Fetch HTML via browser_exec (para evitar 403).
    Retorna o HTML ou None.
    """
    code = f"""
# Navegar para URL
goto_url("{url}")
wait_for_load()

# Extrair HTML
js("document.documentElement.outerHTML")
"""
    try:
        result = subprocess.run(
            ["browser-use"],
            input=code,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except Exception:
        return None


def compute_hash(text):
    """Compute SHA-256."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_regulations(content, source_name):
    """
    Extrair lista de normas da página HTML.
    Retorna: [(nome, numero, data, url), ...]
    """
    if not content:
        return []

    import re

    # Extrair link e título de cada norma
    pattern = r'<a[^>]*href="[^"]*[/\\]([^"\.]+)\.(?:html|pdf)"[^>]*>(.*?)</a>'
    matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)

    regulations = []
    for raw_link, title in matches:
        nome = re.sub(r'<[^>]+>', '', title).strip()
        if not nome:
            continue
        data = None
        url = f"{source_name}/...{raw_link}"
        regulations.append({"nome": nome, "numero": raw_link, "data": data, "url": url})

    return regulations


def load_catalog():
    """Carregar catálogo atual do vault (normas + raws)."""
    catalog = set()
    if NORMAS_DIR.exists():
        for f in NORMAS_DIR.glob("*.md"):
            catalog.add(f.stem.lower())
    if RAW_DIR.exists():
        for f in RAW_DIR.glob("*.md"):
            if f.name.startswith("tre-pr") or f.name.startswith("tse-"):
                catalog.add(f.stem.lower())
    return catalog


def get_state():
    """Carregar estado persistente."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"sources": {}, "last_run": None}


def save_state(state):
    """Salvar estado persistente."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def log_result(changes_detected, changes_list):
    """Registra resultado no relatorio-monitoramento.md."""
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("---\ntitle: Relatório de Monitoramento Normativo\ntype: metadata\n---\n\n")

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_blank = None
    for i, line in enumerate(lines):
        if line.strip() == "" and i > 0:
            first_blank = i
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = f"""
## Rodada {timestamp}

### Detecção de mudanças (script leve com browser)
- Registros verificados: {len(SOURCES)}
- Novas normas detectadas: {len(changes_list)}
- Ação: {"Processar com agente" if changes_list else "[SILENT] - nenhuma mudança"}

"""
    if first_blank:
        lines.insert(first_blank + 1, log_entry)
    else:
        lines.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    print(f"=== Monitoramento TRE-PR: Detecção Leve (browser) ===")
    print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    state = get_state()
    current_catalog = load_catalog()
    changes_detected = []

    # Verifica cada fonte
    for source_name, url in SOURCES.items():
        print(f"Verificando: {source_name}...")

        content = fetch_via_browser(url)
        if not content:
            print(f"  ❌ Falha no fetch (browser)")
            continue

        current_hash = compute_hash(content)
        prev_hash = state.get("sources", {}).get(source_name, {}).get("hash")
        changed = prev_hash != current_hash

        state["sources"][source_name] = {
            "hash": current_hash,
            "last_seen": datetime.now().isoformat()
        }

        if changed:
            print(f"  ✅ Mudança detectada (hash diferente)")
            reg = extract_regulations(content, source_name)
            print(f"  {len(reg)} normas encontradas na fonte")

            for r in reg:
                nome_lower = r["nome"].lower()
                if nome_lower not in current_catalog:
                    changes_detected.append(r)
        else:
            print(f"  ⏭️ Sem mudanças")

    save_state(state)
    log_result(changes_detected, changes_detected)

    print()
    if changes_detected:
        print(f"=== NOVAS NORMAS DETECTADAS: {len(changes_detected)} ===")
        for reg in changes_detected:
            print(f"  - {reg['nome']}")
        print()
        print(f"AÇÃO: Processar com agente (não silenciar)")
    else:
        print("=== [SILENT] - nenhuma mudança detectada ===")


if __name__ == "__main__":
    main()
