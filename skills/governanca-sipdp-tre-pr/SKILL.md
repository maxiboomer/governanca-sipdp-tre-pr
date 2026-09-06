---
name: governanca-sipdp-tre-pr
description: Acervo de normas internas do TRE-PR e da Justiça Eleitoral (187 textos, 2016–2026) e regulamentações da ANPD, mantido pela AGM, com camada curada de Segurança da Informação, Proteção de Dados e continuidade. Use para responder qual norma rege um tema no TRE-PR, se ela está vigente ou foi revogada, com qual publicação isso se sustenta, e quem é a unidade competente — e para fundamentar despacho, parecer, minuta ou nota técnica com citação verificável. Ative ao mencionar PSI, LGPD no TRE-PR, CGSI/PDP, Encarregado/DPO, ETIR, ASC, AGM, SECTI, COSIG, Comitê de Crises Cibernéticas, PGCN, RIPD, RoPA, prazo normativo, vigência, revogação, inventário de normas, Res. TSE 23.763/2026, Res. TRE-PR 974/2026, 962/2025, 982/2026, 971/2026, 959/2025, 932/2024, Portaria DG 086/2026, Portaria 247/2021, Portaria 302/2025, IN-DG, Norma Técnica SECTI, Ordem de Serviço, ANPD, transferência internacional de dados, RTID, encarregado, comunicação de incidente, dosimetria de sanções, legítimo interesse — ou ao pedir "qual norma diz", "isso está revogado?", "quem é competente por", "qual o prazo de", "onde foi publicada".
---

# Acervo Normativo TRE-PR — SI/PDP

Acervo de normas internas do TRE-PR e da Justiça Eleitoral, com camada curada de Segurança
da Informação, Proteção de Dados Pessoais e continuidade de negócios. Unidade dona: a
**AGM** (`references/entities/agm.md`).

O vocabulário deste domínio está em `CONTEXT.md`. As decisões de desenho estão em
`docs/adr/`. **Leia o `CONTEXT.md` antes de usar os termos "norma", "situação",
"publicação", "curada" e "inventário"** — aqui eles têm sentido fixo.

**Conteúdo:** 187 páginas em `references/normas/` (todas curadas) + `entities`, `concepts`,
`comparisons`, `inventarios`, `sources`; textos integrais em `references/raw/` (com `sha256` para
detecção de drift). Páginas curadas carregam `confidence: high|medium|low` (high = DJE/DOU
nomeado; medium = compilado sem DJE; low = monitoramento sem confirmação).

## Exemplos de uso

### TRE-PR
- "Qual a penalidade para vazamento de dados no TRE-PR?" → ver [[normas/anpd-resolucao-15-2024-incidente-seguranca]] e [[normas/anpd-resolucao-04-2023-dosimetria-sancoes]]
- "Quem é o encarregado do TRE-PR?" → ver [[entities/encarregado-dpo]] e [[normas/anpd-resolucao-18-2024-encarregado]]
- "Qual o prazo para comunicar um incidente?" → ver [[normas/anpd-resolucao-15-2024-incidente-seguranca]] (art. 6º)
- "O que é o CETI?" → ver [[entities/ceti]] (comitê executivo, 12 atribuições, Portaria 124/2026)
- "O que é o CGTI?" → ver [[entities/cgti]] (comitê deliberativo, 16 integrantes, Portaria 296/2025)
- "O que é o CGER?" → ver [[entities/cger]] (estratégia + riscos, AGEP como presidente, Portaria 296/2025)
- "O que é o CGSIPDP?" → ver [[entities/cgsipdp]] (SI + LGPD, SECTI como presidente, Portaria 296/2025)
- "Posso usar legítimo interesse para marketing?" → ver [[normas/anpd-guia-legitimo-interesse-2024]]

### Distinção de comitês (evitar confusão)
- **CETI** (Comitê Executivo de TI) — órgão operacional, 12 atribuições, reuniões quinzenais
- **CGTI** (Comitê de Gestão da TI) — órgão deliberativo, 16 integrantes, define diretrizes de SI
- **CGER** (Comitê de Gestão Estratégica e Riscos) — 14 integrantes, AGEP como presidente
- **CGSIPDP** (Comitê Gestor de SI e PDP) — 17 integrantes, SI + LGPD

