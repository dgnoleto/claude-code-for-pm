---
name: code-discovery
description: Use sempre que o usuário pedir para investigar, mapear, entender ou documentar um repositório de código desconhecido, legado, órfão ou esquecido — mesmo que ele não use as palavras "discovery" ou "mapear" explicitamente. Cobre pedidos como "ninguém lembra o que esse repositório faz", "herdei esse projeto e preciso entender antes de tocar", "acha código morto/duplicado/redundante aqui", "esse arquivo ainda é usado por alguma coisa?", ou "faz um discovery desse projeto". NÃO use para refatorar, corrigir bugs, implementar funcionalidades, ou documentar código novo/conhecido — esta skill é só de investigação e relatório sobre código que já existe e está em dúvida.
---

# Code Discovery — Investigação de Repositórios Esquecidos

Esta skill aplica a mesma metodologia do [Code Discovery Toolkit](https://github.com/SEU-USUARIO/code-discovery-toolkit), de forma autônoma: você usa suas próprias ferramentas (Glob, Grep, Read, Bash, Write) em vez de depender de alguém colar conteúdo manualmente.

## Princípios não negociáveis (valem durante toda a sessão, não só na primeira resposta)

- **Não inventar.** Toda conclusão precisa de evidência real: código, commit, histórico, ou confirmação do usuário. Se não houver evidência suficiente, diga isso explicitamente em vez de supor.
- **Não refatorar, corrigir, renomear, mover ou apagar nada sem autorização explícita do usuário.** Esta skill é de investigação e relatório — não de execução. Mesmo que você tenha ferramentas de escrita disponíveis, não as use para alterar código de produção como parte desta skill.
- **Não sair do escopo confirmado pelo usuário.** Achados fora do escopo vão para uma seção separada do relatório, não são investigados na hora.

## Fluxo

### Etapa 1 — Varredura leve

Use Glob para listar a estrutura de pastas e nomes de arquivos, e `git log --oneline | tail -20` (via Bash) para ver os commits iniciais, se houver histórico Git. NÃO leia o conteúdo completo dos arquivos ainda — o objetivo aqui é só mapear o que existe, gastando o mínimo de tokens possível antes de saber o que realmente precisa de leitura profunda.

### Etapa 2 — Confirmação de escopo

Pare e pergunte ao usuário:

"Quer que eu investigue (a) o repositório como um todo, (b) um módulo específico, (c) uma função específica, (d) um campo específico, ou (e) candidatos a código morto/duplicação que você já tem em mente?"

Se a resposta não for "o repositório como um todo", avise explicitamente que as conclusões não vão cobrir o restante do repositório e podem não se sustentar se o usuário tentar generalizar para o sistema inteiro.

Espere a resposta antes de continuar — não prossiga com leitura profunda sem essa confirmação.

### Etapa 3 — Local de saída e formato

Sugira um caminho padrão para salvar o relatório, por exemplo `discovery/AAAA-MM-DD-<tipo>-<escopo>.md` (onde `<tipo>` é mapeamento, codigo-morto, duplicacoes ou relatorio-final, e `<escopo>` é o que foi confirmado na etapa 2). Pergunte se o usuário confirma esse caminho ou prefere outro.

Pergunte também qual formato o usuário prefere: Markdown padrão, ou Obsidian Flavored Markdown (com properties no frontmatter, callouts e wikilinks) — relevante se ele lê esses relatórios no Obsidian. Se a skill `obsidian-markdown` também estiver disponível na sessão, prefira consultá-la para a sintaxe exata em vez de confiar só na referência rápida abaixo.

Espere a confirmação de caminho e formato antes de escrever qualquer arquivo.

### Etapa 4 — Investigação (só depois das etapas acima)

Agora sim, use Read e Grep para ler o conteúdo necessário dentro do escopo confirmado. Dependendo do que foi pedido, investigue:

- **Propósito**: o que o repositório/módulo parece fazer, com base no código, README e histórico.
- **Candidatos a código morto**: funções, arquivos ou trechos sem referência aparente em nenhum outro lugar do escopo investigado.
- **Duplicações e redundâncias**: lógica repetida, funções muito parecidas, arquivos quase idênticos.

Para cada achado, registre: localização exata (arquivo e linha/função), a evidência que sustenta o achado, e o nível de confiança (confirmado / provável / hipótese).

### Etapa 5 — Relatório

Escreva o relatório no caminho confirmado na etapa 3, no formato escolhido.

**Markdown padrão:**

```markdown
# Relatório de Discovery — [nome do repositório/escopo]

**Data:** [data atual]
**Escopo investigado:** [o que foi confirmado na etapa 2]

## Achados confirmados
[com evidência clara — arquivo, linha, commit]

## Achados prováveis
[heurística forte, mas sem confirmação humana ainda]

## Hipóteses
[precisam de validação antes de virar conclusão]

## Achados fora do escopo (para outra rodada)
[qualquer coisa relevante encontrada fora do que foi confirmado]

## Perguntas abertas para validar com o time
[...]

## Recomendação
> Esta seção contém recomendações, não decisões. Nenhuma ação foi executada.
[sugestões de investigar/validar — nunca de remover, refatorar ou alterar]
```

**Obsidian Flavored Markdown:** mesma estrutura de conteúdo acima, mas com properties no frontmatter (`title`, `date`, `tags`, `status`), callouts para achados fora do escopo e hipóteses, e wikilinks para outros relatórios relacionados do mesmo discovery (use o nome do arquivo sem extensão como destino do wikilink):

```markdown
---
title: Discovery — [nome do repositório/escopo]
date: [data atual]
tags:
  - discovery
  - [tipo: mapeamento / codigo-morto / duplicacoes / relatorio-final]
status: rascunho
---

# Discovery — [nome do repositório/escopo]

**Escopo investigado:** [o que foi confirmado na etapa 2]

## Achados confirmados
[com evidência clara — arquivo, linha, commit]

## Achados prováveis
[heurística forte, mas sem confirmação humana ainda]

> [!question] Hipóteses
> [precisam de validação antes de virar conclusão]

> [!warning] Fora do escopo (para outra rodada)
> [qualquer coisa relevante encontrada fora do que foi confirmado]

## Perguntas abertas para validar com o time
[...]

## Recomendação
> [!important] Recomendações, não decisões
> Nenhuma ação foi executada. [sugestões de investigar/validar]

Relatório relacionado: [[AAAA-MM-DD-outro-tipo-escopo]]
```

Avise o usuário onde o arquivo foi salvo ao final, em qualquer um dos dois formatos.

## Referência

A metodologia completa, incluindo prompts equivalentes para usar com outras IAs (ChatGPT, Gemini, Cursor), está documentada no [Code Discovery Toolkit](https://github.com/SEU-USUARIO/code-discovery-toolkit) — esta skill é a versão autônoma dessa mesma metodologia, pensada para o Claude Code.

A sintaxe Obsidian usada na etapa 5 segue a skill [`obsidian-markdown`](https://github.com/kepano/obsidian-skills) (Steph Ango). A pasta `evals/` desta skill segue a metodologia de testes de gatilho do [`skill-creator`](https://github.com/anthropics/skills) (Anthropic).
