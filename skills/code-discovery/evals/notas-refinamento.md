# Notas de refinamento — description da skill `code-discovery`

Este conjunto de testes foi montado seguindo a metodologia do [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) (Anthropic): 8 frases que deveriam acionar a skill e 8 que não deveriam, incluindo alguns "quase-acertos" propositalmente difíceis — frases que usam palavras parecidas mas pedem algo diferente.

Importante: o `skill-creator` tem um script (`run_loop.py`) que roda esse teste de forma automatizada de verdade, chamando o Claude Code repetidamente e medindo a taxa de acerto. Isso só funciona de dentro do Claude Code, com acesso a sub-agentes — não é algo que dá pra executar num ambiente de chat comum. O que está documentado aqui é o raciocínio aplicado manualmente sobre esse mesmo conjunto de testes; o arquivo `trigger-eval.json` já está no formato certo pra rodar de verdade com o script oficial, se você quiser.

## Quase-acertos mais importantes

- **"refatora essa função... ela tá duplicada"** — usa a palavra "duplicada" (que está na description), mas o pedido real é refatorar, não investigar. É o teste mais importante: a description precisa deixar claro que o limite não é sobre o assunto (duplicação), e sim sobre a ação pedida (investigar vs. executar).
- **"atualiza o README"** / **"documenta essa API nova"** — usam a palavra "documentar" (também na description), mas se referem a documentação de algo novo/conhecido, não a investigar algo desconhecido ou esquecido.
- **"explica esse algoritmo... linha por linha"** — parece pedido de entendimento de código, mas é sobre uma função específica e já conhecida, não sobre um repositório desconhecido ou legado.

## Ajuste aplicado na description

A versão original já cobria bem esses casos (por já restringir os verbos "investigar/mapear/documentar" a repositórios "desconhecidos, legados ou esquecidos", e por ter uma cláusula negativa explícita). O ajuste foi reforçar dois pontos, seguindo a recomendação do `skill-creator` de deixar a description um pouco mais "insistente" pra evitar que a IA deixe de acionar a skill por falta de cobertura de frases:

1. Adicionar exemplos cobrindo o caso de um único arquivo/função (não só "o repositório inteiro"), como em "esse arquivo ainda é usado por alguma coisa?".
2. Deixar explícito que a skill deve acionar mesmo quando o usuário não usa as palavras "discovery" ou "mapear" — já que esse é um viés conhecido (IAs tendem a deixar de acionar skills quando a frase não usa palavras óbvias do domínio).
3. Adicionar "documentar código novo/conhecido" à lista de exclusões, deixando mais explícito o limite com os quase-acertos de documentação.

A description atualizada está no `SKILL.md`.
