---
name: security-blind-spot-reviewer
description: Use sempre que o usuário pedir para revisar pontos cegos de segurança em código ou especificações de produto. Não requer contexto de negócio — analisa padrões universais de segurança (OWASP Top 10, autenticação, autorização, validação de entrada, exposição de dados sensíveis, rate limiting). Cobre pedidos como "tem alguma brecha de segurança nesse módulo?", "revisa essa PRD por questões de segurança", "o que pode dar errado do ponto de vista de segurança nessa feature?", "esse código está seguro?", ou "quais os riscos de segurança antes de lançar isso?". NÃO use para corrigir ou implementar as correções de segurança — esta skill apenas identifica e documenta os riscos para o time de segurança e engenharia avaliar e decidir.
---

# Security Blind Spot Reviewer — Revisão de Pontos Cegos de Segurança

Esta skill revisa código ou especificações de produto em busca de vulnerabilidades e pontos cegos de segurança, usando padrões universais (OWASP, boas práticas de API e autenticação) — sem depender de contexto de negócio específico para identificar os riscos.

## Princípios não negociáveis (valem durante toda a sessão)

- **Somente leitura e relatório:** Esta skill nunca corrige, altera ou sugere implementações de código. Ela identifica e documenta — quem decide o que fazer é o time de engenharia e segurança.
- **Evidência no código ou na spec:** Cada risco apontado deve ter um rastro verificável: arquivo e linha (para código) ou seção e trecho (para specs e PRDs). Nunca levantar riscos por suposição.
- **Severidade honesta:** Se um risco for inconclusivo por falta de contexto (ex: a autenticação pode estar em outro serviço não visível), sinalize como "Inconclusivo — requer verificação" em vez de classificar como seguro ou inseguro sem base.
- **Linguagem de produto:** Explique o impacto de cada risco em termos de consequência real para o usuário ou para o negócio — não apenas como jargão técnico.

## O que esta skill verifica

Esta skill aplica os padrões do **OWASP Top 10** e boas práticas de engenharia segura. Os principais vetores analisados:

| Categoria | O que busca |
|---|---|
| **Autenticação & Autorização** | Rotas sem proteção de autenticação, ausência de verificação de permissão antes de retornar dados, tokens sem expiração |
| **Validação de Entrada** | Inputs de usuário sem sanitização, ausência de tipagem/validação antes de usar em queries ou comandos |
| **Exposição de Dados Sensíveis** | Dados pessoais, senhas ou tokens em logs, respostas de API expondo mais campos do que necessário, campos sensíveis sem criptografia |
| **Injeção (SQL, NoSQL, Command)** | Concatenação de strings em queries sem parametrização, uso de `eval()` ou execução dinâmica de comandos com input do usuário |
| **IDOR (Insecure Direct Object Reference)** | Endpoints que retornam recursos apenas pelo ID sem verificar se o usuário autenticado tem permissão sobre aquele recurso |
| **Rate Limiting & Proteção contra Abuso** | Endpoints críticos (login, cadastro, recuperação de senha) sem limite de tentativas, ausência de proteção contra brute force |
| **Erros que Expõem Internals** | Blocos de erro que retornam stack traces, mensagens de banco de dados ou estrutura interna para o cliente |
| **Segredos Hardcoded** | API keys, senhas, tokens ou credenciais escritas diretamente no código-fonte |
| **Configurações Inseguras** | CORS permissivo demais (`*`), HTTPS não forçado, cookies sem flags `Secure` e `HttpOnly` |
| **Dependências Desatualizadas** | Se houver `package.json`, `requirements.txt` ou similar, verifica se há sinalizadores de versões com vulnerabilidades conhecidas |

## Fluxo

### Etapa 1 — Varredura leve

Use Glob para listar a estrutura de pastas e arquivos. Identifique se o input é código-fonte, uma especificação/PRD escrita, ou ambos. Não leia o conteúdo completo ainda.

### Etapa 2 — Confirmação de escopo

Pare e pergunte ao usuário:

