---
version: 1.0
name: feature-impact-analysis
description: Use sempre que o usuário apresentar uma nova funcionalidade pretendida, rascunho de especificação ou PRD (Product Requirements Document) e pedir para analisar o impacto arquitetural, mapear arquivos afetados ou estimar riscos técnicos dessa alteração na base de código. Cobre pedidos como "se eu quiser criar a feature X, o que ela afeta no código?", "faz uma análise de impacto dessa PRD nesse repo", ou "onde eu mexeria no código para mudar a regra de cupom?". NÃO use para implementar a funcionalidade — esta skill serve apenas para documentar o impacto técnico pré-refinamento.
---

# Feature Impact Analysis — Análise de Impacto Técnico para Novas Features

Esta skill ajuda Product Managers a anteciparem a complexidade e o risco técnico de uma nova funcionalidade (ou alteração de regra de negócio) antes de levá-la para o refinamento técnico com o time de engenharia.

## Princípios não negociáveis (valem durante toda a sessão)

- **Foco em Componentes e Dependências:** Identifique exatamente quais partes do sistema (Ex: APIs públicas, Banco de Dados, Controllers de Autenticação) serão modificadas.
- **Risco Orientado a Produto:** Explique o risco em termos de impacto para o produto (Ex: "Risco Alto: altera o fluxo de checkout que afeta a conversão de vendas", e não apenas "Risco Alto: altera a classe principal").
- **Cruzamento com Arquitetura:** Se o repositório tiver arquivos de especificação de arquitetura ou diagramas legados, use-os como base inicial.

## Fluxo

### Etapa 1 — Varredura leve & Documentação de Apoio

Use Glob para mapear a estrutura física do repositório. 

**Importante (Cruzamento de Contexto):** Busque ativamente por documentação técnica de arquitetura, esquemas de banco de dados (`schema.sql`, `prisma.schema`), diagramas ou PRDs anteriores na pasta. A combinação de *código-fonte + documentação legada* elevou a precisão da análise de impacto para a faixa de **93% a 97%** — resultado observado pelo autor em repositórios B2B de média complexidade. Repositórios com menor cobertura de documentação técnica podem apresentar resultados diferentes.

NÃO faça leitura profunda de códigos ainda.

### Etapa 2 — Entrada da Especificação (PRD)

Pare e solicite ao PM:

"Por favor, compartilhe a descrição da nova feature ou alteração que você quer analisar. Pode ser:
- Um rascunho rápido de ideias
- Uma História de Usuário / Critérios de Aceite
- O texto ou caminho de uma PRD completa (Product Requirements Document)"

Espere o envio do escopo ou texto do usuário.

### Etapa 3 — Caminho de Saída e Formato

Sugira salvar em `impacto/AAAA-MM-DD-impacto-<nome-feature>.md`. Pergunte qual formato ele prefere:
- **Markdown padrão:** Ideal para exportar para o Notion ou Wiki da empresa.
- **Obsidian Flavored Markdown:** Com properties (metadados), callouts e wikilinks.

Espere a confirmação do usuário.

### Etapa 4 — Mapeamento do Impacto

Use Grep e Read para investigar no código os locais que serão afetados pela feature descrita na Etapa 2. 

Procure:
- Onde os dados da nova funcionalidade serão gravados (Banco de Dados).
- Quais APIs/Endpoints existentes precisarão de novos parâmetros ou novas rotas.
- Quais regras de negócio existentes serão modificadas/sobrescritas.
- Possíveis quebras de compatibilidade (Breaking Changes).

### Etapa 5 — Relatório de Impacto Técnico

Escreva o relatório no formato escolhido e no caminho confirmado na Etapa 3.

**Modelo de Saída (Markdown Padrão):**

```markdown
# ⚡ Análise de Impacto Técnico — [Nome da Feature]

**Data da Análise:** [data atual]
**Proposta de Negócio:** [resumo curto da nova feature]

## 🎯 Componentes Afetados no Repositório

### 1. Banco de Dados / Persistência
- **Onde mudar:** [Ex: Tabela `Users`, arquivo de migrate X]
- **Descrição da mudança:** [Ex: Necessário adicionar coluna `vip_status`]

### 2. Back-End / APIs
- **Arquivos afetados:** `controllers/userController.js` (linhas X-Y)
- **Descrição da mudança:** [Ex: Mudar rota `/users/profile` para expor o novo campo]

### 3. Front-End / Telas (Se houver)
- **Arquivos afetados:** `pages/UserProfile.tsx`
- **Descrição da mudança:** [...]

---

## ⚠️ Avaliação de Risco Técnico
- **Nível de Risco:** [Baixo / Médio / Alto]
- **Justificativa de Produto:** [Ex: Risco Alto. A alteração afeta o fluxo crítico de pagamento. Qualquer erro impede a conclusão de vendas no app.]

## 🔗 Dependências Chaves & Efeitos Colaterais
- **Integrações Externas:** [Ex: Depende da API do Stripe atualizar para suportar o novo fluxo]
- **Possíveis Efeitos Colaterais:** [Ex: Outros relatórios que usam a tabela `Users` precisarão tratar o campo nulo]

## 💬 Pauta para o Refinamento Técnico (Perguntas para os Devs)
1. [Dúvidas de viabilidade técnica para discutir na planning]
```

**Modelo de Saída (Obsidian):**

```markdown
---
title: Impacto Técnico — [Feature]
date: [data atual]
tags:
  - analise-de-impacto
  - refinamento
status: rascunho
---

# ⚡ Impacto Técnico — [Feature]

**Resumo:** [resumo curto]

## Componentes Afetados
- **Banco de Dados:** [schema.prisma](file:///caminho/absoluto/schema.prisma#L45)
- **API Controller:** [userController.js](file:///caminho/absoluto/userController.js#L12)

> [!caution] Risco Alto
> A alteração afeta o fluxo central de autenticação do usuário.

## Perguntas para Planning
- [ ] O banco atual suporta a migração desse campo sem downtime?
```

Avise o usuário quando o relatório for gerado.
