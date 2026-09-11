---
title: "Anonimização e Pseudonimização — Síntese LGPD/ANPD"
type: concept
created: 2026-09-11
updated: 2026-09-11
status: vigente
curadoria: completa
escopo: central-si-pdp
confidence: high
status_verificacao: "Baseado em 3 documentos oficiais ANPD (2 estudos técnicos + estudo preliminar) publicados entre nov/2023 e fev/2024"
sources:
  - references/raw/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023.md
  - references/raw/anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-computacionais-2023.md
  - references/raw/anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023.md
tags: [anonimizacao, pseudonimizacao, lgpd, anpd, sintese, conceito]
---

# Anonimização e Pseudonimização — Síntese LGPD/ANPD

Síntese consolidada das informações vigentes sobre anonimização e pseudonimização de dados pessoais no Brasil, baseada nos três documentos oficiais da ANPD.

## Definições Legais (LGPD)

| Termo | Definição (art. 5º) | Base legal |
|-------|---------------------|------------|
| **Dado anonimizado** (III) | "dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento" | LGPD art. 5º, III |
| **Anonimização** (XI) | "utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo" | LGPD art. 5º, XI |
| **Pseudonimização** | Dado pessoal que pode ser reidentificado com informações adicionais mantidas separadamente (chave de pseudonimização) | LGPD art. 12, §1º; art. 13, §4º |

## Diferença Fundamental

| Característica | Anonimização | Pseudonimização |
|----------------|--------------|-----------------|
| **Reversibilidade** | Irreversível (com meios razoáveis) | Reversível (com chave) |
| **Natureza jurídica** | Dado **não-pessoal** (fora da LGPD) | Dado **pessoal** (sujeito à LGPD) |
| **Escopo da LGPD** | Não se aplica ao dado anonimizado | Aplica-se integralmente |
| **Técnicas típicas** | Supressão, generalização, randomização, k-anonimidade, pixelização, blur | Substituição, hash, encriptação |
| **Risco de reidentificação** | Minimizado (não-zero) | Inerente (chave mantida separadamente) |

## O Limite entre Anonimização e Pseudonimização (art. 12, §2º)

Dados anonimizados **continuam sendo pessoais** quando:
1. O processo for revertido utilizando **exclusivamente meios próprios**, OU
2. Quando, com **esforços razoáveis**, puder ser revertido

### Fatores para "esforços razoáveis"
- Custo econômico
- Tempo de dedicação
- Estado da técnica disponível
- Força de trabalho e recursos humanos

### O que NÃO conta
- Crimes cibernéticos
- Meios proibidos por lei

## O Processo de Anonimização (Modelo ANPD)

A ANPD propõe um processo contínuo baseado em risco, com as seguintes etapas:

### 1. Determinação do Risco de Reidentificação Aceitável (RRA)
- Definir o limite superior de risco tolerável
- Variáveis: sensibilidade dos dados, volume da base, natureza dos titulares
- **Não existe metodologia padronizada** — depende do contexto

### 2. Identificação dos Dados e Finalidade
- Mapear identificadores diretos e indiretos
- Definir a finalidade específica da anonimização
- Verificar compatibilidade com a finalidade original (se tratamento posterior)

### 3. Seleção de Técnicas
- Ver tabela abaixo
- Combinar múltiplas técnicas quando necessário

### 4. Aplicação das Técnicas
- Aplicar as técnicas selecionadas ao conjunto de dados
- Documentar cada etapa

### 5. Avaliação do Risco Residual
- Medir o risco remanescente
- Comparar com o RRA
- Se superior ao RRA → o dado **não é considerado anonimizado**

### 6. Documentação
- Registrar estados do conjunto de dados
- Manter propriedades estatísticas para a finalidade pretendida
- Trilha de auditoria completa

### 7. Medidas de Segurança e Administrativas
- Controle de acesso aos dados anonimizados
- Proteção da chave de pseudonimização (se aplicável)
- Governança do processo

### 8. Monitoramento Contínuo
- A anonimização é um **processo contínuo**, não um evento pontual
- Revisar periodicamente o risco
- Atualizar técnicas conforme o estado da técnica evolui

### 9. Governança do Processo
- Definir responsáveis
- Estabelecer políticas de revisão
- Integrar com o programa de privacidade

### 10. Comunicação ao Encarregado
- Informar o DPO sobre o processo de anonimização
- Registrar no ROPA (art. 37)

