# Cron Job Template — Monitoramento Normativo (Otimizado)

**Inclua este bloqueio no prompt do cron para prevenir rate limit:**

```text
[RATE LIMIT PROTECTION]
Máximo de 20 tool calls por execução. Se a execução atingir 18 calls, interrompa e salve progresso.
Priorize batching: sempre combine múltiplas buscas/web_extract em uma única chamada.
- search_files: use 1 call com wildcard em vez de 3 calls separadas
- web_search: use 1 call com query combinada em vez de 3 calls
- web_extract: use 1 call com 3 URLs em vez de 3 calls separadas
```

---

## Prompt Otimizado (versão completa)

```text
[IMPORTANT: You are running as a scheduled cron job. DELIVERY: Your final response will be automatically delivered to the user — do NOT use send_message. Just produce your report/output. SILENT: If nothing new to report, respond with exactly "[SILENT]".]

MONITORAMENTO NORMATIVO TRE-PR + TSE + CNJ — execução semanal otimizada.

CONTEXTO:
- Vault (fonte da verdade): /root/llmwiki/llm-wiki/wiki
- Build (repo GitHub): /root/governanca-sipdp-tre-pr
- Normas curadas: wiki/normas/, raw em raw/ (raiz do vault: /root/llmwiki/llm-wiki/raw/)

CRITÉRIO DE ESCOPO: leia ANTES wiki/_meta/criterio-escopo.md

OBJETIVO: Detectar novas normas/revogações SI/PDP-relevantes, sincronizar e publicar no GitHub.

PASSO 1 — INVENTÁRIO (2 calls MAX):
1. read_file: /root/llmwiki/llm-wiki/wiki/_meta/criterio-escopo.md
2. search_files: limit=200, path=/root/llmwiki/llm-wiki/wiki/normas, pattern=*.md

PASSO 2 — COLETAR FONTES (1 call BATCHED):
web_extract com URLs (max 5):
- https://www.tre-pr.jus.br/legislacao/normas
- https://www.tse.jus.br/legislacao/normas
- https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd

PASSO 3 — BUSCAS ESPECÍFICAS (1 call BATCHED):
web_search com query combinada:
"TRE-PR TSE CNJ ANPD normas 2026 segurana da informação proteção dados PSI resolução portaria"

PASSO 4 — VERIFICAÇÃO DE NOVIDADES (1 call BATCHED):
search_files:
- path=/root/llmwiki/llm-wiki/raw, pattern=*tse-resolucao-23-7*, target=files
- path=/root/llmwiki/llm-wiki/raw, pattern=*tse-portaria*, target=files

PASSO 5 — ANÁLISE DE GAP:
Para cada raw file sem wiki page correspondente:
- read_file: 1ª linha (20 chars) para meta
- Compare com inventário

PASSO 6 — DECISÃO DE PUBLICAÇÃO:
Se norma nova em raw →
1. Crie wiki/normas/*.md com frontmatter completo
2. Commit e push no repo governanca-sipdp-tre-pr
3. Publique no GitHub (sync+bump+tag+release)

SEMENTES PARA EVITAR:
- Não use urllib (bloqueado 403)
- Não faça search_files repetidas para cada número (use wildcard)
- Não faça web_search separadas para cada tribunal (combine query)
- Não ultrapasse 20 tool calls — pare em 18 e salve
```

---

## Atualização do Cron Job

Execute:

```bash
hermes cronjob update --job-id=7bc98667d933 --prompt=@/root/governanca-sipdp-tre-pr/references/_meta/monitor_normas_prompt.md
```

**Ganhos esperados:**
- De ~25-30 calls para ~8-12 calls (60% redução)
- 1 web_extract batched vs 3 separados
- 1 web_search batched vs 3 separados
- 2 search_files batched vs 6 separados