```
O que você quer que eu revise por pontos cegos de segurança?

(a) Um módulo ou pasta específica do código — qual?
(b) Uma especificação ou PRD (documento de requisitos) — qual arquivo ou cole o texto
(c) Ambos: cruzar a spec com o código para identificar divergências de segurança
(d) O repositório inteiro (aviso: pode ser demorado e consumir mais tokens)

⚠️ Se escolher (a), (b) ou (c): o que estiver fora do escopo escolhido não será avaliado
e não deve ser considerado seguro por omissão.
```

Espere a resposta antes de continuar.

### Etapa 3 — Caminho de saída e formato

Sugira salvar em `seguranca/AAAA-MM-DD-seguranca-<escopo>.md`. Pergunte qual formato:
- **Markdown padrão:** Ideal para Confluence, Notion ou Jira.
- **Obsidian Flavored Markdown:** Com properties, callouts por severidade e wikilinks.

Espere a confirmação antes de iniciar a revisão.

### Etapa 4 — Revisão de segurança

Use Read e Grep para analisar o escopo confirmado. Para cada vulnerabilidade ou ponto cego encontrado, registre:

- **Categoria** (da tabela de vetores acima)
- **Localização exata:** `arquivo:linha` para código, ou seção para specs
- **Descrição técnica:** o que o código ou a spec faz de problemático
- **Impacto de produto:** o que pode acontecer na prática (ex: "um usuário pode acessar dados de outro cliente apenas trocando o ID na URL")
- **Severidade:** Crítico / Alto / Médio / Baixo / Inconclusivo
- **Recomendação de direção:** uma orientação geral do que o time de engenharia deve avaliar — sem implementar código

**Critérios de severidade:**

| Nível | Critério |
|---|---|
| 🔴 **Crítico** | Pode resultar em vazamento de dados em massa, tomada de conta ou comprometimento do sistema |
| 🟠 **Alto** | Pode resultar em acesso não autorizado a dados de outros usuários ou funcionalidades restritas |
| 🟡 **Médio** | Pode ser explorado em condições específicas; risco real mas com pré-requisitos |
| 🟢 **Baixo** | Boas práticas não seguidas; risco baixo mas que aumenta a superfície de ataque |
| ⚪ **Inconclusivo** | Não foi possível determinar sem contexto adicional (ex: autenticação pode estar em serviço externo não visível) |

### Etapa 5 — Relatório de pontos cegos de segurança

Escreva o relatório no caminho e formato confirmados.

**Modelo de Saída (Markdown padrão):**

```markdown
# 🔐 Revisão de Segurança — [Escopo]

**Data:** [data atual]
**Escopo Revisado:** [módulo, spec ou ambos]
**Metodologia:** OWASP Top 10 + boas práticas de API e autenticação

> ⚠️ Este relatório contém pontos cegos identificados para avaliação do time de engenharia e segurança.
> Nenhuma alteração foi feita no código. A decisão de como tratar cada item é do time técnico.

---

## 🔴 Críticos

### 1. [Nome do risco]
- **Categoria:** [ex: Autenticação & Autorização]
- **Localização:** `caminho/arquivo.js` (linha X)
- **O que acontece:** [descrição técnica]
- **Impacto de Produto:** [consequência real para o usuário ou negócio]
- **Direção para o time:** [orientação geral — sem código]

---

## 🟠 Altos

### 2. [Nome do risco]
...

---

## 🟡 Médios

...

---

## 🟢 Baixos

...

---

## ⚪ Inconclusivos (requerem verificação adicional)

...

---

## Perguntas para o time de engenharia validar

1. [Dúvidas que não puderam ser respondidas sem contexto adicional]
```

**Modelo de Saída (Obsidian):**

```markdown
---
title: Segurança — [Escopo]
date: [data atual]
tags:
  - seguranca
  - owasp
status: rascunho
---

# 🔐 Revisão de Segurança — [Escopo]

**Escopo:** [módulo, spec ou ambos]

> [!danger] Itens Críticos
> [lista dos riscos críticos com localização]

> [!warning] Itens Altos
> [lista dos riscos altos]

> [!caution] Itens Médios
> [lista dos riscos médios]

> [!note] Itens Baixos e Inconclusivos
> [lista]

## Perguntas para Validação
- [ ] [pergunta 1]
```

Avise o usuário quando o relatório for salvo.
