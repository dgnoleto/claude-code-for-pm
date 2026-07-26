# Notas de refinamento — `business-rules-extractor`

Conjunto de testes de gatilho seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic): 8 frases que devem acionar a skill e 8 que não devem, incluindo quase-acertos propositalmente difíceis.

## Quase-acertos mais importantes

- **"ninguém sabe o que esse módulo de cobrança faz, pode investigar?"** — soa como extração de regras de negócio, mas o verbo "investigar" e o contexto de "ninguém sabe o que faz" apontam para `code-discovery`. A diferença: `business-rules-extractor` pressupõe que o módulo é conhecido e a pergunta é sobre *o que ele faz internamente*. `code-discovery` é acionada quando o próprio propósito é desconhecido.

- **"como funciona o fluxo de autenticação do sistema?"** — parece pedido de regra de negócio, mas autenticação é um fluxo de arquitetura mais do que uma regra de produto. Tende a acionar `code-discovery` ou `tech-debt-evaluator` dependendo do contexto. Não deve acionar `business-rules-extractor` a menos que a pergunta seja sobre uma regra específica dentro do fluxo (ex: "quando um usuário é bloqueado após falhas de login?").

- **"faz uma análise de impacto se eu mudar a regra de frete"** — usa a palavra "regra", mas o pedido é de impacto de uma *mudança futura*, não de extração do comportamento *atual*. Deve acionar `feature-impact-analysis`.

## Ajuste aplicado na description

A description original estava precisa, mas foi reforçado um ponto na cláusula negativa: a skill serve para documentar o comportamento *atual* do código em linguagem de produto — não para projetar o impacto de mudanças futuras e não para investigar módulos cujo propósito é completamente desconhecido. Esses dois casos têm skills próprias.
