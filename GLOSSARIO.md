# 📚 Glossário de IA, Discovery Técnico & Engenharia Agêntica para PMs

Este glossário explica em linguagem didática e acessível todos os conceitos utilizados neste repositório — desde os termos do dia a dia de produto e engenharia até os **conceitos avançados de Inteligência Artificial Agêntica e Arquitetura que sustentam o Claude Code**.

---

## 🤖 1. Conceitos de Inteligência Artificial & Engenharia Agêntica

Estes conceitos explicam como ferramentas agênticas modernas (como o **Claude Code**) funcionam e por que este repositório impõe regras rígidas de segurança e governança.

### **Agente de IA (AI Agent / Autonomous Agent)**
* **O que é**: Diferente de um chat tradicional (onde você só conversa), um agente de IA possui **autonomia e ferramentas** para ler arquivos, executar comandos no terminal, pesquisar e tomar decisões em sequência para atingir um objetivo.
* **No Claude Code**: O Claude Code opera como um agente: ele navega sozinho pelas pastas do projeto, lê o código relevante e gera relatórios sem que você precise copiar e colar nada.

### **Skill (Habilidade do Agente)**
* **O que é**: Uma extensão padronizada (uma pasta contendo um arquivo `SKILL.md`) que ensina o agente de IA a realizar uma tarefa complexa seguindo uma metodologia específica.
* **No Claude Code**: A própria IA decide quando ativar uma skill com base na descrição dela. Neste repositório, a skill [`code-discovery`](skills/code-discovery/SKILL.md) ensina o Claude a fazer auditoria não-destrutiva de repositórios.

### **LLM (Large Language Model / Modelo de Linguagem de Grande Porte)**
* **O que é**: O "cérebro" de IAs como Claude (Anthropic) e ChatGPT (OpenAI), treinado em bilhões de textos e linhas de código para entender intenções humanas e lógica de programação.
* **No Claude Code**: O modelo por trás do Claude Code analisa a semântica do código para responder perguntas de produto e arquitetura.

### **Approval Gates (Gates Humanos de Aprovação)**
* **O que é**: Pontos de parada obrigatórios em um fluxo agêntico onde a IA é proibida de avançar sem a autorização explícita de uma pessoa.
* **No Claude Code**: A skill `code-discovery` impõe gates rígidos: a IA faz uma varredura leve, para e pergunta o escopo desejado. Ela só lê o código a fundo ou escreve o relatório após a sua aprovação.

### **Human-in-the-Loop (HITL / Humano no Controle)**
* **O que é**: Filosofia de design de IA onde o agente atua como assistente consultivo, mantendo o ser humano (neste caso, o PM ou Engenheiro) como responsável final pelas decisões e alterações no sistema.
* **No Claude Code**: O Claude Code sugere análises e recomendações, mas nunca altera código de produção ou toma decisões de produto sozinho.

### **Chain-of-Verification (CoVE / Cadeia de Verificação)**
* **O que é**: Técnica onde a IA é forçada a checar e tentar refutar suas próprias hipóteses antes de emitir um diagnóstico final, evitando "alucinações" (respostas inventadas).
* **No Claude Code**: A skill exige que para cada achado, a IA informe `arquivo:linha`, a evidência concreta e o nível de confiança (*Confirmado*, *Provável* ou *Hipótese*).

### **Janela de Contexto (Context Window) & Token Limits**
* **O que é**: A "memória de trabalho" máxima que uma IA consegue ler de uma só vez. Cada palavra ou caractere de código consome "tokens".
* **No Claude Code**: Para economizar os seus créditos de uso e evitar estourar o limite de memória, as skills fazem **varreduras leves** (mapeando a estrutura antes de ler arquivos inteiros).

### **RAG (Retrieval-Augmented Generation / Geração Aumentada por Recuperação)**
* **O que é**: A técnica de buscar informações em arquivos e documentos locais em tempo real antes de responder, em vez de depender apenas do conhecimento pré-treinado da IA.
* **No Claude Code**: O Claude Code faz RAG automático ao usar ferramentas como `Grep` e `Read` para consultar exatamente as linhas de código necessárias no seu repositório.

