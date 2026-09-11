---
title: "ANPD — Estudo Técnico: Anonimização de Dados na LGPD (Análise Jurídica)"
type: fonte-normativa
created: 2026-09-11
updated: 2026-09-11
status: vigente
curadoria: completa
escopo: central-si-pdp
confidence: high
status_verificacao: "Fonte oficial ANPD (gov.br), arquivo publicado em novembro/2023"
sources: [references/raw/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023.md]
tags: [anpd, anonimizacao, pseudonimizacao, lgpd, estudo-tecnico, analise-juridica]
fonte_publicacao: "Portal ANPD — Documentos Técnicos e Orientativos"
data_publicacao: 2023-11-01
---

# ANPD — Estudo Técnico: Anonimização de Dados na LGPD (Análise Jurídica)

Primeiro da série de dois estudos técnicos sobre anonimização publicados pela ANPD (novembro/2023). Versão 1.0.

## Metodologia

Pesquisa teórica orientada pelos tipos metodológicos jurídico-compreensivo e jurídico-comparativo (com o direito da UE — GDPR, Article 29 Working Party, ENISA, diretivas 95/46/CE e 2016/679).

## Definições e Conceitos Fundamentais

### Dado Anonimizado (LGPD art. 5º, III)
> "dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento"

### Anonimização (LGPD art. 5º, XI)
> "utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo"

### Dado Pessoal — abordagem expansionista (art. 5º, I)
O conceito brasileiro adotou a perspectiva expansionista: inclui identificadores indiretos e a noção de "identificabilidade" — se é possível distinguir (*single out*) um indivíduo, ainda que por combinação de dados de diversas fontes, o dado é pessoal.

### Identificadores
| Tipo | Definição | Exemplos |
|------|-----------|----------|
| **Direto** | Permite identificar unicamente uma pessoa, sem necessidade de combinação | Nome completo, CPF |
| **Indireto** (quase-identificador) | Só não identifica sozinho, mas combinado com outros dados permite a reidentificação | Nacionalidade, idade, raça, CEP, endereço IP, características fenotípicas |

### Pseudonimização ≠ Anonimização
A LGPD distingue expressamente:
- **Pseudonimização** (art. 12, §1º e art. 13, §4º): dado pessoal que **pode** ser reidentificado com informações adicionais mantidas separadamente (chave de pseudonimização). **Continua sendo dado pessoal**.
- **Anonimização**: processo que, **com meios técnicos razoáveis**, torna impossível a associação ao indivíduo. **Deixa de ser dado pessoal**.

## Limite entre anonimização e pseudonimização (art. 12, §2º)

Os dados anonimizados **continuam sendo pessoais** quando:
1. O processo de anonimização for revertido utilizando **exclusivamente meios próprios**, OU
2. Quando, com **esforços razoáveis**, puder ser revertido

### Critérios para "esforços razoáveis"
A LGPD indica que devem ser considerados:
- **Custo** (econômico)
- **Tempo** de dedicação
- **Estado da técnica** disponível
- Força de trabalho e recursos humanos

### O que NÃO conta para "esforços razoáveis"
- Crimes cibernéticos
- Meios proibidos por lei

## O Processo de Anonimização como Tratamento

O ato inicial de anonimização de dados **configura operação de tratamento de dado pessoal** → atrai o regime jurídico da LGPD durante todo o processo.

### Anonimização como tratamento posterior (uso secundário)
Se a finalidade de anonimização não foi informada originalmente ao titular:
- Configura "tratamento posterior" ou uso secundário
- Deve ser **compatível** com a finalidade inicialmente informada (princípio da adequação — art. 6º, II)
- Precisa ter **finalidade específica, lícita e útil** — anonimizar sem finalidade útil não é válido

## Risco de (Re)Identificação

### Dois cenários
| Cenário | Descrição |
|---------|-----------|
| **Reidentificação do promotor** | O atacante **sabe** que um indivíduo específico está no conjunto e deseja encontrar o registro dele |
| **Reidentificação do jornalista** | O atacante **não sabe** quem está no conjunto e deseja reidentificar qualquer indivíduo |

### Risco zero não existe
Conforme Narayanan e Shmatikov (2010), **não há técnica de anonimização com eficácia plena** — todas estão sujeitas a ataques de reidentificação. A anonimização deve ser entendida como **processo contínuo baseado em risco**, não como estado discreto binário.

## Princípios da LGPD Aplicáveis à Anonimização

1. **Finalidade** (art. 6º, I): a anonimização deve ter finalidade específica, legítima e informada
2. **Adequação** (art. 6º, II): a anonimização como tratamento posterior deve ser compatível com a finalidade original
3. **Necessidade** (art. 6º, III): limitar ao mínimo necessário — se o fim pode ser alcançado sem anonimização integral, use técnicas menos restritivas
4. **Livre acesso** (art. 6º, IV): garantir que o titular possa consultar a forma e a duração do tratamento, inclusive da anonimização
5. **Qualidade dos dados** (art. 6º, V): após a anonimização, manter a qualidade estatística para a finalidade pretendida
6. **Transparência** (art. 6º, VII): informar a possibilidade/natureza da anonimização
7. **Prevenção** (art. 6º, VIII): adotar medidas para prevenir danos decorrentes da anonimização inadequada
8. **Responsabilização e prestação de contas** (art. 6º, X): documentar o processo de anonimização, as técnicas empregadas e a avaliação de riscos

## Dados Pseudonimizados (art. 13, §4º)

A LGPD prevê que a **análise de dados pessoais pelos órgãos de pesquisa** deve ser realizada, **sempre que possível**, de forma **pseudônima ou anônima**. Contudo, o dado pseudonimizado **continua sendo pessoal** e exige:
- Todas as salvaguardas da LGPD
- Gestão segura da chave de pseudonimização (mantida separadamente)
- Medidas de segurança e administrativas apropriadas

## Principais Conclusões do Estudo

1. A anonimização é um **processo**, não um estado discreto
2. Os conceitos de dado pessoal e dado anonimizado são **dinâmicos e contextuais**
3. A avaliação da anonimização deve se dar por **abordagem baseada em risco**
4. O critério dos "esforços razoáveis" exige análise concreta do estado da técnica, custo e tempo
5. A **abordagem relativa** (considerando o agente que trata) deve ser combinada com a identificação de esforços razoáveis de terceiros
6. A ANPD reconhece a complexidade técnica e jurídica do tema como autoridade reguladora

## Relacionamentos

- [[normas/anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-2023]] — Estudo Técnico 2: técnicas computacionais
- [[normas/anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023]] — Estudo Preliminar submetido à consulta
- [[normas/anpd-guia-legitimo-interesse-2024]] — Guia já publicado
- [[normas/anpd-guia-tratamento-dados-poder-publico-2023]] — Guia para setor público
- [[concepts/anonimizacao-pseudonimizacao-lgpd]] — Síntese temática (a criar)
- [[inventarios/regulamentacoes-anpd]] — Inventário das regulamentações ANPD