### 11. Revisão Periódica
- Reavaliar o RRA periodicamente
- Atualizar técnicas conforme novas ameaças emergem

### 12. Resposta a Incidentes de Reidentificação
- Ter plano de resposta para casos de reidentificação
- Comunicar à ANPD se houver incidente de segurança

## Técnicas Reconhecidas pela ANPD

### Técnicas de Anonimização

| Técnica | Descrição | Formato |
|---------|-----------|---------|
| **Supressão** | Remoção completa de atributo/valor | Textual estruturado |
| **Generalização** | Substituição por valor mais genérico | Textual estruturado |
| **Randomização** | Adição de ruído aleatório | Textual estruturado |
| **Permutação** | Embaralhamento de valores entre registros | Textual estruturado |
| **k-Anonimidade** | Cada registro indistinguível de k-1 outros | Textual estruturado |
| **l-Diversidade** | Diversidade de valores sensíveis em cada grupo | Textual estruturado |
| **t-Proximidade** | Distribuição de valores sensíveis reflete a global | Textual estruturado |
| **Mascaramento** | Substituição parcial de caracteres | Textual estruturado |
| **Pixelização** | Substituição de região por blocos de pixels | Imagem/vídeo |
| **Blur (Desfoque)** | Aplicação de filtro gaussiano | Imagem/vídeo |
| **NER + Supressão** | Identificação e remoção de entidades em texto livre | Texto não estruturado |

### Técnicas de Pseudonimização

| Técnica | Descrição |
|---------|-----------|
| **Substituição** | Troca do identificador por valor artificial |
| **Função Hash** | Substituição por valor gerado por função hash (ex: SHA-256) |
| **Encriptação** | Substituição por valor cifrado — reversível com chave |

## Cenários de Reidentificação

| Cenário | Descrição |
|---------|-----------|
| **Reidentificação do promotor** | Atacante **sabe** que um indivíduo específico está no conjunto e deseja encontrar o registro |
| **Reidentificação do jornalista** | Atacante **não sabe** quem está no conjunto e deseja reidentificar qualquer indivíduo |

## Princípios da LGPD Aplicáveis

1. **Finalidade** (art. 6º, I): a anonimização deve ter finalidade específica, legítima e informada
2. **Adequação** (art. 6º, II): a anonimização como tratamento posterior deve ser compatível com a finalidade original
3. **Necessidade** (art. 6º, III): limitar ao mínimo necessário
4. **Livre acesso** (art. 6º, IV): garantir que o titular possa consultar a forma e a duração do tratamento
5. **Qualidade dos dados** (art. 6º, V): manter a qualidade estatística após a anonimização
6. **Transparência** (art. 6º, VII): informar a possibilidade/natureza da anonimização
7. **Prevenção** (art. 6º, VIII): adotar medidas para prevenir danos decorrentes de anonimização inadequada
8. **Responsabilização e prestação de contas** (art. 6º, X): documentar o processo

## O Dilema Utilidade × Anonimização

- Quanto maior a anonimização → menor a utilidade do dado
- Quanto maior a utilidade → menor a proteção (maior risco)
- Existe um ponto ótimo, mas na prática depende de ajuste fino entre variáveis conflitantes

## Status Atual (setembro/2026)

- **Estudos Técnicos (nov/2023)**: Publicados, vigentes
- **Estudo Preliminar/Minuta (jan/2024)**: Consulta pública encerrada, versão final **ainda não publicada**
- **Guia de Anonimização e Pseudonimização**: Item 9 (Fase 1) da Agenda Regulatória 2025-2026

## Aplicação ao TRE-PR

Para o TRE-PR, a anonimização e pseudonimização são relevantes para:
- Dados de eleitores em estudos e pesquisas (art. 13, §4º)
- Compartilhamento de dados com órgãos de pesquisa
- Estatísticas e relatórios públicos
- Testes de integridade e auditorias (Res. 893/2022, 934/2024)
- Tratamento de dados pelo Poder Público (art. 23)

## Relacionamentos

- [[normas/anpd-estudo-tecnico-anonimizacao-analise-juridica-2023]] — Estudo 1: fundamentos jurídicos
- [[normas/anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-2023]] — Estudo 2: técnicas computacionais
- [[normas/anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023]] — Estudo Preliminar (minuta do Guia)
- [[normas/anpd-guia-tratamento-dados-poder-publico-2023]] — Guia para setor público
- [[inventarios/regulamentacoes-anpd]] — Inventário das regulamentações ANPD
- [[entities/anpd]] — A Autoridade
