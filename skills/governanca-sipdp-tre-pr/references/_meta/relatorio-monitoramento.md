---
title: "Relatório de Monitoramento Normativo"
created: 2026-08-26
updated: 2026-09-09
type: metadata
status: não-aplicável
curadoria: completa
escopo: contextual
tags: [monitoramento, auditoria, vigencia]
---

# Relatório de Monitoramento Normativo

Relatório **report-only**: registra o que foi verificado nas fontes oficiais e o que
decorre disso. Nada aqui altera o vault automaticamente.

## Rodada 2026-08-26

### Fontes verificadas (via serviço de extração web, não urllib)

| Fonte | URL | Status |
|---|---|---|
| TRE-PR Resoluções 2025 | `.../resolucoes-tre-pr/2025` | Acessível |
| TRE-PR Resoluções 2026 | `.../resolucoes-tre-pr/2026` | Acessível |
| TRE-PR INs 2025 | `.../instrucoes-normativas-tre-pr/2025` | Acessível |
| TRE-PR Normas Técnicas SECTI 2026 | `.../normas-tecnicas-da-secti/2026` | Acessível |
| TSE / CNJ (detalhe) | `atos.cnj.jus.br`, `tse.jus.br` | Bloqueado a urllib; usar extração |

> **Nota de canal:** o acesso direto via `urllib`/curl é bloqueado com HTTP 403 pelos portais.
> O monitoramento operacional usa o serviço de extração web (que resolve como navegador). O
> script `monitor_normas.py` está mantido como referência de fontes, mas o acionamento real é
> sob demanda / via extração.

### Normas SI/PDP-relevantes publicadas e ausentes do vault (detectadas)

O diff das listagens oficiais de 2025/2026 contra o vault identificou **6 normas relevantes**
para segurança da informação / proteção de dados / governança de TI que ainda não estavam no
acervo:

| Norma | Assunto | Ação |
|---|---|---|
| Res. TRE-PR 970/2026 | Política de Gestão da Inovação | **Adicionada** ao vault |
| Res. TRE-PR 979/2026 | Captação/registro audiovisual em atos processuais (LGPD) | **Adicionada** ao vault |
| Res. TRE-PR 983/2026 | Altera Res. 852/2020 (mensagens instantâneas) | **Adicionada** ao vault |
| Res. TRE-PR 946/2025 | Política Antirretaliação | **Adicionada** ao vault |
| Res. TRE-PR 958/2025 | Utilização do PJe | **Adicionada** ao vault |
| NT SECTI 002/2026 | Metodologia de Desenvolvimento de Sistemas (MDS) | Adicionada; texto integral pendente |

### Revogações indiretas detectadas

- **Res. TRE-PR 979/2026 revoga a Res. TRE-PR 615/2012** (captação audiovisual anterior).
- **Res. TRE-PR 958/2025 revoga a Res. TRE-PR 774/2017** (PJe anterior).
- **Res. TRE-PR 970/2026 teve o art. 8º (atribuições do CGER) revogado pela Res. 980/2026.**

### Fora de escopo (não adicionadas)

As demais normas de 2025/2026 não presentes no vault são de tema administrativo/eleitoral sem
relação com SI/PDP/governança de TI (denominação de espaços, eleições suplementares, bandeira,
avaliação de estágio probatório, plebiscitos, comissões de auditoria da votação, planos de
obras, comunicação social). Ficam fora da camada de curadoria.

## Próximas rodadas

- Reconferir as listagens de 2026 (Resoluções/INs/NTs) periodicamente para novas publicações.
- Coletar o texto integral da NT SECTI 002/2026 (MDS).
- Reavaliar TSE/CNJ quando o acesso por extração permitir.

## Rodada 2026-08-29

### Fontes verificadas (via web_extract)

| Fonte | URL | Status |
|---|---|---|
| TRE-PR Resoluções 2026 | `.../resolucoes-tre-pr/2026` | Acessível (até Res. 987/2026) |
| TRE-PR Instruções Normativas 2026 | `.../instrucoes-normativas-tre-pr/2026` | Acessível (apenas IN 001/2026) |
| TRE-PR Normas Técnicas SECTI 2026 | `.../normas-tecnicas-da-secti/2026` | Acessível (NT 001–005) |
| TRE-PR Portarias DG 2026 | `.../portarias-da-diretoria-geral-tre-pr/2026` | Acessível (até Port. 434/2026) |
| TRE-PR Portarias Presidência 2026 | `.../portarias-da-presidencia-tre-pr/2026` | Acessível (até Port. 293/2026) |
| TSE Portarias/Resoluções 2026 | `tse.jus.br/legislacao` | Verificado por busca (23.763, 143, 463 já no acervo) |

### Novas normas SI/PDP detectadas e adicionadas

| Norma | Assunto | Ação |
|---|---|---|
| Portaria DG TRE-PR 124/2026 | Comitê Executivo de TI (CETI): composição e atribuições; revoga 425/2018 e 502/2022 | **Adicionada** (`não-confirmada`, `pendente`); raw preservado em `references/raw/` |

### Revogações confirmadas por fonte oficial

