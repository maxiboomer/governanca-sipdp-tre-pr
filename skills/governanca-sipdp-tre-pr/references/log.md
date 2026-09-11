
## [2026-09-11] ingest | ANPD — Anonimização e Pseudonimização (2 estudos técnicos + estudo preliminar do Guia)
- **raws criados** (3 novos em `references/raw/anpd-estudo-*`):
  - `anpd-estudo-tecnico-anonimizacao-analise-juridica-2023.md`: Estudo Técnico — Análise Jurídica (nov/2023, 50.284 chars)
  - `anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-computacionais-2023.md`: Estudo Técnico — Processo Baseado em Risco e Técnicas Computacionais (nov/2023, 40.885 chars)
  - `anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023.md`: Estudo Preliminar — minuta do Guia de Anonimização e Pseudonimização (dez/2023, consulta jan-fev/2024)
- **Páginas curadas criadas** (3 em `references/normas/`):
  - `anpd-estudo-tecnico-anonimizacao-analise-juridica-2023.md`
  - `anpd-estudo-tecnico-anonimizacao-processo-risco-tecnicas-2023.md`
  - `anpd-estudo-preliminar-anonimizacao-pseudonimizacao-2023.md`
- **Síntese temática criada**: `references/concepts/anonimizacao-pseudonimizacao-lgpd.md` — visão consolidada das definições, diferenças, processo de 12 etapas, técnicas e cenários
- **Inventário atualizado**: `references/inventarios/regulamentacoes-anpd.md` — seção "Estudos Técnicos e Estudos Preliminares" criada
- **conceito `lgpd-recursos-oficiais-anpd`** atualizado com os estudos
- **index.md**: 1 novo concept, 3 novas normas; estatísticas atualizadas (191 raws → 194 raws, 190 normas → 193 normas, 14 concepts → 15 concepts)

## [2026-09-09] ingest | Correção de escopo + integração IN TRE-PR 001/2026 (AcompVot)
- **Correção de escopo**: a IN 001/2026 (Sistema AcompVot) fora inicialmente mantida "fora do escopo" pelo monitoramento sob premissa FALSA (auditorias de votação "excluídas" — mas Res. 893/2022 e 934/2024 estão curadas como `contextual`). Corrigido e integrado.
- **Critério de escopo** criado: `references/_meta/criterio-escopo.md` — referência canônica; tecnologia eleitoral de votação/urna entra como `contextual`; verificar norma análoga antes de excluir.
- **IN 001/2026 AcompVot**: raw (texto integral, sha256) + página curada `contextual` vinculada a 893/2022 e 934/2024.
- **ADR 0005** criado (criterio-escopo-tecnologia-eleitoral-contextual).
- **Prompt do cron** atualizado para carregar o critério de escopo.
- Relatório de monitoramento corrigido (premissa falsa anotada).

## [2026-09-04] audit | Auditoria completa do vault
- Relatório: wiki/_meta/relatorio-auditoria-20260904.md
- Resultado: 230 páginas curadas, 188 raws, cobertura 100%, 0 duplicatas, 0 drift de conteúdo
- 187 normas: 155 vigentes, 19 revogadas, 12 históricas, 1 não-aplicável
- Build drift: 0 (só link rewriting esperado)
- Hash drift: 0/11 raws ANPD verificados

## [2026-09-04] ingest | Regulamentações ANPD — scraping + curadoria completa
- **Scraping** da página oficial de Regulamentações da ANPD (gov.br) — 17 atos identificados (13 Resoluções, 3 Portarias, 1 Enunciado)
- **Raws criados** (11 novos em `references/raw/anpd-*.md`):
  - Res. 01/2021 (Fiscalização e Sancionador), Res. 02/2022 (Pequeno Porte), Res. 04/2023 (Dosimetria), Res. 15/2024 (Incidente), Res. 18/2024 (Encarregado), Res. 19/2024 (RTID), Res. 23/2024 (Agenda Regulatória), Res. 32/2026 (Adequação UE), Enunciado 1/2023 (Crianças)
