---
title: Discovery — Checkout de demonstração
date: 2026-09-17
tags:
  - discovery
  - regras-de-negocio
status: exemplo-didatico
---

# Discovery — Checkout de demonstração

> [!info] Escopo
> Exemplo editorial em formato Obsidian. Usa [checkout.py](checkout-demo/checkout.py) e [política legada](checkout-demo/politica-legada.md), ambos fictícios e incluídos neste repositório. Não é uma saída medida da skill.

## Evidência observada

A função `frete_gratis` utiliza limite de 19.900 centavos para Sudeste e 29.900 para demais regiões. A comparação é estrita: subtotal igual ao limite não recebe frete grátis.

> [!warning] Divergência
> A política antiga descreve R$ 150,00 para Sudeste. O código utiliza R$ 199,00. Ainda é necessário definir qual regra deve prevalecer.

## Informação insuficiente

> [!question] Onde ocorre a validação de BEMVINDO?
> A política prevê expiração, mas as funções analisadas não recebem data de cadastro nem identificação do cupom. Essa validação pode estar fora do escopo.

## Próximos passos propostos

- Confirmar a política vigente com o responsável pelo produto.
- Localizar consumidores antes de concluir que uma validação está ausente do sistema.
- Documentar os limites e os critérios de aceite da alteração aprovada.

Veja o [caso completo](exemplo-regras-de-negocio.md) e o [protocolo de avaliação](../docs/avaliacao-de-respostas.md).
