---
title: "Norma Técnica SECTI Nº 006/2026 — Testes de Penetração (Pentest)"
name: "Norma Técnica SECTI Nº 006/2026"
created: 2026-09-09
updated: 2026-09-21
type: fonte-normativa
number: 006
year: 2026
status: vigente
curadoria: completa
escopo: central-si-pdp
status_verificacao: "Confirmada vigente em 2026-09-09: DJE-TRE-PR nº 192, 04/09/2026, p. 19-22 (publicação na página individual do compilado oficial TRE-PR)"
confidence: high
fonte_publicacao: "https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-no-006-de-28-de-agosto-de-2026"
data_publicacao: "28/08/2026"
tags: [norma, tre-pr, secti, norma-tecnica, pentest, testes-penetracao, seguranca-informacao, gestao-vulnerabilidades, lgpd, si-pdp]
sources: [references/raw/tre-pr-nt-secti-norma-tecnica-006-de-28-de-agosto-de-2026.md]
---

# Norma Técnica SECTI Nº 006/2026 — Testes de Penetração (Pentest)

## Finalidade e escopo

Esta norma integra o corpus de **SI/PDP** do TRE-PR. Estabelece os **procedimentos e responsabilidades** para a solicitação, autorização, execução e gestão dos resultados de **Testes de Penetração (Pentest)** na Justiça Eleitoral do Paraná, como ferramenta de validação da eficácia dos controles de segurança.

Publicada em 28/08/2026, pelo Secretário de TI (GILMAR JOSÉ FERNANDES DE DEUS) — **Vigente** (DJE-TRE-PR nº 192, 04/09/2026, p. 19-22). Complementa o arcabouço da PSI (Res. TRE-PR 974/2026; Res. TSE 23.763/2026) e da ENSEC-PJ (CNJ 396/2021).

## Fundamentos (CONSIDERANDO)

- Res. CNJ nº 396/2021 — Estratégia Nacional de Segurança Cibernética do Poder Judiciário (ENSEC-PJ).
- Res. TSE nº 23.763/2026 e Res. TRE-PR nº 974/2026 — Política de Segurança da Informação (PSI).
- Boas práticas ABNT NBR ISO/IEC 27001 e 27002; modelo **CIS Controls v8, Controle 18 (Penetration Testing)**.
- LGPD (Lei 13.709/2018) — implementar controles para tratamento de dados pessoais.
- Integração com o processo de Gestão de Riscos e Gestão de Vulnerabilidades do Tribunal.
- Portaria CNJ 162/2021, Anexo V (fiscalização de requisitos de segurança sob contratação externa / auditorias cruzadas).

## Estrutura normativa

| Capítulo | Arts. | Tema |
|---|---|---|
| I — Disposições Preliminares | 1º-2º | Objeto e observância à PSI (TSE 23.763/2026 e TRE-PR 974/2026) |
| II — Definições e Objetivos | 3º-4º | Glossário (Pentest, RoE, Gestor do Ativo) e 5 objetivos |
| III — Autorização e Escopo | 5º-8º | Termo de Autorização/RoE obrigatório; conteúdo mínimo; frequência |
| IV — Regras de Execução e Conduta | 9º-12º | Proibições expressas; interrupção; classificação da informação; contratação externa |
| V — Responsabilidades | 13º-15º | Papéis: SECTI, Gestores de Ativos, Equipe de Teste |
| VI — Gestão de Vulnerabilidades e Re-teste | 16º-18º | Prazos por CVSS; prorrogação; validação; risco residual ao CGSIPDP |
| VII — Disposições Finais | 19º-21º | Casos omissos; revisão; entrada em vigor |

## Obrigações e controles-chave

