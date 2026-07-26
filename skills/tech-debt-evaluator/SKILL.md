---
name: tech-debt-evaluator
description: Use sempre que o usuário pedir para avaliar o débito técnico, a saúde do código, code smells, gargalos de performance aparentes ou problemas de manutenção no repositório. Cobre pedidos como "faz um diagnóstico de débito técnico desse repo", "onde estão as maiores gambiarras desse código?", "avalia a qualidade desse módulo", ou "me dá argumentos para convencer a diretoria a refatorar esse checkout". NÃO use para refatorar ou corrigir o código — esta skill serve apenas para traduzir o impacto técnico em riscos de negócio e retorno sobre investimento (ROI) da refatoração.
---

# Tech Debt Evaluator — Auditoria de Débito Técnico & ROI de Refatoração

Esta skill audita o código em busca de "gambiarras", complexidade excessiva e código morto, traduzindo esses problemas técnicos em riscos de negócio legíveis para PMs, diretores e stakeholders.

## Princípios não negociáveis (valem durante toda a sessão)

- **Tradução para Negócio (Métricas de Produto):** Não diga apenas "temos classes acopladas". Traduza para: "Isso aumenta o tempo de desenvolvimento de novas features em X% e o risco de bugs em outras telas".
- **Identificação de "Red Flags":** Destaque riscos críticos de segurança, performance ou quebra de serviço (Ex: queries sem paginação ou falta de tratamento de erro/timeout em conexões críticas).
- **Sem Modificações:** Não tente corrigir os arquivos de código.

## Fluxo

### Etapa 1 — Varredura leve & Documentação de Apoio

Use Glob para mapear a estrutura física do repositório.

**Importante (Cruzamento de Contexto):** Procure ativamente por arquivos de histórico de bugs, logs, issues relatadas, documentação de arquitetura antiga ou PRDs da primeira versão. A combinação de *código-fonte + histórico de problemas documentados* elevou a precisão do diagnóstico de débito técnico para a faixa de **93% a 97%** — resultado observado pelo autor em repositórios B2B com histórico de issues e PRDs disponíveis. Projetos sem histórico documentado podem apresentar resultados diferentes.

NÃO faça leitura profunda de códigos ainda.

### Etapa 2 — Confirmação de Escopo

Pare e valide com o PM:

"Onde você suspeita ou o time técnico mais reclama que há problemas de qualidade?
(a) No repositório inteiro (varredura geral)
(b) Em uma pasta/módulo específico (ex: checkout, painel de administração, integração com gateway)
(c) Em arquivos específicos que sempre dão bug"

Espere a resposta do usuário.

### Etapa 3 — Caminho de Saída e Formato

Sugira salvar em `debito-tecnico/AAAA-MM-DD-debito-<escopo>.md`. Perguntar qual formato ele prefere:
- **Markdown padrão:** Ideal para apresentações executivas ou Confluence.
- **Obsidian Flavored Markdown:** Com properties (metadados), callouts e wikilinks.

Espere a confirmação do usuário.

### Etapa 4 — Auditoria do Código

Use Grep e Read nos arquivos dentro do escopo confirmado. Procure por:
- **Funções gigantescas:** Funções com centenas de linhas difíceis de manter.
- **Código morto/duplicado:** Funções copiadas e coladas ou não referenciadas.
- **Acoplamento crítico:** Alterar um arquivo obriga a alterar outros 5 arquivos.
- **Falta de Tratamento de Erros:** Trechos de código que podem derrubar a aplicação sem avisar em caso de falha externa.

### Etapa 5 — Relatório de Débito Técnico & Argumentação de Negócio

Escreva o relatório no formato escolhido e no caminho confirmado na Etapa 3.

**Modelo de Saída (Markdown Padrão):**

```markdown
# 📉 Relatório de Débito Técnico & Risco de Produto — [Escopo]

**Data da Análise:** [data atual]
**Escopo Analisado:** [módulo ou geral]

## 🚨 Principais Pontos de Risco (Red Flags)

### 1. [Nome do Problema 1]
- **Onde está:** `caminho/do/arquivo.js` (linhas X-Y)
- **O que é técnico:** [Ex: Query de banco de dados sem paginação e sem limite de linhas]
- **Impacto no Produto (Negócio):** [Ex: Risco de queda do sistema. Se a base de dados crescer muito, a tela de histórico vai travar e o cliente não conseguirá ver os pedidos.]
- **Esforço de Correção:** [Baixo / Médio / Alto]

### 2. [Nome do Problema 2]
- **Onde está:** `caminho/do/arquivo2.js` (linhas A-B)
- **O que é técnico:** [Ex: Lógica de checkout duplicada em 3 arquivos diferentes]
- **Impacto no Produto (Negócio):** [Ex: Alto custo de manutenção. Qualquer alteração de preço ou cupom precisa ser replicada em 3 lugares, aumentando a chance de bugs e atrasando o roadmap.]
- **Esforço de Correção:** [Médio]

---

## 💼 Argumentação para Negócio & ROI da Refatoração
> Use esta seção para convencer stakeholders sobre a importância de investir tempo limpando esse código.

- **Custo da Inação (O que acontece se não mexer?):** [Ex: Aumento progressivo de bugs reportados por clientes no checkout e lentidão nas entregas de novas features.]
- **Benefício da Refatoração (O que ganhamos?):** [Ex: Redução no tempo de desenvolvimento de novas regras de pagamento em até 50% e eliminação de falhas de timeout.]
- **Métrica Sugerida de Sucesso:** [Ex: Tempo médio de carregamento da página ou taxa de conversão do checkout.]
```

**Modelo de Saída (Obsidian):**

```markdown
---
title: Débito Técnico — [Módulo]
date: [data atual]
tags:
  - debito-tecnico
  - saude-do-codigo
status: rascunho
---

# 📉 Débito Técnico — [Módulo]

## Red Flags Identificadas

### 1. Query Sem Paginação
- **Arquivo:** [userController.js](file:///caminho/absoluto/userController.js#L89)
- **Impacto de Produto:** Risco iminente de queda na produção sob alto tráfego.

> [!important] Argumento de ROI para Negócio
> A refatoração desse módulo reduzirá o custo de servidores da AWS e acelerará o lançamento de novas features de relatório.
```

Avise o usuário quando o relatório for gerado.