### ANPD
- "Posso transferir dados para a Europa?" → ver [[normas/anpd-resolucao-32-2026-adequacao-ue]] e [[normas/anpd-resolucao-19-2024-rtid]]
- "Qual a multa por descumprimento da LGPD?" → ver [[normas/anpd-resolucao-04-2023-dosimetria-sancoes]]
- "O que é legítimo interesse?" → ver [[normas/anpd-guia-legitimo-interesse-2024]]

## Escopo

O acervo é de **normas internas do TRE-PR e da JE**, de qualquer tema — inclui normas sem
relação com SI/PDP (teletrabalho, feriados, plantão). O recorte de SI/PDP é a **camada
curada**, não o acervo. Decisão registrada na ADR 0001.

## Convenção de caminhos

Todo link interno é caminho a partir da raiz da skill, no formato
`[[references/normas/psi-tse-23763-2026.md]]` (wikilink para arquivo sob
`references/`). **Não usar** `[[wiki/...]]` — esse é o formato do vault Obsidian e
**quebra no plugin** (o CI falha se aparecer). O `sync_vault_to_build.py` reescreve
automaticamente `[[wiki/...]]` → `[[references/...]]` ao publicar.

## Como consultar

1. Abra `references/index.md` — catálogo com links resolvíveis.
2. Vá à página do tema (`normas/`, `entities/`, `concepts/`, `inventarios/`).
3. **Todas as páginas de `normas/` estão curadas** — têm síntese, objeto/ementa, obrigações e
   status documentado. Responda pela síntese; para o teor exato, consulte o texto integral em
   `references/raw/`.
4. Nunca edite `references/raw/`. Correções vão nas páginas curadas.

## Regra de sustentação — a mais importante

**Nem este inventário nem a planilha da SECTI são autoridade sobre vigência.** A verdade é a
publicação oficial (ADR 0002). Ao afirmar que uma norma vale ou foi revogada, **diga sempre
com o que isso se sustenta**, nesta ordem:

1. **Citação de DJE/DOU** (veículo, número, data, página) — suficiente para citar em documento.
2. **Compilado oficial** do TRE-PR/TSE — serve para trabalhar; para documento, suba ao DJE.
3. **Nada** — a linha está como `Não confirmada`. **Diga que não foi possível confirmar.**
   Não presuma vigência, não presuma revogação.

Consulte `references/inventarios/normas-tre-pr-tse.md` e
`references/inventarios/lacunas-do-inventario.md` antes de afirmar situação.

## Outras regras de resposta

- **Cite norma, artigo e data.** Resposta sobre competência ou prazo sem dispositivo não serve.
- **Distinga norma de arranjo interno.** Onde a estrutura real do Tribunal não estiver
  refletida em norma vigente, diga — é ali que estão os riscos (ver a AGM).
- **Instrumento monitorado não é norma.** `Plano nº 371943/2023` e
  `Norma Técnica CDTI 02/2014` estão em
  `references/inventarios/instrumentos-monitorados.md` e nunca fundamentam nada.
- **Sinalize excertos.** Alguns arquivos de `raw/` não são texto integral (Res. 971/2026, por
  exemplo). Nesses casos, recomende conferir a fonte oficial.

## Mapa rápido

