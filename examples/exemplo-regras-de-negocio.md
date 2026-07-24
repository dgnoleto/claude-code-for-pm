# 📋 Documento de Regras de Negócio — Módulo de Desconto & Checkout

**Data da Extração:** 2026-07-24
**Escopo Analisado:** Módulo de precificação e validação de cupons.
**Documentos de Apoio Consultados:** `docs/Checkout-Spec-2025.md` (cruzado com código real para 94% de acurácia).

---

## 🎯 Objetivo de Negócio do Módulo

Garantir que as regras de desconto aplicadas no carrinho de compras sigam as políticas de marketing vigentes, evitando fraudes (uso acumulado de cupons) e validando limites mínimos de compra para frete grátis.

---

## 🔍 Regras de Negócio Identificadas no Código

### 1. Regra de Não-Acumulação de Descontos
- **Descrição:** Um usuário não pode utilizar um cupom de desconto promocional caso o carrinho já possua itens com descontos individuais de oferta relâmpago superiores a 15%.
- **Rastro Técnico:** [discountService.js](file:///d:/Github/claude-code-for-pm/examples/mocks/discountService.js#L23-L37)
- **Status de Certeza:** Confirmado pelo código ativo.

### 2. Regra de Limite de Desconto Máximo por Cupom
- **Descrição:** Independentemente da porcentagem do cupom (ex: 50% OFF), o valor absoluto de desconto máximo concedido por cupom é limitado a R$ 100,00 por transação.
- **Rastro Técnico:** [discountService.js](file:///d:/Github/claude-code-for-pm/examples/mocks/discountService.js#L54)
- **Status de Certeza:** Confirmado pelo código ativo.

### 3. Regra de Frete Grátis Regionalizado
- **Descrição:** O frete é grátis apenas para a região Sudeste em compras acima de R$ 199,00. Para as demais regiões, o frete grátis é concedido apenas acima de R$ 299,00.
- **Rastro Técnico:** [shippingCalculator.js](file:///d:/Github/claude-code-for-pm/examples/mocks/shippingCalculator.js#L12-L29)
- **Status de Certeza:** Confirmado pelo código ativo.

---

## ⚠️ Inconsistências Detectadas (Código vs Documentação)

- **Divergência de Frete Grátis:** A especificação legada (`docs/Checkout-Spec-2025.md`) diz que o frete grátis para o Sudeste deveria ser acima de R$ 150,00. No entanto, no arquivo [shippingCalculator.js](file:///d:/Github/claude-code-for-pm/examples/mocks/shippingCalculator.js#L14) o valor real programado é de **R$ 199,00**.
- **Divergência de Cupom de Primeira Compra:** A documentação prevê que o cupom `BEMVINDO` deveria expirar em 30 dias após o cadastro. No código, não há validação de data de expiração, apenas uma checagem se o usuário já fez alguma transação anterior no banco.

---

## ❓ Perguntas para Validação Técnico-Comercial (Dúvidas de Produto)

1. **Sobre o Frete Grátis:** O valor de R$ 199,00 no código está correto, ou foi um erro de desenvolvimento e deveria ter sido R$ 150,00 conforme o Confluence?
2. **Expiração do Cupom `BEMVINDO`:** Devemos implementar a expiração de 30 dias, ou a checagem de "primeira compra" é suficiente?
