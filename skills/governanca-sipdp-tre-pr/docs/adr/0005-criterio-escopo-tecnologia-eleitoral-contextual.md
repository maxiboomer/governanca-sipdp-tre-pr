---
status: accepted
date: 2026-09-09
---

# Critério de escopo explícito; tecnologia eleitoral (urna/votação) é contextual, não excluída

O monitoramento de 2026-08-31 manteve a IN TRE-PR 001/2026 (Sistema AcompVot, que regula
o acompanhamento operacional/logístico da votação nas Eleições 2026) como "fora de escopo
SI/PDP estrito", sob a premissa de ser "análoga às comissões de auditoria de votação,
excluídas na rodada anterior". A premissa era **falsa**: as resoluções de auditoria de
funcionamento das urnas (Res. TRE-PR 893/2022 e 934/2024) **estão curadas** no acervo com
`escopo: contextual`. O julgamento de exclusão foi feito sem um critério explícito e sem
verificar a consistência com normas análogas já presentes.

## Considered Options

- **Criar um critério de escopo explícito e auditável** (documentado em
  `wiki/_meta/criterio-escopo.md`), que o prompt do cron carregue, e curar a IN 001/2026
  como `contextual`, consistente com as auditorias de urnas. Escolhido.
- Corrigir só a IN 001/2026 sem criar critério. Rejeitado: não evita a recorrência.
- Manter como estava. Rejeitado: inconsistência factual com o acervo.

## Decision

1. **Criar `wiki/_meta/criterio-escopo.md`** como referência canônica de classificação.
2. **Tecnologia eleitoral de votação/apuração/urna** (incluindo sistema de acompanhamento
   do pleito como o AcompVot) entra no acervo como **`contextual`**, não é excluída por
   ser "operacional".
3. **Proteções transversais contam**: norma com artigos de controle de acesso (credenciais)
   ou tratamento de dados sob LGPD não é automaticamente fora de escopo.
4. **Antes de excluir**, verificar se há norma análoga curada (grep no `wiki/normas/`).
   Consistência é obrigatória.
5. **Dúvida → curar como `contextual`** e registrar pendência de revisão humana, em vez
   de excluir.

## Consequences

- A IN 001/2026 (AcompVot) é integrada ao acervo com `escopo: contextual`, vinculada às
  resoluções de auditoria de urnas.
- O monitoramento (cron) deve carregar o critério de escopo e aplicá-lo antes de excluir
  qualquer candidata.
- Itens outrora marcados "fora de escopo" podem precisar revisão à luz do critério novo;
  fica registrado como pendência (TSE 334/2026, TSE 527/2026, Res. 984-987/2026) — decidir
  em rodada dedicada.
- Consistente com o ADR 0001 (acervo amplo de normas do TRE-PR; SI/PDP é a camada de
  curadoria, não uma poda do acervo).
