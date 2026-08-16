# 🤖 Claude Code para PM/PO

Um guia de instalação e um conjunto de Skills reais do Claude Code para times de produto. Focado em **Discovery Técnico de Sistemas Legados** e no **Planejamento/Criação Segura de Sistemas do Zero (Vibe Coding)** — sem precisar ser dev.

## Nunca usou Claude Code? Comece aqui

1. Veja o guia de instalação pro seu sistema: [Windows](guia-instalacao/01-instalar-windows.md) ou [Mac](guia-instalacao/02-instalar-mac.md).
2. Depois, siga [`03-primeiros-passos-claude-code.md`](guia-instalacao/03-primeiros-passos-claude-code.md) pra rodar o Claude Code dentro de um repositório clonado.
3. Por fim, [`04-instalar-a-skill.md`](guia-instalacao/04-instalar-a-skill.md) explica como instalar o **PM Skill Pack** completo (7 skills) deste repositório.

## Esse repositório é irmão do Code Discovery Toolkit

Esse projeto nasceu do [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit) — um conjunto de prompts e metodologia para investigar repositórios esquecidos, que funciona com **qualquer IA** (ChatGPT, Gemini, Cursor, Claude, etc.).

Este repositório é diferente de propósito: centrado numa ferramenta específica (Claude Code) e num público específico (PM/PO que querem usar IA agêntica sem depender de um dev pra isso). As Skills do **PM Skill Pack** aplicam a mesma metodologia de forma autônoma — o próprio Claude Code decide quando usar, lê o código com suas próprias ferramentas, e só para para perguntar o que realmente precisa de confirmação humana.

| Pasta / Arquivo | Skill | O que faz | Pra quem |
|---|---|---|---|
| [`skills/system-bootstrap-architect/`](skills/system-bootstrap-architect/SKILL.md) | `system-bootstrap-architect` | Planeja, modela e arquiteta novos sistemas do zero (ou Vibe Coding) seguindo a metodologia rigorosa de 13 pontos. | Quem quer começar um projeto novo do jeito certo e seguro |
| [`skills/code-discovery/`](skills/code-discovery/SKILL.md) | `code-discovery` | Investiga, mapeia e documenta repositórios legados ou esquecidos. Gera relatórios em Markdown ou Obsidian. | Quem precisa entender um sistema antes de tocar nele |
| [`skills/business-rules-extractor/`](skills/business-rules-extractor/SKILL.md) | `business-rules-extractor` | Extrai regras de negócio ocultas no código e traduz para linguagem de produto, cruzando com documentação legada. | Quem precisa escrever PRDs ou critérios de aceite precisos |
| [`skills/feature-impact-analysis/`](skills/feature-impact-analysis/SKILL.md) | `feature-impact-analysis` | Analisa o impacto arquitetural de uma feature nova ou PRD antes do refinamento com o time de engenharia. | Quem quer entrar no refinamento com análise técnica pronta |
| [`skills/tech-debt-evaluator/`](skills/tech-debt-evaluator/SKILL.md) | `tech-debt-evaluator` | Audita débito técnico e traduz problemas de código em riscos de negócio e argumentos de ROI para stakeholders. | Quem precisa convencer a diretoria a investir em refatoração |
| [`skills/security-blind-spot-reviewer/`](skills/security-blind-spot-reviewer/SKILL.md) | `security-blind-spot-reviewer` | Revisa código ou especificações em busca de pontos cegos de segurança (OWASP, autenticação, exposição de dados). Não requer contexto de negócio. | Quem quer blindar uma feature antes de ir pro sprint |
| [`skills/spec-challenger/`](skills/spec-challenger/SKILL.md) | `spec-challenger` | Assume a persona de um dev sênior, arquiteto ou engenheiro e questiona a spec/PRD até que todas as pontas soltas sejam sanadas. | Quem quer estressar a spec antes de apresentar ao time |
| [`examples/exemplo-system-blueprint.md`](examples/exemplo-system-blueprint.md) | — | Exemplo completo de blueprint de arquitetura segura gerado com a metodologia de 13 pontos. | Quem quer ver um modelo pronto de especificação |
| [`guia-instalacao/`](guia-instalacao/01-instalar-windows.md) | — | Passo a passo de instalação do Claude Code (Windows e Mac) e primeiros passos. | Qualquer pessoa, mesmo sem experiência técnica |
| [`GLOSSARIO.md`](GLOSSARIO.md) | — | Glossário completo de IA agêntica, Discovery Técnico, Arquitetura e Gestão de Produtos. | PMs, POs, Tech Leads e Agilistas |

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
| Planejar um novo sistema do zero | `"Quero planejar a arquitetura de um novo SaaS de [tema]"` | `system-bootstrap-architect` |
| Mapear um repositório abandonado | `"Faz um discovery completo desse projeto"` | `code-discovery` |
| Extrair regras de negócio | `"Quais as regras de validação e taxas ativas no checkout?"` | `business-rules-extractor` |
| Analisar impacto de nova feature | `"Se eu quiser criar um Pix Parcelado, o que afeta no código?"` | `feature-impact-analysis` |
| Avaliar débitos e gambiarras | `"Faça uma auditoria de débito técnico deste módulo"` | `tech-debt-evaluator` |
| Revisar segurança antes do sprint | `"Revisa essa PRD por pontos cegos de segurança"` | `security-blind-spot-reviewer` |
| Estressar a spec antes do refinamento | `"Questiona essa spec como um dev backend sênior irritado"` | `spec-challenger` |
| Cruzar com documentos antigos | `"Use as PRDs da pasta /docs e cruze com o código atual"` | *(Todas as skills)* |

