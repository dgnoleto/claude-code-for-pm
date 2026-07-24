# 🤖 Claude Code para PM/PO

Um guia de instalação e uma Skill real do Claude Code para times de produto que já usam (ou querem começar a usar) IA agêntica no dia a dia — sem precisar ser dev.

## Nunca usou Claude Code? Comece aqui

1. Veja o guia de instalação pro seu sistema: [Windows](guia-instalacao/01-instalar-windows.md) ou [Mac](guia-instalacao/02-instalar-mac.md).
2. Depois, siga [`03-primeiros-passos-claude-code.md`](guia-instalacao/03-primeiros-passos-claude-code.md) pra rodar o Claude Code dentro de um repositório clonado.
3. Por fim, [`04-instalar-a-skill.md`](guia-instalacao/04-instalar-a-skill.md) explica como instalar a skill `code-discovery` deste repositório, pra começar a usar de verdade.

## Esse repositório é irmão do Code Discovery Toolkit

Esse projeto nasceu do [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit) — um conjunto de prompts e metodologia para investigar repositórios esquecidos, que funciona com **qualquer IA** (ChatGPT, Gemini, Cursor, Claude, etc.).

Este repositório aqui é diferente de propósito: ele é centrado numa ferramenta específica (Claude Code) e num público específico (PM/PO que querem usar IA agêntica sem depender de um dev pra isso). As habilidades do **PM Skill Pack** aplicam a mesma metodologia do toolkit de forma autônoma — o próprio Claude Code decide quando usar, lê o código com suas próprias ferramentas, e só para pra perguntar o que realmente precisa de confirmação humana.

| Pasta / Arquivo | Conteúdo | Pra quem |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| [`guia-instalacao/`](guia-instalacao/01-instalar-windows.md) | Passo a passo de instalação do Claude Code (Windows e Mac) e primeiros passos | Qualquer pessoa, mesmo sem experiência técnica |
| [`skills/code-discovery/`](skills/code-discovery/SKILL.md) | A skill real do Claude Code (`SKILL.md`). Gera relatórios em Markdown padrão ou Obsidian Flavored. | Quem já tem o Claude Code instalado |
| [`GLOSSARIO.md`](GLOSSARIO.md) | Glossário completo de IA agêntica, Discovery Técnico e Gestão de Produtos | PMs, POs, Tech Leads e Agilistas |

## Glossário

Para uma visão detalhada com todos os termos técnicos de IA (LLM, Agentes, RAG, CoVE, Approval Gates) e Discovery de Produto (Débito Técnico, Código Morto, Regras Ocultas), consulte o nosso **[Glossário Completo (`GLOSSARIO.md`)](GLOSSARIO.md)**.

- **Claude Code**: ferramenta agêntica da Anthropic que roda no terminal/desktop e analisa repositórios locais de forma autônoma.
- **Skill**: pasta contendo um arquivo `SKILL.md` que ensina a IA a executar uma tarefa específica com regras e formatos próprios.
- **Discovery Técnico**: processo de investigar regras de negócio e arquitetura em bases de código antes de planejar novas funcionalidades.

## Princípios (os mesmos do toolkit original)

As skills do pacote seguem exatamente os mesmos princípios do Code Discovery Toolkit: não inventar conclusões sem evidência, não refatorar ou alterar código sem autorização explícita, e não sair do escopo que foi confirmado com a pessoa.

---

## ⚖️ Por que Claude Code vs ChatGPT Web vs Cursor?

Se você é PM, escolher a ferramenta certa para cada momento acelera o seu dia de trabalho:

| Critério | 🤖 Claude Code (CLI) | 💬 ChatGPT / Claude Web | 💻 Cursor / VS Code |
|---|---|---|---|
| **Como lê o código** | **Autônomo (Local):** Ele busca, entra nas pastas e lê sozinho os arquivos necessários. | **Manual:** Você precisa copiar e colar os arquivos ou subir arquivos zipados. | **IDE Completa:** Roda dentro de uma interface de desenvolvedor. |
| **UX para o PM** | **Terminal Conversacional:** Sem menus complexos. Basta digitar comandos e conversar. | **Interface de Chat:** Simples, mas cansativa para repositórios grandes. | **Curva de Aprendizado:** Média/Alta. Pode assustar quem não usa IDEs. |
| **Limites de Token** | **Otimizado:** Varreduras inteligentes economizam tokens e evitam estourar a memória. | **Desperdício:** Enviar arquivos inteiros consome sua cota rapidamente. | **Variável:** Depende do indexador e das configurações da IDE. |
| **Segurança (Alterar Código)** | **Sob Controle:** Roda no seu terminal local. Você precisa aprovar manualmente comandos de escrita. | **Total:** Não tem acesso físico ao seu computador ou repositório para alterar arquivos. | **Risco de Escrita:** Pode alterar ou corromper arquivos facilmente com um clique errado se não tomar cuidado. |
| **Privacidade dos Dados** | **Alta:** Dados trafegam via API da Anthropic. Contas comerciais/API não usam seus dados para treinar modelos por padrão. | **Atenção (Risco):** Chats em contas gratuitas/comuns usam suas mensagens para treinar a IA, trazendo risco de vazamento de segredos comerciais. | **Configurável:** Permite ativar o "Privacy Mode" nas configurações para evitar que seu código seja enviado para treinamento. |

---

## ⚡ Cheat Sheet de Prompts Rápidos para PMs

Depois de instalar o **PM Skill Pack**, você pode usar estes comandos diretamente no Claude Code:

| Objetivo de Produto | O que digitar no Claude Code | Skill Ativada |
|---|---|---|
| Mapear um repositório abandonado | `"Faz um discovery completo desse projeto"` | `code-discovery` |
| Extrair regras de negócio | `"Quais as regras de validação e taxas ativas no checkout?"` | `business-rules-extractor` |
| Analisar impacto de nova feature | `"Se eu quiser criar um Pix Parcelado, o que afeta no código?"` | `feature-impact-analysis` |
| Avaliar débitos e gambiarras | `"Faça uma auditoria de débito técnico deste módulo"` | `tech-debt-evaluator` |
| Cruzar com documentos antigos | `"Use as PRDs da pasta /docs e cruze com o código atual"` | *(Todas as skills)* |

---

## Inspirações e referências

- [**obsidian-skills**](https://github.com/kepano/obsidian-skills) (Steph Ango) — skills de referência para sintaxe Obsidian (wikilinks, callouts, properties). A skill `code-discovery` deste repositório usa essa sintaxe na opção de relatório em Obsidian Flavored Markdown.
- [**skills**](https://github.com/anthropics/skills) (Anthropic) — especificação oficial do formato Skill e o `skill-creator`, cuja metodologia de testes de gatilho foi usada para refinar a `description` da skill `code-discovery` (veja `skills/code-discovery/evals/`).
-  [**agency-agents-app**](https://github.com/msitarzewski/agency-agents-app) — inspirou o template `AGENTS-discovery-template.md` disponível no [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit): o formato AGENTS.md e o conceito de "Approval Gates" foram adaptados para blindar o repositório investigado contra alterações não autorizadas em qualquer ferramenta agêntica compatível.

## Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.
[LinkedIn](https://linkedin.com/in/danilog-noleto)

## Licença

MIT — veja [`LICENSE`](LICENSE).
