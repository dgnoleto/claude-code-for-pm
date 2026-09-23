# Manutenção do Claude Code for PM

Este repositório distribui fluxos de trabalho de produto em skills para Claude Code. O idioma de conteúdo é português. Exemplos são didáticos; não confundir material editorial com avaliação executada ou sistema de produção.

## Escopo e autorização

1. Proponha mudanças de comportamento antes de modificar skills existentes. A aprovação da proposta na conversa autoriza os ajustes correspondentes; não peça a mesma confirmação novamente.
2. Não altere evals históricos nem o glossário sem pedido específico. Novas skills devem trazer seus próprios casos, identificados como não executados. Não reescreva evidência antiga para adequá-la ao novo comportamento.
3. Alterar arquivos localmente não autoriza publicar, enviar mensagens, ativar integrações ou modificar outros repositórios. Respeite a autorização da tarefa.

## Padrão de uma skill

- Pasta com nome em inglês, minúsculas e hífens; conteúdo em português.
- `SKILL.md` com `name`, `description` e `metadata.version` em YAML. A versão é metadado editorial, não controle de comportamento do Claude Code.
- Fluxo em etapas que aproveita contexto já fornecido. Confirmação humana deve resolver uma lacuna ou decisão real, não repetir informações disponíveis.
- Saída na conversa por padrão; arquivo quando solicitado. Markdown padrão e orientação para Obsidian quando pertinente.
- `CHANGELOG.md`: incrementar versão a cada mudança de comportamento e registrar o motivo.
- Para nova skill: `evals/trigger-eval.json` com pelo menos 8 positivos e 8 negativos, incluindo quase-acertos, e `evals/notas-refinamento.md` com critérios e estado da avaliação.
- Referências dentro da pasta da skill quando necessárias à execução. Não depender de arquivos da raiz para funcionar após instalação individual.

## Qualidade

Organize pelo trabalho do PM, não por uma lista de frameworks. Não invente dados, ganhos, pesquisas, aprovações ou resultados. Distinga evidência, hipótese, estimativa e decisão. Trate ferramentas como opcionais e verifique capacidades reais antes de prometer operações.

Preserve nomes existentes nesta revisão. Capacidades planejadas devem estar claramente separadas das disponíveis. Não duplicar no pacote a metodologia geral do Code Discovery Toolkit.

## Verificação

Confira frontmatter, referências locais, exemplos numéricos e mudanças de versão. Os testes do checkout só verificam sua base sintética. Avaliações do comportamento no Claude Code devem seguir `docs/avaliacao-de-respostas.md`, com transcrições e limitações.