---

## 🏗️ A Metodologia de 13 Pontos de Criação Segura (Vibe Coding)

Quando iniciamos um sistema do zero — especialmente no modelo de **Vibe Coding** com agentes de IA —, é fácil gerar códigos rápidos que falham em boas práticas de engenharia e segurança. A skill `system-bootstrap-architect` obriga a IA a projetar e documentar a fundação estrutural do projeto em **13 pontos fundamentais** antes do desenvolvimento:

1. **PRD (Product Requirements Document):** Alinhamento claro de escopo e objetivos.
2. **UML & Mapa do Sistema:** Desenho de fluxos (Mermaid) mostrando quem conversa com quem.
3. **Matriz RBAC (Acessos):** Tabela mapeando permissões de cada perfil de usuário.
4. **Multi-tenancy:** Garantia técnica de isolamento por `tenant_id`.
5. **RLS (Row Level Security):** Proteção de acesso direto nas tabelas do banco de dados.
6. **Secrets Management:** Separação de chaves de API e senhas em arquivos `.env`.
7. **Modularidade & Feature Flags:** Arquitetura limpa com chaves liga/desliga de recursos.
8. **Error Reporting & Logs:** Botão de captura de logs e tela amigável de erro.
9. **Plano de Testes:** Definição de testes Unitários, Integração e E2E.
10. **Security Audit Gate:** Checklist automatizado de segurança antes do deploy.
11. **WAF & Rate Limiting:** Proteção de rede contra abusos e bots.
12. **HTTPS Strict (TLS/HSTS):** Criptografia rígida de ponta a ponta.
13. **ADR (Architecture Decision Record):** Registro do histórico de escolhas de tecnologia do projeto.

---

## Inspirações e referências

- [**obsidian-skills**](https://github.com/kepano/obsidian-skills) (Steph Ango) — skills de referência para sintaxe Obsidian (wikilinks, callouts, properties). A skill `code-discovery` deste repositório usa essa sintaxe na opção de relatório em Obsidian Flavored Markdown.
- [**skills**](https://github.com/anthropics/skills) (Anthropic) — especificação oficial do formato Skill e o `skill-creator`, cuja metodologia de testes de gatilho foi usada para refinar a `description` da skill `code-discovery` (veja `skills/code-discovery/evals/`).
- [**agency-agents-app**](https://github.com/msitarzewski/agency-agents-app) — inspirou o template `AGENTS-discovery-template.md` disponível no [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit): o formato AGENTS.md e o conceito de "Approval Gates" foram adaptados para blindar o repositório investigado contra alterações não autorizadas em qualquer ferramenta agêntica compatível.

## Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.
[LinkedIn](https://linkedin.com/in/danilog-noleto)

## Licença

MIT — veja [`LICENSE`](LICENSE).
