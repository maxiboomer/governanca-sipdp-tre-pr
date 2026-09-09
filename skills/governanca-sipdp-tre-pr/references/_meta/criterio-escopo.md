---
title: "Critério de Escopo do Acervo SI/PDP"
created: 2026-09-09
updated: 2026-09-09
type: meta
status: vigente
curadoria: completa
escopo: contextual
tags: [escopo, classificacao, si-pdp, governanca, criterio, meta]
---

# Critério de Escopo do Acervo governanca-sipdp-tre-pr

**Este documento é a referência canônica de classificação de escopo.** O prompt do
monitoramento (cron) e qualquer curadoria devem aplicar ESTE critério, não decidir
por julgamento ad hoc. Serve para evitar erros de exclusão indevida (ex.: norma de
tecnologia eleitoral julgada "fora de escopo" quando o vault já curava normas
análogas de auditoria de urnas).

## Valores de escopo usados no vault

| Escopo | Significado | Exemplos |
|---|---|---|
| `central-si-pdp` | O objeto central da norma é Segurança da Informação, Proteção de Dados (LGPD), governança de IA, ou continuidade de negócios | PSI (Res. 974/2026), NT Pentest (006/2026), IN Gestão de Identidade/Acesso (004/2025), Res. ANPD incidentes |
| `apoio-governanca-ti` | Norma de governança/gestão de TI que dá suporte à SI (sem ser SI em si) | Comitês de governança de TI, planejamento |
| `contextual` | Norma relevante ao contexto institucional mas cujo objeto NÃO é primariamente SI/PDP — pode ter proteções transversais de SI/LGPD | Auditoria de urnas, regulamento da secretaria, sistema de votação operacional |
| `duplicada` | Duplicata mantida como alias | — |

## Critério de INCLUSÃO (o que entra no acervo)

**Entra no acervo** (com alguma página em `references/normas/`) toda norma que se
enquadre em UMA das seguintes categorias:

1. **Núcleo SI/PDP** — o objeto é segurança da informação, proteção de dados
   (LGPD), governança de IA, ou continuidade de negócios → `central-si-pdp`.
2. **Tecnologia/segurança eleitoral e de votação** — normas que regulam sistemas,
   procedimentos ou auditoria ligados ao processo de votação, apuração, urnas
   eletrônicas ou infraestrutura eleitoral → **`contextual`** (mesmo que o teor
   seja operacional, pois tocam integridade/disponibilidade do processo eleitoral,
   que a PSI considera centrais).
3. **Governança/gestão de TI** que dá suporte à SI → `apoio-governanca-ti` ou
   `contextual`.
4. **Norma que institui órgão/estrutura** de SI, PDP, crise cibernética ou IA
   (CGSIPDP, CGTI, CETI, CGER, ETIR, comitês) → `contextual` ou `central-si-pdp`
   conforme o objeto (criar page, ainda que administrativa, pois estabelece a
   instituição responsável).

## Critério de EXCLUSÃO (o que NÃO entra)

Fica **fora do acervo** apenas o que NÃO se enquadra em nenhuma categoria acima,
tipicamente:
- pessoal (lotação, designação de chefia, férias, teletrabalho);
- administrativo-geral sem teor de TI/SI (orçamento, patrimônio predial);
- eleitoral estrito sem componente de sistema/urna/segurança (calendário,
  prestação de contas partidária, propaganda) — **salvo** se regular infraestrutura
  de votação/apuração.

## Regras de decisão (anti-erro)

1. **Não exclua norma de tecnologia eleitoral** (urna, votação, apuração, sistema
   de acompanhamento do pleito) só por ser "operacional". Verifique primeiro se o
   vault já cura norma análoga. Se curou, trate de forma **consistente**.
2. **Proteções transversais contam.** Uma norma cujo objeto é operacional mas que
   contém artigos de controle de acesso (credenciais, perfis) ou tratamento de
   dados sob LGPD NÃO é automaticamente "fora de escopo" — entra como
   `contextual`.
3. **Consistência é obrigatória.** Antes de marcar algo como "fora de escopo",
   confira o acervo por tema análogo (`grep` no `references/normas/`). Se uma norma
   análoga está curada, a nova deve ser curada também (mesmo escopo), salvo
   justificativa registrada.
4. **Nunca registre "excluídas na rodada anterior" sem verificar** que realmente
   foram excluídas. A rodada de 2026-08-31 errou ao afirmar que "auditorias de
   votação foram excluídas" quando as Res. 893/2022 e 934/2024 estão curadas.
5. **Dúvida → cura como `contextual`** e registra a pendência de revisão humana,
   em vez de excluir. Exclusão só com confirmação explícita.

## Como aplicar (monitoramento/cron)

Ao detectar norma candidata nas listagens oficiais:
1. Ler a ementa E o texto (se acessível).
2. Classificar pela tabela acima.
3. Antes de decidir "fora de escopo", rodar busca de norma análoga no acervo.
4. Se entrar: criar raw + página curada com o escopo correto.
5. Se ficar fora: registrar no relatório COM a justificativa e a confirmação de
   que nenhuma norma análoga está curada.

## Referências

- Decisão de aplicação desta rodada: ADR 0005.
- Exemplos concretos de aplicação (IN AcompVot 001/2026): ver
  `references/normas/tre-pr-in-instrucao-normativa-001-de-24-de-agosto-de-2026-acompvot.md`.
