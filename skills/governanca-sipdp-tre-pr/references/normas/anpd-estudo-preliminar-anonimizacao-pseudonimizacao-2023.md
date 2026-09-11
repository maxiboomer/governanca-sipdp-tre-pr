---
title: "ANPD — Estudo Preliminar: Anonimização e Pseudonimização para a Proteção de Dados Pessoais (Minuta do Guia)"
type: fonte-normativa
created: 2026-09-11
updated: 2026-09-11
status: vigente
curadoria: completa
escopo: central-si-pdp
confidence: high
status_verificacao: "Fonte oficial ANPD (Participa+Brasil), consulta pública de 30/01/2024 a 28/02/2024"
sources: [references/raw/anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023.md]
tags: [anpd, anonimizacao, pseudonimizacao, lgpd, estudo-preliminar, guia, minuta, consulta-publica]
fonte_publicacao: "Participa+Brasil — Consulta à Sociedade"
data_publicacao: 2023-12-01
---

# ANPD — Estudo Preliminar: Anonimização e Pseudonimização para a Proteção de Dados Pessoais

Minuta do Guia de Anonimização e Pseudonimização submetida à consulta pública (30/01/2024 a 28/02/2024). **Versão final do Guia ainda não foi publicada** (até setembro/2026).

## Status Atual

- **30/01/2024**: ANPD abriu consulta pública sobre a minuta
- **28/02/2024** (prorrogado até 04/03/2024): Prazo para contribuições
- **03/2024**: Consolidação das contribuições (Nota Técnica nº 12/2025/CON1/CGN/ANPD)
- **Fev/2025** (Balanço da Agenda Regulatória 2025-2026): *"A minuta final do Guia Orientativo estava em posse do Conselho Diretor para análise e aprovação. Porém, foi reencaminhada para a CGN para adequação a partir de informações supervenientes após a Tomada de Subsídios realizada no âmbito do processo de regulamentação do atual Item 6. Como resultado, foi elaborada a Nota Técnica nº 24/2025/CON1/CGN/ANPD, com a análise técnica suplementar em decorrência de fatos supervenientes à elaboração do Guia. A partir disso, remeteu-se nova minuta ao Conselho Diretor da ANPD para apreciação."*
- **23/12/2025**: Resolução CD/ANPD nº 31 manteve o tema como **Item 9 (Fase 1)** da Agenda Regulatória 2025-2026

## Conteúdo da Minuta

A minuta consolida os dois estudos técnicos de 2023 e adiciona:

### Processo de Anonimização (12 etapas propostas)
1. Determinação do Risco de Reidentificação Aceitável (RRA)
2. Identificação dos dados e finalidade
3. Seleção de técnicas de anonimização
4. Aplicação das técnicas
5. Avaliação do risco residual
6. Documentação do processo
7. Medidas de segurança e administrativas
8. Monitoramento contínuo
9. Governança do processo
10. Comunicação ao encarregado
11. Revisão periódica
12. Resposta a incidentes de reidentificação

### Processo de Pseudonimização (12 etapas correspondentes)
Metodologia similar, com ênfase na gestão segura da chave de pseudonimização e na manutenção do caráter pessoal do dado.

### Técnicas Reconhecidas pela ANPD

**Anonimização:**
- Supressão
- Generalização
- Mascaramento
- Adição de ruído
- Permutação
- Blur (desfocar)
- Pixelização

**Pseudonimização:**
- Substituição
- Função hash
- Encriptação

### Pontos em Aberto na Minuta

A própria minuta reconhece que alguns pontos não foram definitivamente resolvidos:
- Metodologia padronizada para cálculo do RRA (não é "one size fits all")
- Critérios quantitativos para "esforços razoáveis" (depende do contexto)
- Tratamento de dados sintéticos (não mencionado expressamente)
- Interseção com IA generativa e web scraping (emergente após a consulta)

## Estudos que Fundamentam a Minuta

A minuta é baseada nos dois estudos técnicos de novembro/2023:
- [[normas/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023]] — Análise Jurídica
- [[normas/anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-2023]] — Técnicas Computacionais

## Relacionamentos

- [[concepts/anonimizacao-pseudonimizacao-lgpd]] — Síntese temática
- [[inventarios/regulamentacoes-anpd]] — Inventário das regulamentações ANPD
- [[entities/anpd]] — A Autoridade
