---
title: "Instrução Normativa TRE-PR 001/2026 — Sistema AcompVot (Eleições 2026)"
name: "Instrução Normativa TRE-PR 001/2026"
created: 2026-09-09
updated: 2026-09-09
type: norma
number: 001
year: 2026
status: vigente
curadoria: completa
escopo: contextual
status_verificacao: "Confirmada vigente em 2026-09-09: DJE-TRE-PR nº 177, 27/08/2026, p. 50-51 (portal compilado TRE-PR)."
confidence: high
fonte_publicacao: "https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2026/instrucao-normativa-no-001-de-24-de-agosto-de-2026"
data_publicacao: "24/08/2026"
tags: [norma, tre-pr, eleicoes, acompvot, urna, logistica-eleitoral, contextual]
sources: [references/raw/tre-pr-in-instrucao-normativa-001-de-24-de-agosto-de-2026-acompvot.md]
---

# Instrução Normativa TRE-PR 001/2026 — Sistema AcompVot

## Objeto / Ementa

Regulamenta a utilização do **Sistema AcompVot** no âmbito da Justiça Eleitoral do Paraná, a partir das Eleições Gerais 2026. O AcompVot dá suporte ao acompanhamento das atividades operacionais, logísticas e de infraestrutura do pleito.

## Escopo e classificação

Esta norma é de **tecnologia eleitoral operacional** (acompanhamento da votação), classificada como **`contextual`** — **consistente** com o tratamento dado às resoluções de auditoria de funcionamento das urnas ([[normas/tre-pr-resolucao-934-2024-auditoria-urnas]] e [[normas/tre-pr-resolucao-893-2022-auditoria-urnas]]), que integram o acervo com o mesmo escopo.

> **Nota de classificação (correção de 2026-09-09):** esta norma foi inicialmente mantida **fora do escopo** pelo monitoramento (relatório 2026-08-31) sob a premissa de ser "análoga às comissões de auditoria de votação, excluídas na rodada anterior". Essa premissa era **falsa** — as resoluções de auditoria de urnas **estão curadas** no acervo. A norma foi reclassificada para **`contextual`** e integrada ao vault. Ver ADR 0005 e `references/_meta/criterio-escopo.md`.

## Finalidade do sistema (art. 2º)

O AcompVot destina-se a:
- consulta de locais e seções eleitorais;
- registro e tratamento de ocorrências relacionadas às **urnas eletrônicas**;
- realização da **vistoria de véspera** por meio de QR Code;
- acompanhamento das **fases da votação**;
- registro e monitoramento de informações operacionais, logísticas e de infraestrutura do pleito.

## Pontos de SI/PDP presentes (proteções transversais)

Embora o objeto seja operacional/logístico, a norma contém proteções transversais relevantes:

- **Art. 3º** — acesso por perfis e permissões segundo atribuições; **vedado o compartilhamento de credenciais**.
- **Art. 11** — o tratamento de dados pessoais observa a **LGPD**, as normas da JE e as políticas institucionais de proteção de dados e segurança da informação.
  - §1º — acesso restrito a usuários autorizados, limitado ao necessário (menor privilégio).
  - §2º — vedado compartilhar credenciais, usar para finalidade diversa, reproduzir/armazenar/compartilhar indevidamente.

## Competências

- **SECPLEE** (Secretaria de Planejamento e Logística de Eleições e Estratégia) — coordenação operacional do AcompVot, definição de pesquisas/orientações (art. 8º).
- **SECTI** — suporte técnico, tratamento de indisponibilidades e falhas do sistema (art. 9º).
- **Zonas eleitorais** — cadastro de responsáveis por local de votação, orientação, verificação de ocorrências (art. 5º).

## Fundamentação

- Expedida pelo Diretor-Geral com base no **art. 35, VII, da Resolução TRE-PR 971/2026** (Regulamento da Secretaria).
- Considera o **art. 19, § 3º, da Resolução TSE 23.751/2026** (consulta de local e seção de votação).

## Relacionamentos

- [[normas/tre-pr-resolucao-934-2024-auditoria-urnas]] — Auditoria de funcionamento das urnas (mesmo escopo contextual)
- [[normas/tre-pr-resolucao-893-2022-auditoria-urnas]] — Auditoria de urnas (mesmo escopo contextual)
- [[normas/tre-pr-resolucao-971-2026-regulamento-secretaria]] — Regulamento da Secretaria (base de expedição)
- [[entities/secti]] — Secretaria de TI (suporte técnico ao sistema)

## Status

**Vigente** (DJE-TRE-PR nº 177, 27/08/2026, p. 50-51). Norma de vigência relacionada ao ciclo eleitoral 2026.
