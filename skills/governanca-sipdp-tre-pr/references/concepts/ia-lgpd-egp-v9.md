---
title: "IA e LGPD — Escola de Governo do Paraná (V9, agosto/2026)"
created: 2026-09-15
updated: 2026-09-15
type: concept
status: vigente
status_verificacao: "Documento DOCX V9 capturado em 15/09/2026 — Escola de Governo do Paraná"
tags: [ia, lgpd, egp, capacitacao, setor-publico, roteiro, tre-pr]
sources: [material-ia-lgpd-egp-v9__2_.docx]
version: "V9"
date_captured: 2026-09-15
---

# IA e LGPD — Escola de Governo do Paraná (V9, agosto/2026)

> Roteiro completo do treinamento "IA e LGPD: Equilíbrio entre Inovação, Segurança e Ética" — Escola de Governo do Paraná (EGP). Versão 9, capturada em 15/09/2026.

## Visão Geral

| Campo | Detalhe |
|-------|---------|
| **Título** | IA e LGPD: Equilíbrio entre Inovação, Segurança e Ética |
| **Versão** | V9 (agosto/2026) |
| **Duração** | 120 min (90 min conteúdo + 30 min tira-dúvidas) |
| **Formato** | Webinar/virtual ao vivo, gravado por padrão |
| **Instrutor** | Roteiro completo com notas de condução |
| **Público** | Servidores públicos (municipal, estadual, federal) |

---

## Cronograma da sessão (120 minutos)

| Bloco | Tema | Duração | Acumulado |
|-------|------|---------|-----------|
| 1 | Abertura e panorama: IA no setor público | 10 min | 0:10 |
| 2 | LGPD aplicada a sistemas de IA | 20 min | 0:30 |
| 3 | Riscos de viés e decisões automatizadas | 20 min | 0:50 |
| 4 | RIPD para projetos de IA (versão enxuta) | 15 min | 1:05 |
| 5 | Governança mínima viável + checklist prático | 25 min | 1:30 |
| 6 | Tira-dúvidas dedicado | 30 min | 2:00 |

---

## Bloco 1 — Abertura e panorama (10 min)

### Objetivo
Situar os participantes: por que este tema é urgente para o órgão em que trabalham.

### Enquadramento
1. O núcleo da LGPD é comum a toda a administração pública, mas cada esfera tem arcabouço próprio de controle, contratação de TI e designação de encarregado
2. Este é um curso de capacitação, **não consultoria**: não serão avaliados casos concretos de órgãos identificáveis
3. As opiniões são pessoais do instrutor e não representam posição institucional

### Ganho de abertura — o dilema (3 min)
*"Chega um pedido de acesso à informação. O cidadão quer a lista de beneficiários de um programa público — quem recebeu, quanto, quando. A Lei de Acesso à Informação diz que informação pública é a regra e o sigilo é a exceção. A LGPD diz que dado pessoal exige base legal, finalidade e minimização. As duas leis estão em vigor ao mesmo tempo. O que você responde?"*

### Conteúdo — Panorama regulatório
- **LGPD (Lei 13.709/2018)** é lei desde 2018, mas boa parte da administração pública ainda está em estágio inicial de maturidade
- **Não há, hoje, lei federal específica de IA em vigor no Brasil**
- O que a IA muda é a **escala do risco**, não a norma aplicável
- **Resolução CNJ nº 615, de 11/03/2025** — disciplina desenvolvimento, governança, auditoria e uso de IA no Poder Judiciário (exceto STF), com abordagem por níveis de risco e exigência de supervisão humana efetiva
  - ⚠️ **Não se aplica a municípios nem ao Executivo** — é paradigma de desenho regulatório, não norma a ser cumprida pelo público deste curso

