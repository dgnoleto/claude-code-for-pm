# Notas de refinamento — `feature-impact-analysis`

Conjunto de testes de gatilho seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic): 8 frases que devem acionar a skill e 8 que não devem, incluindo quase-acertos propositalmente difíceis.

## Quase-acertos mais importantes

- **"se eu mudar a regra de desconto de 10% para 15%, o que é afetado no código?"** — usa a palavra "regra", o que poderia sugerir `business-rules-extractor`. A diferença é o verbo "mudar" e o foco no impacto de uma alteração futura — isso é `feature-impact-analysis`. Já "quais as regras de desconto atuais?" é `business-rules-extractor` (estado atual, não mudança futura).

- **"me explica como funciona a regra de frete atual"** — parece impacto de feature, mas é extração de regra existente sem intenção de mudança. Deve acionar `business-rules-extractor`, não esta skill.

- **"revisa essa PRD por questões de segurança"** — PRD como input pode parecer `feature-impact-analysis`, mas o foco é segurança, não impacto arquitetural. Deve acionar `security-blind-spot-reviewer`.

- **"questiona essa spec como um arquiteto sênior"** — arquiteto como persona pode parecer ligado a análise de impacto arquitetural, mas o pedido é de questionamento da spec, não de mapeamento de impacto no código. Deve acionar `spec-challenger`.

## Ajuste aplicado na description

O sinal mais confiável desta skill é a combinação de dois elementos: (1) há uma feature ou mudança futura sendo proposta, e (2) o pedido é de mapeamento de impacto no código existente. Qualquer um dos dois isolado não é suficiente para acionar esta skill. Esse critério foi reforçado internamente na construção dos exemplos negativos.
