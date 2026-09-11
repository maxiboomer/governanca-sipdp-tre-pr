---
title: "ANPD — Estudo Técnico: Anonimização de Dados na LGPD (Processo Baseado em Risco e Técnicas Computacionais)"
type: fonte-normativa
created: 2026-09-11
updated: 2026-09-11
status: vigente
curadoria: completa
escopo: central-si-pdp
confidence: high
status_verificacao: "Fonte oficial ANPD (gov.br), arquivo publicado em novembro/2023"
sources: [references/raw/anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-computacionais-2023.md]
tags: [anpd, anonimizacao, pseudonimizacao, lgpd, estudo-tecnico, tecnicas-computacionais, processo-risco]
fonte_publicacao: "Portal ANPD — Documentos Técnicos e Orientativos"
data_publicacao: 2023-11-01
---

# ANPD — Estudo Técnico: Anonimização de Dados na LGPD (Processo Baseado em Risco e Técnicas Computacionais)

Segundo da série de estudos técnicos sobre anonimização (novembro/2023). Abordagem computacional e metodológica do processo de anonimização. Complementa o [[normas/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023|Estudo 1 — Análise Jurídica]].

## Processo de Anonimização Baseado em Risco

Modelo proposto pela ANPD em etapas essenciais:

### 1. Identificação e compreensão do risco
- Mapear o contexto e as ameaças específicas
- Identificar identificadores diretos e indiretos no conjunto de dados
- Avaliar sensibilidade dos dados

### 2. Determinação do Risco de Reidentificação Aceitável (RRA)
- Definir o limite superior de risco tolerável
- Variáveis contextuais: sensibilidade dos dados (ex: sensíveis, financeiros reduzem o RRA), volume da base, natureza dos titulares

### 3. Escolha e aplicação de técnicas
- Ver tabela detalhada abaixo (Apêndice I do estudo original)
- Combinar múltiplas técnicas quando necessário

### 4. Avaliação do risco residual
- Medir o risco remanescente após a aplicação das técnicas
- Comparar com o RRA estabelecido
- Se superior ao RRA → o dado **não é considerado anonimizado**

### 5. Documentação contínua
- Registrar estados do conjunto de dados durante o processo
- Manter as propriedades estatísticas para a finalidade pretendida
- Trilha de auditoria completa

### 6. Monitoramento contínuo
- A anonimização é um **processo contínuo**, não um evento pontual
- Revisar periodicamente o risco à medida que novas técnicas de ataque emergem
- Atualizar as técnicas empregadas conforme o estado da técnica evolui

## O Dilema Utilidade × Anonimização

Conforme o gráfico do estudo (Figura 1):
- **Quanto maior a anonimização → menor a utilidade do dado**
- **Quanto maior a utilidade → menor a proteção (maior risco)**
- Existe um ponto ótimo onde ambos são maximizados, mas na prática depende de ajuste fino entre variáveis conflitantes

## Técnicas de Anonimização (Apêndice I — Caderno de Técnicas)

### Técnicas para Dados Textuais Estruturados

| Técnica | Descrição | Formato de dado |
|---------|-----------|-----------------|
| **Supressão** | Remoção completa de atributo/valor | Textual estruturado |
| **Generalização** | Substituição por valor mais genérico (ex: idade → faixa etária) | Textual estruturado |
| **Randomização** | Adição de ruído aleatório | Textual estruturado |
| **Permutação** | Embaralhamento de valores entre registros | Textual estruturado |
| **k-Anonimidade** | Garantir que cada registro é indistinguível de pelo menos k-1 outros | Textual estruturado |
| **l-Diversidade** | Generalização do k-anonimidade — exige diversidade de valores sensíveis em cada grupo | Textual estruturado |
| **t-Proximidade** | Garante que a distribuição de valores sensíveis em cada grupo reflete a distribuição global | Textual estruturado |
| **Mascaramento** | Substituição parcial de caracteres (ex: 123.456.789-XX) | Textual estruturado |

### Técnicas para Dados de Imagem e Vídeo

| Técnica | Descrição | Limitações |
|---------|-----------|------------|
| **Pixelização** | Substituição de região por blocos de pixels unificados | Dificuldade em definir parâmetros ideais |
| **Blur (Desfoque)** | Aplicação de filtro gaussiano sobre região de interesse (ex: face) | Requer identificação precisa da região |

### Técnicas para Dados Não Estruturados

| Técnica | Descrição |
|---------|-----------|
| **Named Entity Recognition (NER) + Supressão** | Identifica entidades (nomes, CPFs) e as remove do texto livre |
| **Hash one-way irreversível** | Quando a reversibilidade não é necessária |

## Técnicas de Pseudonimização

| Técnica | Descrição | Categoria |
|---------|-----------|-----------|
| **Substituição** | Troca do identificador por valor artificial irreversível (quando não há necessidade de reversibilidade) | Pseudonimização |
| **Função Hash** | Substituição por valor gerado por função hash (ex: SHA-256) | Pseudonimização |
| **Encriptação** | Substituição por valor cifrado — reversível com chave | Pseudonimização |

## Glossário de Métricas (Apêndice II)

| Métrica | Descrição |
|---------|-----------|
| **Métrica Base** | Valor calculado unicamente com base no próprio conjunto de dados (ex: tamanho da menor equivalência de classe) |
| **Métrica Contextual** | Métrica base incorporando elementos particulares (ex: sensibilidade dos dados, esforço de reidentificação) |
| **Risco de Reidentificação Aceitável (RRA)** | Limite superior tolerável — risco acima descaracteriza a anonimização |
| **Equivalência de Classe** | Subconjunto do conjunto de dados onde todos os registros são indistinguíveis entre si |

## Limitações Reconhecidas pela ANPD

1. **Nenhuma técnica é 100% eficaz** contra reidentificação
2. **Dados em fluxo (streaming)** exigem técnicas adaptadas
3. **Dados não estruturados** (texto livre, áudio, imagem) são mais difíceis de anonimizar que dados tabulares
4. A combinação de dados de múltiplas fontes (linking attack) pode reidentificar mesmo dados "anonimizados"

## Relacionamentos

- [[normas/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023]] — Estudo 1: fundamentos jurídicos
- [[normas/anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023]] — Estudo Preliminar (consulta)
- [[concepts/anonimizacao-pseudonimizacao-lgpd]] — Síntese temática (a criar)
