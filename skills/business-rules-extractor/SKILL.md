---
name: business-rules-extractor
description: Use sempre que o usuário pedir para extrair, mapear, documentar ou entender regras de negócio, lógicas de validação, restrições, fórmulas de cálculo ou termos implícitos codificados no repositório. Cobre pedidos como "quais as regras de frete desse checkout?", "como funciona o cálculo de cupom no código?", "me explica a lógica desse validador", ou "extrai as regras desse módulo para uma PRD". NÃO use para refatorar, reescrever ou sugerir novas regras de negócio — esta skill serve apenas para traduzir e documentar o comportamento atual do código em linguagem de produto.
---

# Business Rules Extractor — Extração de Regras de Negócio Ocultas

Esta skill traduz a complexidade do código de programação em regras de negócio claras, didáticas e organizadas em formato de especificação de produto, cruzando o código-fonte com qualquer documentação legada disponível para garantir precisão cirúrgica.

## Princípios não negociáveis (valem durante toda a sessão)

- **Linguagem de Produto:** Evite jargões técnicos de programação (como "instanciar classe", "passar parâmetro por referência", etc.) no corpo das regras. Traduza estruturas condicionais (`if/else`) e loops em lógica clara em português (ex: "Quando o usuário for...", "Se a condição X...").
- **Evidência no Código:** Cada regra extraída deve referenciar o arquivo e a linha correspondente para auditoria técnica posterior do time de desenvolvimento.
- **Divergências código-documentação:** Se houver documentação legada que diz uma coisa, mas o código faz outra, destaque essa divergência imediatamente como uma "Inconsistência".

## Fluxo

### Etapa 1 — Varredura leve & Documentação de Apoio

Use Glob para listar arquivos e pastas do repositório. 

**Importante (Cruzamento de Contexto):** Busque ativamente por qualquer pasta de especificação, manuais antigos, PRDs anteriores ou arquivos `.md` e `.txt` na raiz que contenham requisitos do sistema. Se encontrar, faça uma leitura rápida para servir de base. O cruzamento das regras descritas nesses documentos com o código-fonte real do projeto garante **93% a 97% de precisão** nas regras extraídas.

NÃO faça leitura profunda de códigos de programação ainda.

### Etapa 2 — Confirmação de Escopo

Pare e valide com o PM:

"Qual regra de negócio ou módulo você deseja extrair?
(a) Um fluxo completo (ex: Checkout, Cadastro de Usuário)
(b) Uma fórmula/cálculo específico (ex: Regra de Imposto, Desconto, Frete)
(c) Uma lógica de validação específica (ex: Regras de senha, Validador de dados)
(d) Outro escopo específico (informar qual)"

Espere a resposta do usuário antes de prosseguir.

### Etapa 3 — Caminho de Saída e Formato

Sugira salvar as regras em `documentacao/AAAA-MM-DD-regras-<escopo>.md`. Pergunte qual formato ele prefere:
- **Markdown padrão:** Ideal para copiar e colar no Confluence, Jira ou Notion.
- **Obsidian Flavored Markdown:** Com properties (metadados), callouts e wikilinks para interconectar notas no Obsidian.

Espere a confirmação do usuário antes de começar a extração profunda.

### Etapa 4 — Extração e Tradução

Agora, use Read e Grep nos arquivos identificados. Mapeie a lógica interna. Traduza os trechos lógicos em regras de negócio textuais estruturadas.

Para cada regra, identifique:
- **Nome da Regra:** Nome amigável de produto (ex: *Desconto Máximo por Cupom*).
- **Lógica de Negócio:** Explicação detalhada em português.
- **Rastro Técnico:** O arquivo e linhas de código que executam essa regra.
- **Nível de Certeza:** *Confirmado* (se há código claro rodando), *Provável* (se a lógica aponta para isso mas tem dependência externa), ou *Inconsistência* (se o código diverge do que estava planejado na documentação).

### Etapa 5 — Relatório de Regras de Negócio

Escreva o arquivo no formato escolhido e no caminho confirmado na Etapa 3.

**Modelo de Saída (Markdown Padrão):**

```markdown
# 📋 Documento de Regras de Negócio — [Escopo / Módulo]

**Data da Extração:** [data atual]
**Escopo Analisado:** [escopo confirmado na etapa 2]
**Documentos de Apoio Consultados:** [PRD antiga, spec legada ou nenhum]

## Regras de Negócio Identificadas

### 1. [Nome da Regra 1]
- **Descrição:** [Explicação em português de negócio]
- **Rastro Técnico:** `caminho/do/arquivo.js` (linhas X-Y)
- **Status de Certeza:** [Confirmado / Provável / Inconsistência]

### 2. [Nome da Regra 2]
- **Descrição:** [...]
- **Rastro Técnico:** `caminho/do/arquivo.js` (linhas X-Y)
- **Status de Certeza:** [...]

## Inconsistências Detectadas (Código vs Documentação)
> Se o código faz algo diferente do que os documentos de apoio antigos previam.
- **Divergência:** [Ex: O documento antigo dizia que a taxa de juros era de 2%, mas o código-fonte fixa em 2.5%]
- **Rastro:** `pasta/arquivo.py` (linha Z)

## Perguntas para Refinamento Técnico (Dúvidas de Produto)
1. [Dúvidas para validar com os desenvolvedores ou stakeholders]
```

**Modelo de Saída (Obsidian):**

```markdown
---
title: Regras de Negócio — [Escopo]
date: [data atual]
tags:
  - regras-de-negocio
  - produto
status: rascunho
---

# 📋 Regras de Negócio — [Escopo]

**Escopo Analisado:** [escopo]
**Documentos de Apoio:** [[AAAA-MM-DD-documento-de-requisito-antigo]]

## Regras Identificadas

### 1. [Nome da Regra]
- **Descrição:** [Explicação]
- **Rastro:** [arquivo.js](file:///caminho/absoluto/arquivo.js#LX-LY)
- **Status:** Confirmado

> [!warning] Inconsistência Detectada
> O código difere da documentação legada na taxa de cobrança. Ver [detalhes](file:///caminho/absoluto/arquivo.js#LZ).

## Dúvidas para o Time de Engenharia
- [ ] Validar a lógica de...
```

Avise o usuário quando o arquivo for salvo.