- **Páginas curadas criadas** (9 em `references/normas/`): as 8 substantivas + agenda regulatória
- **Inventário criado**: `references/inventarios/regulamentacoes-anpd.md` — lista os 17 atos com status, ementa e link para página
- **Correção crítica**: `concepts/lgpd-recursos-oficiais-anpd.md` listava resoluções **falsas** (Res. 01/2021 "Procedimentos para notificações", 02/2021 "Diretrizes para RIPD" etc.) — substituídas pelas regulamentações reais
- **entity anpd.md** atualizada com links para as 8 normas substantivas
- index.md: 9 normas + inventário adicionados; estatísticas (188 raws, 186 normas, 5 inventários)

## [2026-09-04] update | Reconstrução dos raws ANPD (qualidade de tabelas)
- Reconstruídos os 2 raws ANPD com extração limpa e tabelas markdown reais:
  - `references/raw/anpd-guia-legitimo-interesse-2024.md`: Quadro 01, Anexo I (Síntese) e Anexo II (Modelo de teste) agora são tabelas/formulário markdown; hifenização e rodapés removidos
  - `references/raw/anpd-guia-tratamento-dados-poder-publico-2023.md`: Anexo I (Uso compartilhado) e Anexo II (Divulgação) agora são tabelas markdown; hifenização e rodapés removidos
- sha256 recalculados após reconstrução
- Correção: raw de tratamento-dados havia perdido o corpo (13 linhas, só frontmatter) por sobrescrita do write_file — reconstruído com conteúdo completo (210 linhas)
- Lint: 222 páginas, 0 problemas

## [2026-09-04] ingest | ANPD — 2 Guias Orientativos (LGPD)
- **raw/anpd-guia-legitimo-interesse-2024.md**: Guia ANPD sobre legítimo interesse (fev/2024, 1.486 linhas, 80.440 chars)
- **raw/anpd-guia-tratamento-dados-poder-publico-2023.md**: Guia ANPD sobre tratamento pelo Poder Público (jun/2023, 1.457 linhas, 82.879 chars)
- **normas/anpd-guia-legitimo-interesse-2024.md**: Página curada (escopo: central-si-pdp, confidence: high)
- **normas/anpd-guia-tratamento-dados-poder-publico-2023.md**: Página curada (escopo: central-si-pdp, confidence: high)
- **index.md**: Adicionadas 2 normas + estatísticas atualizadas (179 raws, 178 normas)
- **log.md**: Registro de ingest

## [2026-09-02] update | Correção de defeitos da auditoria (links + duplicação + caminhos)
- **Defeito 1 — links quebrados no build**: ~464 ocorrências de wikilinks no formato do
  Obsidian (`references/...`, sem prefixo `references/`) em 51 arquivos do build — formato que não
  resolve no plugin. `sync_vault_to_build.py` agora reescreve esses wikilinks para o formato
  `references/...` (e caminhos `references/raw/...` → `references/raw/...`, `sources: [references/raw/` →
  `sources: [references/raw/`) na cópia do build; o vault preserva o formato do Obsidian.
  O CI passou a **falhar** se um wikilink `references/...` aparecer no build.
- **Defeito 2 — duplicação do acervo**: removida `references/` da raiz do repo; a skill é
  autocontida com **uma única cópia** em `skills/governanca-sipdp-tre-pr/references/` (a que o
  Claude lê). `references/raw/` sincronizado na cópia da skill (166 arquivos; antes 158 e desatualizado).
  ADRs completos dentro da skill (4); órfãos removidos (`references/SCHEMA.md` duplicado,
  `SCHEMA-vault.md`, `cave.md`, `teste-integridade-2026.md`). CONTEXT/CLAUDE/SCHEMA removidos
  da raiz do repo (vivem dentro da skill).
