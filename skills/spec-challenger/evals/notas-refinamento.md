# Notas de refinamento — `spec-challenger`

Conjunto de testes de gatilho seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic): 8 frases que devem acionar a skill e 8 que não devem, incluindo quase-acertos propositalmente difíceis.

## Quase-acertos mais importantes

- **"valida essa spec e me diz se está boa para lançar"** — o verbo "valida" com intenção positiva ("está boa?") é a diferença crítica. Esta skill questiona e encontra problemas — não valida positivamente nem aprova. "Valida se está boa" é aprovação implícita; "me faz as perguntas difíceis" é questionamento. O primeiro NÃO deve acionar a skill; o segundo deve.

- **"revisa essa spec com olhar técnico crítico e me diz o que está fraco"** — não usa palavras como "questiona", "estresa" ou "sênior", mas o foco em "olhar crítico" e "o que está fraco" é exatamente o propósito da skill. Deve acionar mesmo sem o vocabulário-chave.

- **"questiona esse módulo de código como um arquiteto"** — o objeto é código, não uma spec ou PRD. Esta skill questiona *especificações antes da implementação*, não código já escrito. Código existente é território de `tech-debt-evaluator` ou `code-discovery`. Não deve acionar.

- **"revisa essa PRD por questões de segurança"** — PRD como input com revisão técnica pode parecer `spec-challenger`, mas o foco em segurança é específico o suficiente para acionar `security-blind-spot-reviewer`. A diferença: `spec-challenger` faz perguntas amplas sobre pontas soltas; `security-blind-spot-reviewer` usa um checklist estruturado de vetores OWASP.

- **"o que mudaria no código se eu implementar essa spec?"** — spec como input, olhar técnico — mas o pedido é de mapeamento de impacto no código existente, não de questionamento da spec em si. Deve acionar `feature-impact-analysis`.

## Ajuste aplicado na description

Dois pontos reforçados:

1. O objeto desta skill é sempre uma *especificação futura* (spec, PRD, história de usuário, rascunho de requisito) — nunca código já existente. Esse limite separa esta skill de `tech-debt-evaluator` e `code-discovery`.

2. O tom do pedido precisa indicar *questionamento ou identificação de problemas* — não aprovação, validação positiva ou implementação. "Me diz se está boa" é aprovação. "Me faz as perguntas difíceis" é questionamento. A description original cobre isso, mas o quase-acerto do "valida" mostrou que a cláusula negativa pode ser reforçada com um exemplo mais explícito.