- Portaria DG 425/2018 e Portaria DG 502/2022 — já constavam como `revogada` no acervo; **confirmada a fonte revogadora: Portaria DG 124/2026, art. 4º** (DJE-TRE-PR nº 050, 19/03/2026, p. 11-12). Citação precisada na página de 502/2022.

### Fora de escopo (verificadas, não adicionadas)

- Res. TRE-PR 984–987/2026 (Plano de Obras, plebiscito, eleição suplementar) — administrativo/eleitoral.
- IN TRE-PR 001/2026 (Sistema AcompVot) — inicialmente marcada "fora do escopo"; **integrada em 2026-09-09 como `contextual`** (a premissa de que auditorias de votação haviam sido excluídas era falsa). Ver ADR 0005.
- TSE 334/2026 (acesso ao CT-TSE) e TSE 527/2026 (Sala Nacional de Situação Climática) — fora de escopo.
- Demais Portarias DG/Presidência 2026 (designações de chefia, teletrabalho, lotações) — pessoal, sem teor de SI/PDP.

### Pendências

- Curadoria da Portaria DG 124/2026 (confirmar vigência/classificação; texto integral já obtido do portal).
- Decisão de curadoria sobre IN 001/2026 (AcompVot) — item sinalizado para revisão humana.
- Coletar texto integral da NT SECTI 002/2026 (MDS) — pendência de rodadas anteriores.

## Rodada 2026-08-31

### Fontes verificadas (via web_extract)

| Fonte | URL | Status |
|---|---|---|
| TRE-PR Resoluções 2024 | `.../resolucoes-tre-pr/2024` | Acessível (até Res. 942/2024; Res. 940/2024 acessível via página individual) |
| TRE-PR Resoluções 2025/2026 | `.../resolucoes-tre-pr/2025` e `/2026` | Acessíveis |
| TRE-PR INs 2025 | `.../instrucoes-normativas-tre-pr/2025` | Acessível |
| TRE-PR NTs SECTI 2026 | `.../normas-tecnicas-da-secti/2026` | Acessível (NT 001–005) |
| TRE-PR Portarias DG 2026 | `.../portarias-da-diretoria-geral-tre-pr/2026` | Acessível (até Port. 434/2026) |
| TSE Res. 23.763/2026 (PSI) | `tse.jus.br/legislacao/compilada/res/2026` | Acessível (já no acervo) |

### Normas SI/PDP-relevantes detectadas e adicionadas (verificação manual sob demanda)

| Norma | Assunto | Ação |
|---|---|---|
| Res. TRE-PR 940/2024 | Código de Ética e Integridade da JE/PR (princípios, deveres, vedações, Comissão de Ética) | **Adicionada** ao vault (não-confirmada → revisada; vigente no portal) |
| IN TRE-PR 004/2025 | Gestão de Identidade e Controle de Acesso Lógico e Físico (55 artigos) | **Adicionada** ao vault (não-confirmada → revisada; vigente no portal) |

### Pendências fechadas nesta rodada

- **NT SECTI 002/2026 (MDS)** — texto integral coletado (DJE-TRE-PR nº 052, 23/03/2026, p. 08-09); página atualizada para `vigente`/`completa`. O Guia da MDS (anexo) permanece fora do acervo.
- **Portaria DG 124/2026 (CETI)** — curadoria concluída: `vigente`/`completa`, confirmada no compilado oficial + DJE-TRE-PR nº 050, 19/03/2026, p. 11-12.

### Decisão de escopo registrada

- **IN TRE-PR 001/2026 (Sistema AcompVot)** — decisão da rodada 2026-08-31 que a mantinha **fora do escopo** como "tecnologia eleitoral operacional, sem teor de SI/PDP" foi **REVISTA E CORRIGIDA em 2026-09-09**. A premissa era falsa: as resoluções de auditoria de funcionamento das urnas (Res. 893/2022 e 934/2024) **estão curadas** no acervo com `escopo: contextual`, e a IN contém proteções transversais de SI/LGPD (art. 3º controle de credenciais; art. 11 tratamento de dados). A IN foi **integrada ao acervo** com `escopo: contextual`. Ver ADR 0005 e `references/_meta/criterio-escopo.md`.

### Infraestrutura

- `sync_vault_to_build.py` corrigido para incluir `references/raw/` (raiz) e `references/raw/` na cópia vault→build — antes, textos integrais novos não chegavam ao `references/raw/` do repositório.

## Rodada 2026-09-03 (manutenção anti-drift)

### Ação: correção de drift de raws

| Item | Detalhe |
|---|---|
| Norma sem raw | Resolução TRE-PR 855/2020 — a página declarava `sources: [references/raw/lai-tre-pr-855-2020.md]` mas o arquivo não existia no vault nem no build |
| Ação corretiva | Raw baixado do portal (`Res08552020.html`, 43.265 chars, 48 artigos + 2 anexos), salvo em `references/raw/lai-tre-pr-855-2020.md` |
| Frontmatter | Atualizado: `sha256`, `source_url`, `confidence:medium` |
| Build sincronizado | `5cb53aa` (2 files changed, 622 insertions) |

