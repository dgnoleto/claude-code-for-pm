# Notas de refinamento — `tech-debt-evaluator`

Conjunto de testes de gatilho seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic): 8 frases que devem acionar a skill e 8 que não devem, incluindo quase-acertos propositalmente difíceis.

## Quase-acertos mais importantes

- **"tem alguma brecha de segurança nesse código?"** — qualidade de código e segurança são temas próximos, mas o vetor de preocupação é diferente. Débito técnico é sobre manutenibilidade, custo futuro e risco operacional. Segurança é sobre vetores de ataque e vulnerabilidades exploráveis. Deve acionar `security-blind-spot-reviewer`.

- **"tem alguma parte do código que pode travar em produção com aumento de carga?"** — é o quase-acerto mais difícil deste conjunto. Gargalo de performance *pode* ser sintoma de débito técnico (código mal escrito que não escala), mas o contexto "com aumento de carga" sem menção a uma feature nova é suficiente para `tech-debt-evaluator`. Se a frase fosse "esse sistema escala para a nova feature de notificações?", mudaria para `feature-impact-analysis` — porque há uma feature nova como âncora.

- **"esse sistema escala bem para suportar a nova feature de notificações em tempo real?"** — a presença de uma feature nova como contexto muda completamente o acionamento. Não é avaliação de saúde do código atual, é análise de impacto de algo novo. Deve acionar `feature-impact-analysis`.

- **"o time de dev sempre reclama desse módulo — o que há de errado nele?"** — frase informal sem palavras-chave técnicas ("débito", "code smell", "qualidade"). Deve acionar mesmo assim: a skill cobre pedidos sobre "o que há de errado" num módulo, independente do vocabulário usado.

## Ajuste aplicado na description

O sinal mais confiável desta skill é a ausência de uma feature nova como âncora e o foco no estado atual do código (saúde, manutenibilidade, custo futuro). Quando há uma feature nova mencionada, o acionamento correto passa a ser `feature-impact-analysis`. Esse critério foi reforçado no exemplo negativo mais difícil (o do sistema de notificações).
