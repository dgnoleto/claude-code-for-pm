---
title: Discovery — Repositório Legacy Payment
date: 2026-07-24
tags:
  - discovery
  - mapeamento
  - relatorio-final
status: concluido
---

# Discovery — Repositório Legacy Payment

**Escopo investigado:** Repositório completo.
**Documentos de Apoio Consultados:** [[2024-03-15-PRD-Checkout-v1]] (precisão cruzada estimada em 96%).

---

## 🎯 Objetivo do Sistema

O repositório `legacy-payment-service` é uma API em Node.js responsável por orquestrar transações financeiras (cartão de crédito, boleto e Pix) e sincronizar o status com o serviço de faturamento legado.

---

## 🟢 Achados Confirmados

### 1. Duas integrações ativas com Stripe
- **Onde está:** [stripeRouter.js](file:///d:/Github/claude-code-for-pm/examples/mocks/stripeRouter.js#L12) e [stripeService.js](file:///d:/Github/claude-code-for-pm/examples/mocks/stripeService.js#L45)
- **Evidência:** Arquivo de rotas e serviço instanciando a biblioteca oficial `@stripe/stripe-node` versão 12.0.
- **Observação:** O sistema faz chamadas de webhook para processar cobranças recorrentes.

---

## 🟡 Achados Prováveis

### 1. Lógica redundante de cálculo de juros
- **Onde está:** [financeUtils.js](file:///d:/Github/claude-code-for-pm/examples/mocks/financeUtils.js#L34-L52)
- **Evidência:** Há duas funções (`calculateSimpleInterest` e `applyStandardInterest`) que realizam essencialmente a mesma multiplicação de taxa, mas uma delas não é chamada no fluxo principal, apenas no arquivo de teste legados.

---

## ❓ Hipóteses (A Validar)

> [!question] Hipótese: Gateway da Pagar.me desativado?
> Encontramos chaves de configuração e rotas para a Pagar.me em `config/pagarme.js`, mas nenhuma transação ativa ou chamada de produção utiliza este arquivo desde o commit `8c3f2d` de Dezembro de 2024. É provável que seja código morto.

---

## ⚠️ Fora do Escopo

> [!warning] Integração com API de Notas Fiscais (e-notas)
> Identificamos que o serviço se comunica com a e-notas para emissão de NF. Como o escopo foi fechado apenas em pagamentos, não aprofundamos nos webhooks de falha de nota fiscal. Recomenda-se um discovery focado nisso na próxima rodada.

---

## 📋 Perguntas para Validar com Engenharia

- [ ] A integração Pagar.me realmente pode ser limpa do código ou ainda há algum cliente antigo rodando nela?
- [ ] O arquivo `financeUtils.js` linha 34 pode ser unificado para evitar bugs de arredondamento?

---

## 💡 Recomendações de Produto

> [!important] ROI da Limpeza Técnica
> A unificação do cálculo de juros evita reclamações de clientes no suporte sobre divergência de centavos no boleto. A remoção do código morto da Pagar.me reduz a complexidade para o onboarding de novos desenvolvedores no projeto.
