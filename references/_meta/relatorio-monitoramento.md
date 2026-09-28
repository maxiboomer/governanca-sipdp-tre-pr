---
title: Relatório de Monitoramento Normativo
type: metadata
---

## Rodada 2026-09-28 08:44 — verificação manual + deploy monitor v3

### Verificação manual (agente): Guia de Anonimização/Pseudonimização NÃO publicado
- **Regulamentações**: última norma vigente = Resolução CD/ANPD nº 32/2026 (adequação UE, jan/2026). Nenhuma norma sobre anonimização/pseudonimização.
- **Notícias** (Modificado em 24/09/2026): conteúdo novo desde 23/09 = audiência pública do regulamento de fiscalização (22/09), resultado do 4º Prêmio Danilo Doneda (21/09), ECA Digital 1 ano (16/09), Sandbox IA finalista (16/09). **Sem relação com anonimização.**
- **Documentos Técnicos e Orientativos**: últimos documentos sobre anonimização = Estudos Técnicos nov/2023 (Análise Jurídica; visão de processo/risco/técnicas) + Estudos de Casos set/2023 — todos já curados no vault (commit ab2e6e4).
- **Agenda Regulatória** (Modificado em 14/08/2026): sem alteração desde 14/08.

### Correção do script (v1 → v3) — fim do falso positivo crônico
- v1 tinha `changed = changed if changed else True` (mudança forçada em TODA rodada) e hash sobre HTML bruto (ruído dinâmico do CDN gov.br). As "mudanças" registradas em 21/09, 23/09 e 28/09 08:30 eram **falsos positivos** — verificado manualmente nesta rodada.
- v3: hash sobre HTML normalizado (sem scripts/estilos/tokens), notícias via `?b_start=0` (contorna variante shell JS do CDN), agenda monitorada por data "Modificado em", **nova fonte**: Documentos Técnicos e Orientativos (vetor principal de publicação do Guia), alerta de keyword apenas quando surge contexto NOVO vs. baseline (a página de documentos técnicos sempre contém "anonimização" dos estudos 2023 — não é alerta).
- Estabilidade validada: 3 rodadas consecutivas com hash idêntico nas 4 fontes; baselines v3 estabelecidas.
- Limitação conhecida: listagem de notícias e tabela da agenda são JS — o script vê apenas o envelope server-rendered; verificação profunda (web_extract) cabe ao agente quando houver sinal.

## Rodada 2026-09-28 08:30 (v1)

### Mudanças detectadas — FALSO POSITIVO (verificado manualmente, ver rodada 08:44)
- Balanço da Agenda Regulatória 2025-2026: items=74 keywords=0
- Página de Regulamentações: items=125 keywords=0
- Página de Notícias: items=72 keywords=0

## Rodada 2026-09-23 14:01 (v1)

### Mudanças detectadas — FALSO POSITIVO (bug v1: hash bruto + changed forçado)
- Balanço da Agenda Regulatória 2025-2026: items=74 keywords=0
- Página de Regulamentações: items=125 keywords=0
- Página de Notícias: items=72 keywords=0

## Rodada 2026-09-21 08:30 (v1)

### Mudanças detectadas — FALSO POSITIVO (bug v1: hash bruto + changed forçado)
- Balanço da Agenda Regulatória 2025-2026: items=74 keywords=0
- Página de Regulamentações: items=125 keywords=0
- Página de Notícias: items=72 keywords=0

# Histórico anterior

## Rodada 2026-09-14 15:00

### Fontes consultadas
- TRE-PR legislação compilada ✓
- TSE legislação compilada ✓
- CNJ atos normativos ✓

### ✅ Normas curadas

#### TSE
| Norma | Título |
|-------|--------|
| Res. 23.763/2026 | PSI na Justiça Eleitoral |
| Res. 23.758/2026 | Auditoria de votação |
| Res. 23.769/2026 | Auditoria de votação |
| Res. 23.650/2021 | Privacidade e LGPD |
| Res. 23.644/2021 | PSI |
| Portaria 143/2026 | Cloud computing |
| Portaria 463/2026 | Planos de conformidade |

#### CNJ
| Norma | Título |
|-------|--------|
| Res. 615/2025 | Diretrizes de IA |
| Prov. 213/2026 | Padrões TIC serventias |
| Res. 647/2025 | Compartilhamento de dados |

### 📊 Status do vault
- Total raw files: ~20
- Total normas curadas: ~80+
- Critério de escopo: Res. 971/2026