- **Defeito 3 — pendencias-curadoria.md**: caminho `references/_meta/classificacao-normas.md`
  reescrito para `references/_meta/classificacao-normas.md` no build.
- Descrições do plugin corrigidas (174 → 176 normas); SKILL.md frontmatter atualizado;
  README estrutura corrigida. Publicado como v1.5.2.

## [2026-09-02] update | Blindagem do acervo: CI + lint + instrumentos monitorados
- **Defeito corrigido**: `references/inventarios/instrumentos-monitorados.md` era referenciado
  pelo SKILL.md mas não existia. Criado `references/inventarios/instrumentos-monitorados.md`
  (Plano 371943/2023, NT CDTI 02/2014; regra: instrumento monitorado não fundamenta parecer).
- **CI/CD**: criado `.github/workflows/ci.yml` — valida em todo push/PR ao master:
  versão plugin.json==marketplace.json, frontmatter completo em references/*, index.md lista
  todas as normas, sem broken wikilinks. Rede de segurança para o cron auto-publicar.
- **Remote git** atualizado para `governanca-sipdp-tre-parana` (endereço canônico; silencia
  warning de redirect em todo push).
- **Lint aprofundado**: `lint_vault.py` agora sinaliza `review_candidates` (páginas com
  `confidence: low` ou `contested: true`) para revisão humana — fecha o ciclo da v1.5.0.
- **Nova comparison**: `references/comparisons/controle-acesso-in004-2025-vs-2022-vs-2018.md`
  (IN 004/2025 atual × IN 004/2022 geral × IN-DG 2018 revogadas; cadeia de revogação).

## [2026-09-02] update | Higiene llm-wiki + confidence + sha256 + comparisons
- **Lint zerado** (era: 1 broken link, 2 fora do index, 8 field_issues):
  - Criado `references/concepts/governanca-ti.md` (corrige broken link da página 124/2026).
  - Movido `references/raw/tre-pr-portaria-dg-124-2026.md` → `references/raw/` com frontmatter (corrige 8 field_issues; raw agora em local canônico).
  - Adicionadas ao index: página 124/2026 (estava ausente), concept governanca-ti, seção Comparisons.
- **confidence** adicionado às 20 páginas `central-si-pdp` (12 high com DJE/DOU nomeado, 8 medium).
- **sha256** adicionado aos 166 raws (detecção de drift em re-coleta); `source_url` derivado onde faltava.
- **Camada `references/comparisons/`** criada: `psi-je-23644-23763-974.md` (comparação PSI antiga × nacional × local).
- **SCHEMA.md**: camada comparisons, campos `confidence`/`contested`, exigência de `sha256` nos raws.
- **ADR 0004**: revogadas/históricas permanecem em `references/normas/` (decisão consciente vs `_archive/` do llm-wiki).
- **Páginas >200 linhas** (6) registradas como dívida técnica — dividir quando passarem de ~500 linhas.
- sync_vault_to_build.py: inclui `references/comparisons`.

## [2026-09-02] update | Curadoria concluída + ADR 0003 + cron auto-publicação
- Res. TRE-PR 940/2024 e IN TRE-PR 004/2025 promovidas a `vigente`/`completa` (DJE-TRE-PR nº 325, 07/11/2024, p. 11-24 e nº 102, 30/05/2025, p. 05-15). Acervo sem páginas não-confirmadas.
- ADR 0003 (docs/adr/0003): critério de confirmação de vigência (página oficial individual + DJE embutido) e auto-publicação de novas normas pelo cron (revogações/escopo só reportam).
- Cron semanal atualizado com as regras do ADR 0003.
- SKILL.md: removidas referências a skills externas inexistentes (`analise-normas-eleitorais`, `monitoramento-normas-secti`).

## [2026-08-31] update | Fechamento de pendências + evolução da skill
- **NT SECTI 002/2026 (MDS)**: texto integral coletado (DJE-TRE-PR nº 052, 23/03/2026, p. 08-09) em `references/raw/tre-pr-nt-secti-002-2026-mds.md`; página promovida a `vigente`/`completa`.
- **Portaria DG 124/2026 (CETI)**: curadoria concluída (`vigente`/`completa`), confirmada no compilado oficial + DJE-TRE-PR nº 050, 19/03/2026, p. 11-12.
- **IN TRE-PR 001/2026 (AcompVot)**: decisão de escopo registrada — mantida FORA do acervo (tecnologia eleitoral operacional, sem teor SI/PDP); pendência de revisão humana encerrada.
- `sync_vault_to_build.py` corrigido para incluir `references/raw/` e `references/raw/` (antes, textos integrais novos não chegavam ao `references/raw/` do repo).
- SKILL.md atualizado: 174→176 páginas; mapa rápido ganhou Res. 940/2024 e IN 004/2025; aviso da NT 002/2026 atualizado.
- index.md: estatísticas corrigidas (176 normas, 8 entities, 13 concepts, 3 inventários, 166 raws).

## [2026-08-31] update | Inclusão de normas ausentes detectadas em verificação manual
- Identificada a **Resolução TRE-PR 940/2024** (Código de Ética e Integridade) — vigente no portal, mas sem página curada no vault (apenas citada como `CONSIDERANDO` na IN 004/2025).
- Identificada a **Instrução Normativa TRE-PR 004/2025** (Gestão de Identidade e Controle de Acesso Lógico/Físico) — vigente no portal, mas sem página curada no vault (apenas em `references/raw/`).
- Criadas as páginas curadas:
  - `references/normas/tre-pr-resolucao-940-2024.md` (status: `não-confirmada`, curadoria: `pendente`)
  - `references/normas/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md` (status: `não-confirmada`, curadoria: `pendente`)
- Salvo o texto integral da Res. 940/2024 em `references/raw/tre-pr-resolucao-940-2024.md`.
- Atualizados `index.md` (seção "Normas (novas)") e `log.md`.
- Observação: a Res. 940/2024 não aparece na listagem compilada de 2024 do portal (que mostra apenas até 942/2024), embora a página individual funcione — possível desordem de indexação ou retificação não-refletida na sumarificação. Norma confirmada vigente via acesso direto à página.

## [2026-08-26] update | Reconciliação e correção do fluxo de curadoria
- Identificado que a curadoria desta sessão havia sido gravada apenas no build (references/), não no vault (fonte da verdade).
- Portadas 159 páginas curadas do build de volta ao vault; raw/ preservado. Vault e build agora sincronizados (0 divergências).
- Corrigidos 96 wikilinks com prefixo `references/` incorreto (quebravam o vault).
- lint_vault.py corrigido: `curadoria` agora vem do frontmatter (fonte única), não de heurística de texto; adicionado check de prefixo `references/`.
- Vault: 206 páginas, 0 stubs, 0 links quebrados, 0 campos ausentes, 0 prefixo errado.

## [2026-08-26] update | Monitoramento normativo — 1ª rodada
- Identificadas e adicionadas ao vault 6 normas SI/PDP-relevantes publicadas em 2025/2026 que estavam ausentes: Res. TRE-PR 970/2026 (inovação), 979/2026 (captação audiovisual/LGPD), 983/2026 (altera 852/2020), 946/2025 (antirretaliação), 958/2025 (PJe) e NT SECTI 002/2026 (MDS, texto pendente).
- Revogações indiretas detectadas: 979/2026 revoga 615/2012; 958/2025 revoga 774/2017; art. 8º da 970/2026 revogado pela 980/2026.
- Criado wiki/_meta/relatorio-monitoramento.md (report-only) e atualizado monitor_normas.py (canal web, não urllib).
- lint_vault.py: index.md e log.md excluídos do check de campos obrigatórios (arquivos administrativos).
