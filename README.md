# governanca-sipdp-tre-pr

Plugin Claude para acervo de **normas internas do TRE-PR e da Justiça Eleitoral** —
SI (Segurança da Informação), PDP (Proteção de Dados Pessoais), governança de IA,
continuidade de negócios e auditoria de urnas.

O vocabulário do domínio está em
[`skills/governanca-sipdp-tre-pr/CONTEXT.md`](./skills/governanca-sipdp-tre-pr/CONTEXT.md).
As decisões de desenho estão em [`docs/adr/`](./docs/adr/) (cópia dentro da skill em
`skills/governanca-sipdp-tre-pr/docs/adr/`).

## Escopo

O acervo é amplo — normas do TRE-PR de qualquer tema, inclusive sem relação com SI/PDP. O
recorte de SI/PDP é a camada de curadoria, não o acervo. Ver
[ADR 0001](./docs/adr/0001-escopo-amplo-com-camada-curada.md).

Critério de escopo canônico: `references/_meta/criterio-escopo.md`.

## O que tem dentro

- **PSI nacional** — Res. TSE 23.763/2026 (e a revogada 23.644/2021 como histórico)
- **PSI local** — Res. TRE-PR 974/2026
- **LGPD/PDP** — fundamentos, framework documental, fases 1–2, maturidade, IA & LGPD, PGPPDP
- **Pentest** — NT SECTI 006/2026 (Testes de Penetração)
- **Normas técnicas SECTI** — nuvem, projetos, segurança Linux, desenvolvimento, orçamento
- **Estrutura orgânica** — Res. 982/2026, Res. 971/2026, CGSI/PDP, CETI, CGTI, CGER, ETIR,
  SECTI, Comitê de Crises Cibernéticas
- **Continuidade** — PGCN e Protocolo Socioambiental
- **Auditoria de urnas** — CAVE (Res. 977/2026), Res. 893/2022, 934/2024
- **Prazos consolidados** e inventários de vigência (TRE-PR/TSE e CNJ)

## Estrutura

O plugin é autocontido: a skill e o acervo vivem em `skills/governanca-sipdp-tre-pr/`,
com **uma única cópia** de `references/` (a raiz do repo não duplica o acervo).

```
skills/governanca-sipdp-tre-pr/
├── SKILL.md                        entrada da skill
├── CONTEXT.md                      glossário do domínio
├── SCHEMA.md                       schema do vault
├── docs/adr/                       decisões de desenho (5 ADRs)
└── references/
    ├── index.md                    catálogo (todas as páginas)
    ├── normas/            185     página por norma
    ├── entities/           22     AGM, CGSI/PDP, ETIR, ASC, DPO, SECTI, ANPD, etc.
    ├── concepts/           22     LGPD, continuidade, prazos, governança, etc.
    ├── comparisons/         2      PSI-JE, controle de acesso
    ├── inventarios/         7      vigências TRE-PR/TSE, CNJ, lacunas, instrumentos
    ├── sources/             7      sínteses por tipo de norma
    ├── raw/               186     textos das normas (camada imutável, com sha256)
    └── _meta/               6      matriz de verificação, classificação, pendências, etc.
```

Links internos usam `[[references/...]]` (caminho a partir da raiz da skill); o sync
reescreve automaticamente os wikilinks `[[wiki/...]]` do vault nesse formato ao publicar.

## Estado de curadoria — leia antes de confiar

- **185 páginas de `references/normas/` estão curadas** — têm síntese, objeto/ementa,
  obrigações (artigos), status documentado e fonte em `raw/`.
- Todas as normas têm **status jurídico definitivo** (vigentes, revogadas, históricas ou não-aplicáveis).
- **186 raws** com sha256 para verificação de integridade.
- **Lacunas do inventário** mapeadas em `references/inventarios/lacunas-do-inventario.md`.
- **Classificação** em `references/_meta/classificacao-normas.md`.

## Convenção de caminhos

Todo link interno é caminho a partir da raiz do plugin
(`references/normas/psi-tse-23763-2026.md`), não wikilink de vault.

## Fontes

Normas publicadas nos portais do TRE-PR, TSE e CNJ. O monitoramento semanal verifica novas
publicações automaticamente (cron job).

## Versionamento

Este repositório segue versionamento semântico. O histórico de mudanças está no
[CHANGELOG](./CHANGELOG.md) (quando disponível) e no histórico de commits do GitHub.

## Licença

Veja [LICENSE](./LICENSE).
