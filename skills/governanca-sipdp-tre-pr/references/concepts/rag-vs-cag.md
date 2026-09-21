---
title: "RAG vs CAG — Comparativo de arquiteturas de IA Generativa"
created: 2026-09-16
updated: 2026-09-16
type: concept
status: vigente
status_verificacao: "Video TikTok capturado em 16/09/2026"
tags: [ia, rag, cag, arquitetura, generativa]
curadoria: completa
escopo: contextual
---

# RAG vs CAG — Comparativo de arquiteturas de IA Generativa

> Infográfico comparativo entre duas arquiteturas de IA Generativa: RAG (Retrieval-Augmented Generation) e CAG (Context-Augmented Generation).

curadoria: completa
escopo: contextual
---

## RAG — Retrieval-Augmented Generation

Fluxo completo:

```
User Input → Input Encoding → Tokenization → Vector Representation → Information Fetching → Relevant Context Extraction → Vector DB → Remove Noise → Integration Step → Response Creation → Accuracy Review → Final Output
```

Loops de qualidade:
- **Bias removal** — remoção de viés (paralelo)
- **Quality Check** — verificação de qualidade (volta para Integration Step)

### Características RAG
- Busca informação **externa** (Vector DB)
- Recupera contexto relevante
- Remove ruído
- Valida precisão e viés
- Ideal para: bases de conhecimento grandes, documentos atualizados, compliance

curadoria: completa
escopo: contextual
---

## CAG — Context-Augmented Generation

Fluxo completo:

```
User Input → Query Processing → Context Injection → Domain Knowledge → Data Merging → Information Repository → Output Generation → Response Verification → Consistency check → Final Output
```

Loops de qualidade:
- **Context Enrichment** — enriquecimento de contexto (paralelo)
- **Context Synchronization** — sincronização de contexto (volta para Information Repository)

### Características CAG
- Injeta contexto **interno** (Domain Knowledge)
- Mescla dados existentes
- Verifica consistência
- Enriquece contexto continuamente
- Ideal: domínio específico, conhecimento proprietário, dados estruturados

curadoria: completa
escopo: contextual
---

## Comparativo

| Aspecto | RAG | CAG |
|---------|-----|-----|
| **Fonte de conhecimento** | Externa (Vector DB) | Interna (Domain Knowledge) |
| **Método** | Recuperação por similaridade | Injeção + mesclagem |
| **Atualização** | Tempo real (busca) | Batch (sincronização) |
| **Controle de qualidade** | Bias removal, Quality Check | Consistency check, Context Enrichment |
| **Complexidade** | Alta (embeding, vector search) | Média (merge + injection) |
| **Custo** | Mais alto (infra vetorial) | Mais baixo (contexto fixo) |

curadoria: completa
escopo: contextual
---

## Ver também

- [[ia-lgpd-egp-v9]] — Curso "IA e LGPD" (Bloco 2 menciona RAG)
- [[agentes-ia-roi-business-case]] — ROI de agentes de IA

curadoria: completa
escopo: contextual
---

*Infográfico capturado em 16/09/2026. Fonte: TikTok.*