### Variaredura de integridade (raws faltantes)

**10 normas** com `sources` apontando para raws que **não existem** no vault:

| Norma | Raw faltante | Status da norma |
|---|---|---|
| cnj-resolucao-363-2021 | raw/cnj-resolucao-363-2021.md | vigente |
| governanca-e-crises-tre-pr | raw/governanca-e-crises-tre-pr.md | vigente |
| ia-tre-pr-959-2025 | raw/ia-tre-pr-959-2025.md | vigente |
| lai-12527-2011 | raw/lai-12527-2011.md | vigente |
| portaria-tre-pr-302-2025 | raw/portaria-tre-pr-302-2025.md | vigente |
| psi-termos-portaria-tse-444-2021 | raw/psi-termos-portaria-tse-444-2021.md | vigente |
| psi-tre-pr-974-2026 | raw/psi-tre-pr-974-2026.md | vigente |
| psi-tse-23644-2021-revogada | raw/psi-tse-23644-2021-revogada.md | revogada |
| psi-tse-23763-2026 | raw/psi-tse-23763-2026.md | vigente |
| resolucao-tre-pr-962-2025 | raw/resolucao-tre-pr-962-2025.md | vigente |

**Cobertura**: 167 raws / 176 normas (94,9%). As 10 ausentes são **drift de rastreabilidade** — a norma aponta para fonte que não está no acervo.

### Estado do acervo
- 176 normas: 144 vigentes, 19 revogadas, 12 históricas, 1 não-aplicável
- 167 raws (94,9% de cobertura)
- 10 raws faltantes (pendência de curadoria)

## Rodada 2026-09-02 (evolução / curadoria)

### Normas promovidas a `vigente`/`completa`

| Norma | Publicação que sustenta | Ação |
|---|---|---|
| Res. TRE-PR 940/2024 (Código de Ética e Integridade) | DJE-TRE-PR nº 325, 07/11/2024, p. 11-24 | Promovida de `não-confirmada` → `vigente`/`completa` |
| IN TRE-PR 004/2025 (Gestão de Identidade e Controle de Acesso) | DJE-TRE-PR nº 102, 30/05/2025, p. 05-15 | Promovida de `não-confirmada` → `vigente`/`completa` |

### Decisões de processo registradas (ADR 0003)

- **Critério de confirmação**: página oficial individual com texto integral + referência DJE embutida
  sustenta `vigente` (caso 940/2024: ausente da listagem 2024, mas DJE rastreado no rodapé).
- **Auto-publicação pelo cron**: adição de norma nova com texto integral é publicada automaticamente
  (nasce `não-confirmada`); revogação/alteração de status/decisão de escopo exigem revisão humana e
  só são reportadas. Cron atualizado em 2026-09-02.
- Referências a skills externas inexistentes (`analise-normas-eleitorais`, `monitoramento-normas-secti`)
  removidas do SKILL.md — nenhuma outra skill do plugin cobre o acervo.

### Estado do acervo

- 176 páginas: 144 vigentes, 19 revogadas, 12 históricas, 1 não-aplicável; 0 não-confirmadas.
- Curadoria: 175 completas, 1 resumo (todas sem pendência de curadoria).

## Rodada 2026-09-09 (correção de escopo — IN AcompVot 001/2026)

### Contexto

O monitoramento semanal de 2026-09-09 reportou "sem mudanças", mantendo a IN TRE-PR
001/2026 (Sistema AcompVot) como fora de escopo. Revisão sob demanda identificou que a
decisão anterior (rodadas 08-29 e 08-31) se baseava em **premissa falsa**: afirmava que
"comissões de auditoria de votação foram excluídas na rodada anterior", mas as Res. TRE-PR
893/2022 e 934/2024 (auditoria de funcionamento das urnas) **estão curadas** no acervo com
`escopo: contextual`.

### Ação corretiva

| Item | Ação |
|---|---|
| **Critério de escopo** | Criado `references/_meta/criterio-escopo.md` — referência canônica de classificação; tecnologia eleitoral de votação/urna/apuração entra como `contextual`; verificar consistência com normas análogas antes de excluir |
| **IN 001/2026 (AcompVot)** | **Integrada ao acervo** com `escopo: contextual` — raw + página curada, vinculada às resoluções de auditoria de urnas |
| **ADR** | Criado `docs/adr/0005-criterio-escopo-tecnologia-eleitoral-contextual.md` |
| **Cron** | Prompt atualizado para carregar o critério de escopo e verificar normas análogas antes de excluir |
| **Histórico** | Rodadas 08-29/08-31 corrigidas; premissa falsa anotada |

### Pendências abertas (itens antes marcados "fora de escopo" — revisar em rodada dedicada)

- Res. TRE-PR 984–987/2026 (Plano de Obras, plebiscito, eleição suplementar)
- TSE 334/2026 (acesso ao CT-TSE) e TSE 527/2026 (Sala Nacional de Situação Climática)

### Estado do acervo (após correção)

- 188 normas: (atualizar após contagem) · 189 raws
- IN 001/2026 AcompVot adicionada como `contextual`