### [NOVO NA V9] PL 2338/2023 (Marco Legal da IA)
- Aprovado pelo Senado em dezembro/2024
- **Ainda NÃO é lei** — está na Câmara dos Deputados, parado na fase de parecer do relator na Comissão Especial
- Cinco datas de votação já foram marcadas e perdidas desde novembro/2025
- Em 24/08/2026 o relator adiou a decisão para depois das eleições de outubro/2026

### Resoluções CD/ANPD vigentes que mudam o dia a dia
- **Res. 15/2024** — Comunicação de Incidente de Segurança
- **Res. 18/2024** — Encarregado/DPO
- **Res. 19/2024** — Transferência Internacional
- **Res. 32/2026** — Adequação UE

### Casos de uso comuns na administração pública
- Chatbots de atendimento ao cidadão (WhatsApp, sites)
- Triagem de solicitações e priorização de atendimento (saúde, assistência social)
- Apoio a decisões administrativas: geração de pareceres, minutas, respostas a ofícios

> **Ponto-chave:** toda vez que um sistema processa dado de uma pessoa identificável, a LGPD já se aplica — independente do sistema ser "IA" ou uma planilha comum.

---

## Bloco 2 — LGPD aplicada a sistemas de IA (20 min)

### Objetivo
Dar um critério prático para saber quando um projeto de IA "vira" um problema de LGPD.

### Regra prática
Se a entrada (input) ou a saída (output) do sistema contém informação sobre pessoa identificada ou identificável, **há tratamento de dados pessoais**.

### Armadilha comum
- "é só um teste" — não é base legal
- "são dados anonimizados" — dado pseudonimizado **ainda é dado pessoal** (art. 12 LGPD)

### Bases legais aplicáveis
- **Art. 7º, II** — cumprimento de obrigação legal pelo controlador
- **Art. 7º, III** — execução de políticas públicas pela administração pública

> ⚠️ Nenhuma dessas bases dispensa documentação: a base legal precisa estar registrada no RoPA/inventário de tratamento do órgão.

### Modelos de terceiros: quem é quem

| Situação | Enquadramento |
|----------|---------------|
| Órgão usa API de modelo de fornecedor privado | Órgão é controlador; fornecedor é operador — precisa de cláusula contratual de proteção de dados |
| Servidor usa ferramenta de IA gratuita e pessoal para redigir documento oficial | Compartilhamento não autorizado de dados com terceiro — risco alto, sem base legal |
| Sistema de IA desenvolvido internamente, hospedado em infra do órgão | Órgão é controlador único — responsabilidade integral pela conformidade |

### Transferência Internacional (Res. CD/ANPD 19/2024 e 32/2026)
- Pergunta crítica: **onde o modelo de IA processa os dados?**
- Se a API está hospedada fora do Brasil, há transferência internacional — mesmo que a infraestrutura do órgão seja local
- Exige cláusula-padrão (Res. 19/2024) ou adequação (Res. 32/2026)

### [NOVO NA V5] Menção a RAG
- RAG (Retrieval-Augmented Generation) — arquitetura que reduz risco de transferência
- A IA consulta a base de dados do próprio órgão em vez de só depender de conhecimento genérico do modelo
- MGI tem guia prático sobre isso

---

## Bloco 3 — Riscos de viés e decisões automatizadas (20 min)

### Objetivo
Mostrar que viés algorítmico é um risco concreto em decisões administrativas.

### Como o viés entra no sistema
- **Viés de dados históricos**: sistema aprende com decisões passadas que já discriminavam
- **Viés de proxy**: variáveis aparentemente neutras (bairro, CEP) funcionam como substitutas de raça/classe
- **Viés de exclusão**: sistemas treinados com pouca representatividade erram mais para esses grupos

### Onde pesa mais na administração pública
- Assistência social: priorização automática de quem recebe visita/benefício
- Saúde e segurança: triagem de urgência, fila de atendimento

> **Frase para usar em sala:** "A pergunta não é se o sistema é neutro. Nenhum sistema treinado com dados históricos é neutro. A pergunta é: quem revisa a decisão antes que ela afete a vida de alguém?"