### Autorização obrigatória (arts. 5º-8º)
- **Nenhum Pentest inicia sem Termo de Autorização e Regras de Engajamento (RoE)** elaborado pela Coordenadoria de Segurança da Informação e aprovado pela SECTI.
- O RoE deve conter: escopo detalhado, ativos excluídos, metodologia (Black/Grey/White Box), identificação da equipe, cronograma/janelas, pontos de contato de emergência, regras de manuseio de dados sensíveis (LGPD), e comprovação de autorização de provedores de nuvem/terceiros.
- **Frequência obrigatória**: aplicações críticas expostas à Internet; antes da entrada em produção; após mudanças significativas na arquitetura de segurança.

### Proibições expressas (art. 9º)
- DoS/DDoS ou indisponibilidade de produção.
- Exfiltração, alteração ou destruição de dados reais (especialmente pessoais/sigilosos).
- Acesso a sistemas de terceiros fora do escopo.
- Engenharia social sem alinhamento prévio com a Administração Superior.

### Classificação e proteção de dados (art. 11º)
- Relatórios, dados brutos e informações coletadas: **[RESTRITO]** ou **[SECRETO]**.
- Armazenamento e transmissão **obrigatoriamente criptografados**.
- Alinhamento com a LGPD (Lei 13.709/2018).

### Prazos de remediação por CVSS (art. 16, § 1º)

| Criticidade | CVSS | Prazo | Ação |
|---|---|---|---|
| Crítica | 9.0-10.0 | **5 dias úteis** | Correção imediata ou controle compensatório urgente |
| Alta | 7.0-8.9 | **20 dias úteis** | Inclusão prioritária no ciclo de manutenção |
| Média | 4.0-6.9 | **60 dias úteis** | Planejamento conforme cronograma |
| Baixa | 0.1-3.9 | Conforme conveniência | Monitoramento ou correção futura |

### Risco residual (art. 18)
- Vulnerabilidade não corrigível → risco residual **formalmente documentado** e submetido ao **CGSIPDP** para **aceitação formal**.
- Casos omissos: resolvidos pelo **CGSIPDP** (art. 19º).
- Revisão da norma: mediante aprovação do **CGSIPDP** (art. 20º).

## Lacunas e pontos de atenção

| # | Lacuna | Risco | Sugestão |
|---|---|---|---|
| 1 | **Não define periodicidade mínima obrigatória** — art. 8º diz "frequência definida pelo GSI" mas não estabelece intervalo máximo (ex.: anual) | Testes podem não ser realizados com a frequência necessária | Incluir periodicidade mínima (ex.: anual para sistemas críticos) |
| 2 | **Prazo de 5 dias úteis para CVSS Crítico é muito curto** em ambiente judicial com equipes de TI sobrecarregadas | Descumprimento do prazo pode gerar passivo operacional | Considerar prazo escalonado (ex.: 10 dias) ou possibilidade de prorrogação imediata |
| 3 | **Não menciona comunicação de incidentes** — se o Pentest descobrir um incidente em andamento, não há previsão de acionamento da Res. TRE-PR 974/2026 (gestão de incidentes) | Lacuna na integração entre segurança ofensiva e resposta a incidentes | Adicionar obrigação de notificação imediata à Coordenadoria de Segurança da Informação |
| 4 | **Equipe de teste não tem qualificação mínima definida** — art. 12 exige NDA e "comprovação de qualificação técnica" mas não especifica certificações (ex.: OSCP, CEH, Pentest+) | Risco de teste de baixa qualidade gerar falso senso de segurança | Especificar certificações ou critérios mínimos de qualificação |
| 5 | **Não integra com o Plano de Continuidade de Negócios (PCN)** — testes em sistemas críticos podem impactar disponibilidade | Indisponibilidade não planejada durante testes | Adicionar exigência de janelas de baixo impacto e coordenação com o PCN |

## Relações normativas no vault