### **MCP (Model Context Protocol)**
* **O que é**: O padrão aberto universal criado pela Anthropic para conectar assistentes de IA diretamente a ferramentas, bancos de dados e APIs do computador de forma segura e padronizada.

### **Agente Somente Leitura (Read-Only Agent)**
* **O que é**: Um perfil de agente cujas capacidades de escrita e alteração de arquivos são desabilitadas ou bloqueadas por regras de sistema.
* **No Claude Code**: Garante que o discovery seja 100% não-destrutivo. O Claude lê o código para aprender, mas não modifica arquivos de produção.

---

## 🛠️ 2. Conceitos de Discovery Técnico & Gestão de Produtos Digitais

Termos práticos do dia a dia de Product Managers (PMs), Product Owners (POs), Tech Leads e Engenharia.

### **Discovery Técnico**
* **O que é**: O processo de investigar, auditar e mapear a arquitetura, regras de negócio ocultas e a saúde de um repositório de código antes de planejar novas funcionalidades, PRDs ou refatorações.

### **Débito Técnico (Technical Debt)**
* **O que é**: O custo acumulado de escolher soluções rápidas ou improvisadas no passado em vez de uma arquitetura limpa. Como um empréstimo financeiro, o débito técnico acumula "juros" na forma de lentidão, bugs frequentes e dificuldade de lançar novas features.

### **Código Morto (Dead Code)**
* **O que é**: Arquivos, funções, rotas de API ou telas que continuam existindo no repositório, mas não são mais utilizados por nenhum usuário ou sistema ativo. Gera confusão e atrasa o desenvolvimento.

### **Regras de Negócio Ocultas (Implicit Business Logic)**
* **O que é**: Regras de validação, taxas, descontos ou fluxos de trabalho que nunca foram documentados no Jira ou Confluence e existem **apenas dentro do código-fonte**. O Claude Code ajuda o PM a "escavar" e documentar essas regras.

### **Code Smells & Red Flags (Sintomas de Alerta)**
* **O que é**: Padrões no código que indicam problemas estruturais profundos de manutenção — como funções gigantescas, falta de tratamento de erros ou ausência de *timeouts* em chamadas externas.

### **Clean Code (Código Limpo)**
* **O que é**: Conjunto de boas práticas de escrita de código focadas em clareza, simplicidade e manutenibilidade por seres humanos.

### **Análise de Impacto de Feature**
* **O que é**: A avaliação prévia de quais partes da aplicação (tabelas, APIs, telas) serão afetadas ao criar uma nova funcionalidade, evitando efeitos colaterais indesejados no produto.

---

## 💻 3. Ferramentas do Ecossistema PM Tech-Savvy

### **Claude Code**
* **O que é**: A ferramenta da Anthropic executada via terminal ou app desktop que permite interagir com repositórios de código de forma agêntica e conversacional.

### **Terminal (PowerShell / Bash)**
* **O que é**: A interface de linha de comando do sistema operacional. No contexto deste repositório, é a "janela" onde você conversa com o Claude Code.

### **Obsidian Flavored Markdown**
* **O que é**: A sintaxe estendida usada pelo aplicativo de notas [Obsidian](https://obsidian.md). Inclui suporte a propriedades de metadados (`properties`), caixas de destaque (`callouts`) e links bidirecionais entre notas (`[[wikilinks]]`).

### **Git & Repositório**
* **Git**: O sistema de controle de versão que registra o histórico de alterações do código.
* **Repositório (Repo)**: A pasta organizada onde todo o código-fonte, configurações e documentação de um projeto ficam armazenados.

---

## 💡 Como usar este Glossário

- **Para PMs e POs**: Use este guia para dominar os termos técnicos ao negociar escopo e débito técnico com engenheiros e Tech Leads.
- **Para Tech Leads e Eng Managers**: Use como material de onboarding para ensinar times de produto a fazerem discovery autônomo e seguro usando IA.
- **Para Designers e Agilistas**: Use para entender as limitações técnicas e dependências de arquitetura durante o refinamento de histórias.