### Direito à explicação (art. 20, LGPD)
- O titular tem direito a solicitar revisão de decisão tomada unicamente com base em tratamento automatizado
- "Revisão" pressupõe **supervisão humana real** — não um funcionário que apenas clica "aprovar"
- Nenhuma decisão que gera impacto relevante para o cidadão deveria ser 100% automática sem checkpoint humano documentado

### Convergência regulatória
- **Resolução CNJ nº 615/2025** estrutura IA por níveis de risco e impõe supervisão humana efetiva
- Art. 20 LGPD e Res. 615/2025 partem de lugares diferentes e chegam ao mesmo ponto: decisão que afeta pessoa precisa de humano responsável no circuito

---

## Bloco 4 — RIPD para projetos de IA (15 min)

### Objetivo
Dar um roteiro simples para o órgão aplicar sem depender de consultoria externa.

### Quando o RIPD é necessário (critério ANPD)
O tratamento é de alto risco quando estão presentes, **ao mesmo tempo**, pelo menos 1 critério geral E pelo menos 1 critério específico:

**Critérios gerais (precisa de pelo menos 1):**
- Tratamento em larga escala
- Tratamento que afeta significativamente interesses e direitos fundamentais dos titulares

**Critérios específicos (precisa de pelo menos 1):**
- Uso de tecnologias emergentes ou inovadoras (IA generativa, foundation models)
- Vigilância ou controle de zonas acessíveis ao público
- Decisões tomadas unicamente com base em tratamento automatizado
- Uso de dados sensíveis, de crianças, adolescentes ou idosos

> **Na prática:** quase todo projeto de IA já atende a um critério específico (é "tecnologia emergente" por definição). Por isso, na prática, quando há IA com efeito real sobre pessoas, **assuma que o RIPD é necessário**.

### [NOVO NA V8] Estrutura mínima de um RIPD para IA (mnemônico de 5 seções)

1. **Descrição** — o que o sistema faz, quais dados usa, de onde vêm
2. **Necessidade e proporcionalidade** — por que a IA é necessária, existe alternativa menos invasiva?
3. **Identificação de riscos** — viés, vazamento, uso indevido, decisão errada sem revisão
4. **Medidas de mitigação** — supervisão humana, auditoria periódica, canal de contestação
5. **Responsáveis** — quem assina o RIPD, quem monitora depois

> ⚠️ **Este mnemônico é síntese didática do instrutor** — para elaborar um RIPD de verdade, use o **Modelo oficial do MGI/PPSI 2.0** (7 seções) que vai no material de apoio.

### [NOVO NA V5] AIE do MGI
- Autoavaliação de Impacto Ético em IA — framework em 4 níveis (Baixo, Médio, Alto, Excessivo)
- **Complementa, não substitui**, o critério de RIPD da ANPD

### [NOVO NA V6] AIA da LAPIN
- Avaliação de Impacto Algorítmico — proposta doutrinária de organização da sociedade civil
- **Não é lei nem norma vigente** — é referência doutrinária

---

## Bloco 5 — Governança mínima viável (25 min)

### Objetivo
Entregar uma estrutura que um órgão de pequeno porte consegue implementar sem grande orçamento.

### Estrutura de responsabilidades
| Papel | Atribuição |
|-------|------------|
| **Encarregado (DPO)** | Formalmente designado por portaria (Res. 18/2024), independência funcional, atribuições claras em portaria |
| **Ponto focal de TI** | Quem tecnicamente entende o que cada sistema de IA faz |
| **Gestor da área finalística** | Quem responde pelo impacto da decisão no cidadão |

> ⚠️ Esses três papéis podem ser 3 pessoas ou, em órgão pequeno, 2 — mas **nunca uma pessoa isolada** decidindo sozinha sobre IA.