| Tema | Página |
|---|---|
| PSI nacional (TSE 23.763/2026) | `references/normas/psi-tse-23763-2026.md` |
| PSI local (Res. TRE-PR 974/2026) | `references/normas/psi-tre-pr-974-2026.md` |
| Comitê de crises cibernéticas (932/2024 e 962/2025) | `references/normas/governanca-e-crises-tre-pr.md` |
| Estrutura orgânica atual (Res. 982/2026) | `references/normas/tre-pr-resolucao-982-2026-reestruturacao.md` |
| Gestão da Inovação (Res. 970/2026) | `references/normas/tre-pr-resolucao-970-2026-gestao-inovacao.md` |
| Captação audiovisual / LGPD (Res. 979/2026) | `references/normas/tre-pr-resolucao-979-2026-captacao-audiovisual.md` |
| Mensagens instantâneas (Res. 983/2026, altera 852/2020) | `references/normas/tre-pr-resolucao-983-2026-altera-852-mensagens.md` |
| Política Antirretaliação (Res. 946/2025) | `references/normas/tre-pr-resolucao-946-2025-antirretaliacao.md` |
| PJe (Res. 958/2025) | `references/normas/tre-pr-resolucao-958-2025-pje.md` |
| AGM — governança e monitoramento de SI | `references/entities/agm.md` |
| CGSI/PDP (Port. DG 086/2026) | `references/entities/cgsipdp.md` |
| Código de Ética e Integridade (Res. 940/2024) | `references/normas/tre-pr-resolucao-940-2024.md` |
| Identidade e Controle de Acesso (IN 004/2025) | `references/normas/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md` |
| Encarregado/DPO (Port. 247/2021, na SEGEI) | `references/entities/encarregado-dpo.md` |
| ETIR | `references/entities/etir.md` |
| ASC — Segurança Cibernética (COSIG/SECTI) | `references/entities/asc.md` |
| SECTI | `references/entities/secti.md` |
| Continuidade / PGCN (Port. 302/2025) | `references/concepts/continuidade-negocios-tre-pr.md` |
| IA / LGPD | `references/concepts/lgpd-ia-governanca.md` |
| Prazos consolidados | `references/concepts/prazos-normativos-tre-pr.md` |
| Inventário TRE-PR/TSE | `references/inventarios/normas-tre-pr-tse.md` |
| Inventário CNJ | `references/inventarios/normas-cnj.md` |
| Lacunas do inventário | `references/inventarios/lacunas-do-inventario.md` |
| Instrumentos monitorados | `references/inventarios/instrumentos-monitorados.md` |

## Fronteira com outras skills

Esta skill é **acervo e sustentação**: o que a norma diz, se vale, com que publicação, quem
é competente. Ela **não** produz documento nem executa metodologia.

| Pedido | Skill adequada |
|---|---|
| Redigir plano de continuidade (PE, PGC, PCO, PRD, PCOM, PRN, PSBP, PCSA), ISO 22301 | `bcm-specialist` |
| Estruturar programa de compliance LGPD, gap analysis, maturidade, RIPD, ANPD | `lgpd-compliance-setor-publico` |
| Gerar documentos de implementação da Res. CNJ 363/2021 | `cnj-363-2021` |
| Padronizar minuta segundo LC 95/1998 (legística) | `padronizacao-atos-normativos` |
| Rotina de cartório eleitoral, CAE, Corregedoria | `codigo-normas-cre-pr` |
| Classificação e temporalidade documental | `pcd-ttd-trepr` |
| Lavrar ata de reunião no padrão TRE-PR | `ata-tre-pr` |

**Sobreposição conhecida** — nesses temas, confirme aqui antes de fechar:

- Nenhuma outra skill deste plugin cobre o mesmo acervo. Referências antigas a
  `analise-normas-eleitorais` e `monitoramento-normas-secti` foram removidas: essas skills não
  fazem parte deste plugin e não devem ser assumidas como instaladas. Se uma skill externa com
  nome semelhante existir no ambiente, o acervo desta (vault + `references/`) continua sendo a
  fonte de verdade a conferir antes de fechar resposta.

## Avisos

- Normas revogadas permanecem como histórico, sinalizadas.
- Todas as 187 páginas de `normas/` estão curadas; o teor exato está em `references/raw/`.
- Os Anexos I e II da Res. 982/2026 (cargos e organograma) não constam do acervo.
- O Guia da MDS (anexo da NT SECTI 002/2026) não consta do acervo; o ato normativo (DJE-TRE-PR nº 052, 23/03/2026, p. 08-09) está em `references/raw/`.
