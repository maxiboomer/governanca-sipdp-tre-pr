---
title: "Relatório de Auditoria do Vault — 2026-09-04"
created: 2026-09-04
updated: 2026-09-04
type: meta
status: vigente
curadoria: completa
escopo: contextual
tags: [auditoria, vault, saude, metadados, relatorio]
---
# Auditoria do Vault — 2026-09-04

## Resumo executivo

| Métrica | Valor | Status |
|---|---|---|
| Total páginas curadas (excluindo raw) | 230 | ✅ |
| Total raws | 188 | ✅ |
| Cobertura de rastreabilidade | 100,0% (187/187) | ✅ |
| Frontmatter completo | 187/187 | ✅ |
| Index vs filesystem | 187/187 (0 divergências) | ✅ |
| Duplicatas reais | 0 | ✅ |
| Build drift (conteúdo) | 0 (só link rewriting) | ✅ |
| Hash drift (amostra ANPD) | 0/11 | ✅ |

## Inventário por camada

| Camada | Quantidade |
|---|---|
| raw/ | 188 |
| wiki/normas/ | 187 |
| wiki/entities/ | 8 |
| wiki/concepts/ | 14 |
| wiki/comparisons/ | 2 |
| wiki/inventarios/ | 5 |
| wiki/sources/ | 7 |
| wiki/_meta/ | 7 |

## Status das normas

| Status | Quantidade |
|---|---|
| vigente | 155 |
| revogada | 19 |
| histórica | 12 |
| não-aplicável | 1 |

## Verificações realizadas

### 1. Rastreabilidade (drift de fontes)
- 187 normas com `sources: [references/raw/...]` → 187 raws encontrados no filesystem
- Cobertura: **100%** (meta: ≥95%)

### 2. Frontmatter
- 187/187 normas com todos os campos obrigatórios (`title`, `created`, `updated`, `type`, `status`, `curadoria`, `escopo`, `tags`)
- 0 campos faltantes

### 3. Index vs filesystem
- Index menciona 187 normas
- Sistema de arquivos: 187 normas
- 0 ausências em ambos os lados

### 4. Duplicatas
- 0 duplicatas por número de norma
- 4 candidatos com números similares (12527, 855) são distintos: `lai-12527-2011` (federal, type=norma), `lei-12527-2011-acesso-informacao` (alias, type=metadata), `lai-tre-pr-855-2020` (local, type=norma), `tre-pr-resolucao-855-2020-acesso-informacao` (fonte-normativa)

### 5. Build drift
- 187 normas com hash diferente vault↔build → **todas por link rewriting** (conversão `references/` → `references/` no build), comportamento correto do sync
- 0 divergências de conteúdo real
- 2 raws com diferença: `INVENTARIO-NORMAS-COLETADAS.md` e `README.md` (arquivos de documentação, não fontes normativas)

### 6. Hash drift
- Amostra de 11 raws ANPD verificados → 0 drift (todos os sha256 batem)

### 7. Stubs
- 1 página com corpo < 300 chars: `lei-12527-2011-acesso-informacao.md` (185 chars) — é um alias/metadata, não um stub (type=metadata, status=não-aplicável)

## Problemas encontrados

### Nenhum problema crítico.

Problemas menores (já resolvidos ou de baixa prioridade):
1. **2 raws de documentação divergentes** (`INVENTARIO-NORMAS-COLETADAS.md`, `README.md`) — não afetam o acervo normativo. Próximo sync resolve.

## Recomendações

1. **Manter**: o vault está saudável — cobertura 100%, sem drift de conteúdo, sem duplicatas
2. **Próximo sync**: os 2 raws de documentação serão re-sincronizados automaticamente
3. **Monitoramento**: a cron semanal (seg. 08:00) continua monitorando TRE-PR + ANPD
4. **Reclassificação**: as 12 normas `histórica` e 19 `revogada` estão corretas (ADR 0004 — revogadas permanecem no acervo)

## ADRs relevantes
- ADR 0002: DJE/DOU como fonte de vigência
- ADR 0003: cron auto-publica novas normas; revogações/escopo só reportam
- ADR 0004: revogadas permanecem em `normas/` (não vão para `_archive/`)