### Transparência ativa (compatibilizando LGPD + LAI)
- Publicar lista simples dos sistemas de IA em uso e sua finalidade
- Se RIPD foi elaborado, publicar resumo público (art. 32 LGPD)
- Disponibilizar canal para o cidadão contestar decisão automatizada (art. 20 LGPD)
- Atualizar política de privacidade do órgão mencionando uso de IA

### Os três movimentos — método de decisão rápida

| Movimento | Pergunta que você faz a si mesmo |
|-----------|----------------------------------|
| **1. IDENTIFICAR** | Tem dado pessoal aqui? Olhe a entrada E a saída. Se não, siga em frente sem burocracia. |
| **2. JUSTIFICAR** | Com que base legal e para qual finalidade? A finalidade precisa ser específica, não genérica. |
| **3. DOCUMENTAR** | Quem responde por isso e onde está registrado? Se não está no registro de operações, não passou pelo Encarregado e não tem responsável nomeado, não existe do ponto de vista de conformidade. |

> **Frase de fechamento:** "Se vocês esquecerem tudo o que eu falei hoje e lembrarem só de três perguntas — tem dado pessoal? com que base e para quê? quem responde e onde está registrado? — o curso terá valido a pena."

### Checklist prático — antes de colocar qualquer sistema de IA em produção

- [ ] Existe DPO formalmente designado?
- [ ] O tratamento de dados pelo sistema está registrado no inventário/RoPA?
- [ ] A base legal está documentada?
- [ ] Foi avaliado se há dado sensível envolvido?
- [ ] Existe checkpoint humano antes de decisões com impacto relevante?
- [ ] Existe canal para o cidadão contestar uma decisão?
- [ ] Se envolve fornecedor externo, o contrato tem cláusula de proteção de dados?
- [ ] Foi feita triagem de necessidade de RIPD?

### Checklist específico de RIPD para IA (se projeto passar na triagem)

- [ ] O sistema toma decisões com efeito jurídico ou similar significativo sobre o titular?
- [ ] Há canal de revisão humana ativo ANTES de qualquer decisão ter efeito?
- [ ] Como foi avaliado o viés do modelo? Em quais grupos protegidos?
- [ ] A acurácia do modelo é homogênea entre grupos?
- [ ] Qual é a base legal específica para coleta dos dados de treinamento?
- [ ] Há risco de reidentificação a partir das saídas do modelo?
- [ ] Como será documentada a lógica geral do modelo ao cidadão que solicitar?
- [ ] Há monitoramento contínuo de drift e discriminação desigual?
- [ ] Se há operador, a cláusula contratual veda uso dos inputs para treino do fornecedor?
- [ ] Há transferência internacional de dados? Qual o mecanismo de proteção?

> ⚠️ **Se QUALQUER resposta for "não" ou "não sei"**, RIPD é obrigatório antes de go-live.

---

## Bloco 6 — Tira-dúvidas dedicado (30 min)

### Regras de condução para sessão virtual
- Perguntas pelo chat OU por voz (levantar a mão virtual)
- Se alguém começar a relatar caso próprio identificável — agradeça e reconduza para a formulação hipotética
- Reserve os últimos 3 minutos para encerramento

### Respostas-padrão (consulta durante o bloco)
- Pergunta sobre órgão identificável → não avalio caso concreto em sessão aberta
- Cidadão sobre direito próprio → indicar caminho institucional (Encarregado, ANPD, Defensoria)
- Servidor sobre conflito com chefia → tratar critério técnico em abstrato
- Pergunta fora do núcleo LGPD → reconhecer o limite e indicar área competente

---

## Material de apoio — Referências normativas