| Norma | Relação | Tipo |
|---|---|---|
| **Res. TRE-PR 974/2026** (PSI Local) | Observância obrigatória | Fundamento |
| **Res. TSE 23.763/2026** (PSI Nacional) | Observância obrigatória | Fundamento |
| **Res. CNJ 396/2021** (ENSEC-PJ) | Fundamento | Fundamento |
| **Portaria CNJ 162/2021** (fiscalização segurança) | Complementar — Anexo V | Complemento |
| **Portaria DG/TSE 444/2021** (norma de termos PSI) | Definições acrescidas | Complemento |
| **NT SECTI 005/2026** (Linux) | Normas da mesma série | Correlata |
| **LGPD (Lei 13.709/2018)** | Obrigação transversal nos testes | Fundamento |
| **Res. CNJ 335/2020** (PDPJ-Br) | Contexto de plataformas digitais | Contextual |

## Impacto para o TRE-PR

### Para a SECTI / Coordenadoria de Segurança da Informação
- **Novo processo operacional obrigatório**: elaboração de plano anual de Pentest, Termos de Autorização, supervisão de execução, validação de relatórios.
- **Necessidade de capacitação**: equipe precisa dominar metodologias (Black/Grey/White Box), CVSS, e redação de RoE.
- **Classificação de informações**: necessidade de implementar [RESTRITO] e [SECRETO] nos relatórios de Pentest.

### Para os Gestores de Ativos (Administrativo, Judiciário, Zonas)
- **Nova responsabilidade formal**: aprovar Termos de Autorização, elaborar Planos de Ação de remediação, implementar correções nos prazos.
- **Prazos rígidos**: 5 dias úteis para vulnerabilidades críticas (CVSS 9.0-10.0).
- **Necessidade de inventário atualizado**: saber quais são os "ativos" sob sua responsabilidade.

### Para o CGSIPDP
- **Nova competência**: apreciar risco residual de vulnerabilidades não corrigíveis (art. 18) e resolver casos omissos (art. 19).
- **Necessidade de agenda**: incluir na pauta a apreciação de riscos residuais.

### Para a Auditoria Interna do TRE-PR
- **Novo objeto de auditoria**: verificar se o plano anual de Pentest está sendo executado, se os prazos de remediação estão sendo cumpridos, se o CGSIPDP está apreciando riscos residuais.
- **Evidências**: Termos de Autorização, relatórios de vulnerabilidade, Planos de Ação.

## Recomendações

1. **Acionar a SECTI** para elaboração do plano anual de Pentest (obrigação implícita no art. 13, I).
2. **Sincronizar com a Res. TRE-PR 974/2026** — se ainda não houver, criar processo de comunicação de incidentes durante Pentest.
3. **Auditoria Interna do TRE-PR** — incluir no plano de auditoria 2026/2027 a verificação da execução do plano anual de Pentest e cumprimento dos prazos de remediação.
4. **Propor à SECTI** a inclusão de periodicidade mínima obrigatória na próxima revisão da NT (art. 8º).

## Status normativo

**Vigente** — publicada em 28/08/2026 (DJE-TRE-PR nº 192, 04/09/2026, p. 19-22). Sem revogações expressas. Revisão sempre que necessário, mediante aprovação do CGSIPDP (art. 20).

## Relacionamentos

- [[entities/cgsipdp]] — Comitê Gestor de SI e Proteção de Dados Pessoais (aprecia risco residual; casos omissos)
- [[entities/secti]] — Secretaria de TI (aprova Termo; supervisiona; valida relatórios)
- [[normas/tre-pr-resolucao-974-2026-psi-local]] — PSI local (res. 974/2026), observada por esta norma
- [[normas/psi-tse-23763-2026]] — PSI nacional (Res. TSE 23.763/2026)
- [[normas/cnj-resolucao-396-2021-ensec-pj]] — ENSEC-PJ (fundamento)
- [[normas/tre-pr-in-dg-08-2019-vulnerabilidades]] — Gestão de Vulnerabilidades (processo que esta norma integra)
- [[concepts/seguranca-informacao-justica-eleitoral]] — Segurança da Informação na JE
