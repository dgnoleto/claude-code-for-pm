# Notas de refinamento — `security-blind-spot-reviewer`

Conjunto de testes de gatilho seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic): 8 frases que devem acionar a skill e 8 que não devem, incluindo quase-acertos propositalmente difíceis.

## Quase-acertos mais importantes

- **"como funciona a lógica de permissões nesse sistema?"** — soa como revisão de segurança, mas é um pedido de entendimento da lógica existente, não de identificação de falhas. O foco em "como funciona" aponta para `business-rules-extractor`. `security-blind-spot-reviewer` deve ser acionada quando o foco é "o que pode estar errado ou exposto", não "me explica como isso funciona".

- **"o módulo de autenticação tem débito técnico?"** — autenticação é um tema de segurança, mas a pergunta é sobre qualidade e manutenibilidade do código, não sobre vetores de ataque. Deve acionar `tech-debt-evaluator`.

- **"o que esse módulo de segurança faz? ninguém aqui sabe"** — tem "segurança" no nome do módulo, mas o pedido é de investigação de propósito desconhecido. Deve acionar `code-discovery`.

- **"quais as regras de validação de senha que o sistema exige hoje?"** — validação de senha parece tema de segurança, mas é uma extração de regra de negócio existente (o que o sistema faz hoje), não uma revisão de pontos cegos. Deve acionar `business-rules-extractor`.

- **"esse formulário valida os inputs do usuário antes de salvar no banco?"** — este é o quase-acerto que DEVE acionar a skill, mesmo sendo uma pergunta sobre o que o código faz. A diferença: a pergunta tem como objetivo descobrir uma ausência de segurança (validação de input é um vetor OWASP), não documentar uma regra de negócio.

## Ajuste aplicado na description

O sinal mais confiável desta skill é a intenção de encontrar *ausências* e *vulnerabilidades*, não de entender *o que o código faz*. Quando a pergunta é "como funciona X?", tende a ser `business-rules-extractor` ou `code-discovery`. Quando é "X está protegido?", "pode ter Y nessa rota?" ou "o que pode dar errado antes do lançamento?", é esta skill.