### Normas citadas
- **Lei nº 13.709/2018 (LGPD)** — arts. 6º, 7º, 12, 20, 23, 32, 37, 38, 41, 52
- **Lei nº 12.527/2011 (LAI)** — em especial art. 31
- **Resolução CD/ANPD nº 2/2022** — Agentes de pequeno porte (critérios de alto risco/RIPD)
- **Resolução CD/ANPD nº 15/2024** — Comunicação de Incidente de Segurança
- **Resolução CD/ANPD nº 18/2024** — Encarregado pelo tratamento de dados pessoais
- **Resolução CD/ANPD nº 19/2024** — Transferência Internacional de Dados Pessoais
- **Resolução CD/ANPD nº 32/2026** — Reconhecimento da União Europeia como organismo adequado
- **Resolução CNJ nº 615/2025** — IA no Poder Judiciário (substitui Res. 332/2020)
- **Guia Orientativo ANPD** — Tratamento de Dados Pessoais pelo Poder Público (junho/2023)
- **Guia ANPD** — Agentes de Tratamento e Encarregado

### [NOVO NA V9] PL 2338/2023 — Marco Legal da IA
- Situação em setembro/2026: aprovado pelo Senado em 10/12/2024, remetido à Câmara em março/2025
- Aguarda parecer do relator na Comissão Especial há mais de 16 meses
- Cinco datas de votação já foram marcadas e perdidas

### Materiais complementares MGI (entregues em PDF)
- Infográfico "Boas Práticas" — uso responsável de IA generativa no dia a dia
- Infográfico "Você sabe o que é RAG?" — Retrieval-Augmented Generation
- Infográfico "Ética em IA" — Framework AIE (Autoavaliação de Impacto Ético)

### [NOVO NA V8] Modelo oficial de RIPD (MGI/PPSI 2.0)
- Template completo (7 seções): contexto, tratamento dos dados, princípios da LGPD, direitos dos titulares, gestão de riscos, histórico, aprovação
- Versão 1.0, 31/07/2026
- Disponível em: gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0

### [NOVO NA V6] Material complementar adicional
- Relatório "Avaliação de Impacto Algorítmico para Proteção dos Direitos Fundamentais" — LAPIN, abril/2023

---

## Condução em sessão aberta — regras de segurança

1. Anunciar na abertura: opiniões pessoais, sem vinculação institucional
2. **Não solicitar relato de caso real**, nome de órgão ou reconhecimento de conduta própria
3. **Não emitir juízo sobre legalidade de conduta de órgão identificável**
4. Perguntas de cidadãos sobre direitos próprios → indicar caminho institucional
5. Servidor sobre conflito com chefia → tratar critério técnico em abstrato
6. **A transmissão é gravada por padrão** — tratar como certeza operacional
7. **O chat é parte do registro da sessão** — tratar com mesmo cuidado da fala

---

## Versionamento

| Versão | Data | Mudanças principais |
|--------|------|-------------------|
| V1 | — | Versão original |
| V2 | — | Gancho de abertura (dilema LAI × LGPD), três movimentos |
| V3 | — | Correção normativa (fundamentação checklist RIPD) |
| V4 | — | Modalidade virtual, regras para gravação e chat |
| V5 | — | Materiais MGI (AIE, RAG, infográficos), modelo RIPD |
| V6 | — | LAPIN AIA, status PL 2338/2023 |
| V7 | — | Res. 2/2022 na lista de referências |
| V8 | — | Reformulação dos 5 elementos de RIPD, modelo MGI |
| **V9** | **agosto/2026** | **Status do PL 2338/2023, etapas até sanção** |

---

## Ver também

- [[anpd-resolucao-15-2024-incidente-seguranca]] — Res. CD/ANPD 15/2024
- [[anpd-resolucao-18-2024-encarregado]] — Res. CD/ANPD 18/2024
- [[anpd-resolucao-19-2024-rtid]] — Res. CD/ANPD 19/2024
- [[anpd-resolucao-32-2026-adequacao-ue]] — Res. CD/ANPD 32/2026
- [[anpd-resolucao-02-2022-pequeno-porte]] — Res. CD/ANPD 2/2022

---

*Dados capturados em 15/09/2026. Fonte: material-ia-lgpd-egp-v9__2_.docx — Escola de Governo do Paraná. Versão 9, agosto/2026.*
