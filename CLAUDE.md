# CLAUDE.md — Instruções para o Claude Code neste repositório

Este arquivo instrui o Claude Code sobre como se comportar ao trabalhar **neste repositório** (`claude-code-for-pm`). Leia antes de qualquer ação.

---

## O que é este repositório

Este é um repositório de **Skills para Claude Code voltadas a PMs e POs**. Ele contém arquivos de instrução (`SKILL.md`), documentação de onboarding (`guia-instalacao/`), evals de gatilho (`evals/`) e um glossário técnico (`GLOSSARIO.md`).

Não é um repositório de código de produção. Nenhum arquivo aqui é executável em ambiente de produção. A linguagem principal é **português**.

---

## Regras de comportamento neste repositório

### 1. Nunca modificar um SKILL.md sem proposta e confirmação explícita

Qualquer alteração em um arquivo `SKILL.md` existente — incluindo a `description`, o fluxo de etapas, os princípios ou os modelos de saída — deve ser **proposta primeiro** com justificativa clara. Só execute a alteração após confirmação explícita do usuário.

### 2. Ao atualizar uma skill, sempre incrementar a versão e registrar no CHANGELOG

Se uma skill for atualizada, dois passos são obrigatórios:
- Incrementar o campo `version` no frontmatter do `SKILL.md` (ex: `1.0` → `1.1`)
- Adicionar uma entrada no `CHANGELOG.md` da skill com a data e o que mudou

### 3. Nunca modificar arquivos de evals sem instrução explícita

Os arquivos `evals/trigger-eval.json` e `evals/notas-refinamento.md` são documentação de raciocínio — não são gerados automaticamente. Só altere se o usuário pedir especificamente.

### 4. Ao criar uma nova skill, seguir o padrão do PM Skill Pack

Toda skill nova deve ter:
- `SKILL.md` com frontmatter contendo `version`, `name` e `description`
- Fluxo em etapas numeradas com gates humanos de confirmação de escopo e destino
- Saída em Markdown padrão **e** Obsidian Flavored Markdown
- Pasta `evals/` com `trigger-eval.json` (mínimo 8 positivos + 8 negativos, incluindo quase-acertos) e `notas-refinamento.md`
- `CHANGELOG.md` com a entrada da versão inicial

### 5. Nunca alterar o GLOSSARIO.md sem proposta prévia

O glossário tem estrutura e tom deliberados. Qualquer adição ou edição deve ser proposta com o trecho exato antes de ser executada.

### 6. Manter o português como língua padrão de todo o conteúdo

Todos os arquivos de conteúdo deste repositório estão em português. Ao criar ou editar qualquer arquivo, use português — exceto nomes técnicos de campos, comandos de código ou termos que não têm tradução convencional (ex: `frontmatter`, `SKILL.md`, `trigger`).

---

## O que você pode fazer livremente

- Ler qualquer arquivo do repositório para responder perguntas
- Sugerir melhorias, novos conteúdos ou ajustes — desde que apresente a proposta antes de executar
- Gerar rascunhos de novos `SKILL.md`, `CHANGELOG.md` ou entradas de glossário para revisão do usuário

---

## Referência rápida

| Ação | Precisa de confirmação? |
|---|---|
| Ler qualquer arquivo | Não |
| Propor mudança em SKILL.md | Não (proposta é bem-vinda) |
| Executar mudança em SKILL.md | Sim — sempre |
| Criar nova skill completa | Sim — aprovar estrutura antes |
| Alterar trigger-eval.json | Sim — sempre |
| Incrementar versão + CHANGELOG | Obrigatório junto com qualquer edição de SKILL.md |
