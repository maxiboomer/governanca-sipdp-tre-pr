---
title: "Norma Técnica SECTI Nº 006/2026 — Testes de Penetração (Pentest)"
name: "Norma Técnica SECTI Nº 006/2026"
created: 2026-09-09
updated: 2026-09-09
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

## Pontos-chave (objeto)

- **Autorização obrigatória**: nenhum Pentest, interno ou externo, inicia sem autorização formal escrita em *Termo de Autorização e Regras de Engajamento* (RoE), elaborado pela Coordenadoria de Segurança da Informação e aprovado pela SECTI (arts. 5º-6º).
- **Conteúdo mínimo do Termo** (art. 7º): escopo detalhado (IPs/URLs/sistemas); ativos/técnicas excluídos; metodologia (Black/Grey/White Box); identificação dos pentesters; cronograma/janelas; pontos de contato de emergência; regras de manuseio de dados sensíveis/pessoais (LGPD); comprovação de autorização prévia junto a provedores de nuvem/terceiros.
- **Frequência definida pelo GSI** (art. 8º): testes obrigatórios em aplicações críticas expostas à internet; antes da entrada em produção de sistemas relevantes; após mudanças significativas na arquitetura de segurança.
- **Proibições expressas** (art. 9º): DoS/DDoS e indisponibilidade de produção; exfiltração/alteração/destruição de dados reais (especialmente pessoais ou sigilosos); acesso a sistemas de terceiros fora do escopo; engenharia social sem alinhamento prévio com a Administração Superior.
- **Classificação da informação** (art. 11): relatórios, dados brutos e informações coletadas são **[RESTRITO]** ou **[SECRETO]**, armazenados/transmitidos por meios criptografados.
- **Contratação externa** (art. 12): exige NDA e comprovação de qualificação técnica.
- **Responsabilidades** (arts. 13-15): SECTI elabora plano anual e supervisiona; Gestores de Ativos aprovam o Termo e implementam correções; equipe de teste ater-se-á estritamente ao escopo autorizado.
- **Tratamento de vulnerabilidades** (art. 16): registro e tratamento conforme o processo de Gestão de Riscos e Vulnerabilidades.
- **Prazos de remediação** (art. 16, §§): por severidade (Crítica/Alta/Média/Baixa); prorrogação mediante justificativa do Gestor do Ativo com anuência do GSI; prazos acordados entre GSIPDP e Gestor do Ativo.
- **Reteste** (art. 17): após correções, a SECTI valida a eficácia da remediação.
- **Risco residual** (art. 18): se não corrigível, formalmente documentado e submetido ao **CGSIPDP** para aceitação formal.

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
