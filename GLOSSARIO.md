# 📚 Glossário de IA, Discovery Técnico & Engenharia Agêntica para PMs

Este glossário explica em linguagem didática e acessível todos os conceitos utilizados neste repositório — desde os termos do dia a dia de produto e engenharia até os **conceitos avançados de Inteligência Artificial Agêntica, Arquitetura de Software e Gestão Ágil que sustentam o Claude Code**.

---

## 🤖 1. Conceitos de Inteligência Artificial & Engenharia Agêntica

Estes conceitos explicam como ferramentas agênticas modernas (como o **Claude Code**) funcionam e por que este repositório impõe regras rígidas de segurança e governança.

### **Agente de IA (AI Agent / Autonomous Agent)**
* **O que é**: Diferente de um chat tradicional (onde você só conversa), um agente de IA possui **autonomia e ferramentas** para ler arquivos, executar comandos no terminal, pesquisar e tomar decisões em sequência para atingir um objetivo.
* **No Claude Code**: O Claude Code opera como um agente: ele navega sozinho pelas pastas do projeto, lê o código relevante e gera relatórios sem que você precise copiar e colar nada.

### **Skill (Habilidade do Agente)**
* **O que é**: Uma extensão padronizada (uma pasta contendo um arquivo `SKILL.md`) que ensina o agente de IA a realizar uma tarefa complexa seguindo uma metodologia específica.
* **No Claude Code**: A própria IA decide quando ativar uma skill com base na descrição dela. Neste repositório, as skills do PM Pack (como a `code-discovery`) ensinam o Claude a fazer tarefas de produto de forma segura e não-destrutiva.

### **LLM (Large Language Model / Modelo de Linguagem de Grande Porte)**
* **O que é**: O "cérebro" de IAs como Claude (Anthropic) e ChatGPT (OpenAI), treinado em bilhões de textos e linhas de código para entender intenções humanas e lógica de programação.
* **No Claude Code**: O modelo por trás do Claude Code analisa a semântica do código para responder perguntas de produto e arquitetura.

### **Approval Gates (Gates Humanos de Aprovação)**
* **O que é**: Pontos de parada obrigatórios em um fluxo agêntico onde a IA é proibida de avançar sem a autorização explícita de uma pessoa.
* **No Claude Code**: As skills do PM Pack impõem gates rígidos: a IA faz uma varredura leve, para e pergunta o escopo desejado. Ela só lê o código a fundo ou escreve o relatório após a sua aprovação.

### **Human-in-the-Loop (HITL / Humano no Controle)**
* **O que é**: Filosofia de design de IA onde o agente atua como assistente consultivo, mantendo o ser humano (neste caso, o PM ou Engenheiro) como responsável final pelas decisões e alterações no sistema.
* **No Claude Code**: O Claude Code sugere análises e recomendações, mas nunca altera código de produção ou toma decisões de produto sozinho.

### **Chain-of-Verification (CoVE / Cadeia de Verificação)**
* **O que é**: Técnica onde a IA é forçada a checar e tentar refutar suas próprias hipóteses antes de emitir um diagnóstico final, evitando "alucinações" (respostas inventadas).
* **No Claude Code**: As skills exigem que para cada achado, a IA informe `arquivo:linha`, a evidência concreta e o nível de confiança (*Confirmado*, *Provável* ou *Hipótese*).

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

### **Prompt Engineering vs. Context Engineering (Engenharia de Contexto)**
* **O que é**: Enquanto *Prompt Engineering* foca na escrita da pergunta (instruções textuais), *Context Engineering* é o ato de fornecer os arquivos, estruturas, regras e limites certos para a IA não se perder em repositórios grandes.
* **No Claude Code**: O PM aprende que o segredo de usar o Claude Code no repositório não é só o "como perguntar", mas sim "quais arquivos e limites contextuais fornecer" para análise da IA.

### **Hallucination & Grounding (Alucinação & Ancoragem de Dados)**
* **Alucinação**: Ocorre quando a IA inventa informações plausíveis, mas falsas.
* **Grounding (Ancoragem)**: A prática de forçar a IA a responder baseando-se estritamente em evidências presentes no texto ou código fornecido.
* **No Claude Code**: As skills do PM Pack forçam a ancoragem exata exigindo rastro físico (`arquivo:linha`), evitando que a IA imagine uma funcionalidade que na realidade não existe no repositório.

---

## 🛠️ 2. Conceitos de Discovery Técnico, Arquitetura & Engenharia de Software

Conceitos essenciais de arquitetura e tecnologia para o PM entender onde a regra de negócio vive no repositório e debater de igual para igual com o time técnico.

### **Discovery Técnico**
* **O que é**: O processo de investigar, auditar e mapear a arquitetura, regras de negócio ocultas e a saúde de um repositório de código antes de planejar novas funcionalidades, PRDs ou refatorações.
* **No Claude Code**: O PM usa o Claude Code para liderar o discovery técnico de forma independente e com autonomia técnica.

### **Monólito vs. Microserviços**
* **Monólito**: Aplicação onde todo o código (telas, banco de dados, regras de negócio) fica em um único repositório e executa de forma unificada.
* **Microserviços**: Arquitetura que divide o sistema em múltiplos serviços menores e independentes (ex: serviço de pagamentos, serviço de catálogo) que se comunicam através da rede.
* **No Claude Code**: Ajuda o PM a saber se a busca por uma regra de negócio exige navegar em apenas um repositório local ou se precisará orientar o Claude a mapear chamadas para múltiplos repositórios e serviços de terceiros.

### **API (Application Programming Interface), Endpoints e Métodos HTTP**
* **O que é**: A API é a ponte de comunicação entre sistemas. Os *Endpoints* são as rotas de acesso (ex: `/api/v1/checkout`), e os *Métodos HTTP* definem a ação (GET para ler, POST para criar, PUT/PATCH para atualizar, DELETE para remover).
* **No Claude Code**: Ao analisar o código, o PM pode identificar as rotas exatas que a tela de um produto chama para entender o ciclo de vida dos dados e validar as regras que passam por elas.

### **Frontend vs. Backend**
* **Frontend**: A camada visual da aplicação com a qual o usuário interage diretamente (telas em React, HTML, CSS, app móvel).
* **Backend**: A camada de servidor, banco de dados e regras de negócio complexas.
* **No Claude Code**: Evita que o PM busque regras comerciais críticas apenas no código da tela (Frontend), orientando o Claude a verificar se essas validações também estão protegidas no servidor (Backend).

### **Webhooks & Event-Driven Architecture (Arquitetura Orientada a Eventos)**
* **O que é**: Mecanismos de comunicação assíncrona onde um sistema notifica outro automaticamente quando um evento ocorre (ex: o gateway de pagamento envia um webhook ao backend avisando que o Pix foi pago).
* **No Claude Code**: Ajuda o PM a mapear fluxos em segundo plano — aqueles onde a resposta da ação não é instantânea na tela, dependendo do retorno de um sistema externo.

### **Schema de Banco de Dados & Entidades**
* **O que é**: A estrutura e modelagem das tabelas do banco de dados, incluindo colunas, tipos de dados e relacionamentos (ex: a entidade *Cliente* se relaciona com várias entidades *Pedido*).
* **No Claude Code**: O PM pode pedir ao Claude para ler os arquivos de *migrations* ou entidades e listar quais dados o produto realmente armazena, validando a viabilidade técnica de gerar um novo relatório ou criar novos campos.

### **Banco de Dados Relacional (SQL) vs. Não-Relacional (NoSQL)**
* **SQL (Relacional)**: Armazena dados em tabelas estruturadas com relacionamentos formais e rígidos (ex: PostgreSQL, MySQL).
* **NoSQL (Não-Relacional)**: Armazena dados em estruturas flexíveis, comumente documentos no formato JSON (ex: MongoDB, DynamoDB).
* **No Claude Code**: Guia a IA a entender como as consultas são feitas e ajuda o PM a entender a complexidade de alterar ou migrar a estrutura de dados existente.

### **ORM (Object-Relational Mapping)**
* **O que é**: Uma biblioteca (ex: Prisma, TypeORM, Hibernate) que traduz tabelas do banco de dados em classes e objetos diretamente no código de programação.
* **No Claude Code**: Como o código moderno raramente usa SQL puro, saber que o sistema usa ORM guia o Claude a procurar as definições de dados nos arquivos de modelo (Models/Entities).

### **Testes Unitários, de Integração e End-to-End (E2E)**
* **Unitários**: Testam uma função ou comportamento isolado no código.
* **Integração**: Testam se dois ou mais módulos funcionam bem juntos (ex: backend acessando o banco de dados).
* **E2E (Ponta a Ponta)**: Simulam a jornada completa do usuário final na tela do produto.
* **No Claude Code**: O PM pode pedir para o Claude ler a pasta de testes para descobrir quais comportamentos e cenários de exceção o time de engenharia já homologou e quais regras carecem de cobertura.

### **Cobertura de Testes (Code Coverage)**
* **O que é**: A porcentagem do código-fonte que é executada pelos testes automatizados da aplicação.
* **No Claude Code**: Permite ao PM avaliar o risco técnico de priorizar e lançar novas alterações em áreas legadas com baixa cobertura de testes.

### **Feature Flags / Feature Toggles**
* **O que é**: Configurações de "chaves liga/desliga" no código que permitem ativar ou desativar uma funcionalidade em ambiente de produção sem a necessidade de lançar um novo deploy do sistema.
* **No Claude Code**: O PM pode usar o Claude para mapear quais feature flags estão ativas no código, planejando rollouts graduais e testes A/B integrados à engenharia de software.

### **CI/CD (Continuous Integration / Continuous Deployment)**
* **O que é**: A esteira automatizada que compila, testa e publica o código em ambientes de homologação ou produção sempre que os desenvolvedores aprovam alterações.
* **No Claude Code**: Permite ao PM prever e estimar o tempo real de publicação de uma correção ou feature a partir do momento em que o código é aprovado pelo time de engenharia.

### **Débito Técnico (Technical Debt)**
* **O que é**: O custo acumulado de escolhas rápidas ou improvisadas no passado em vez de uma arquitetura limpa. Como um empréstimo financeiro, o débito técnico acumula "juros" na forma de lentidão, bugs frequentes e dificuldade de lançar novas features.
* **No Claude Code**: O PM usa a skill `tech-debt-evaluator` para auditar de forma visual onde estão as piores seções de código e traduzir esse atraso em termos de ROI de refatoração para a gestão de negócios.

### **Código Morto (Dead Code)**
* **O que é**: Arquivos, funções, rotas de API ou telas que continuam existindo no repositório, mas não são mais utilizados por nenhum usuário ou sistema ativo. Gera confusão e atrasa o desenvolvimento.
* **No Claude Code**: O Claude Code localiza referências dessas funções no código local para verificar se elas de fato podem ser removidas com segurança.

### **Regras de Negócio Ocultas (Implicit Business Logic)**
* **O que é**: Regras de validação, taxas, descontos ou fluxos de trabalho que nunca foram documentados no Jira ou Confluence e existem **apenas dentro do código-fonte**.
* **No Claude Code**: O Claude ajuda o PM a "escavar" e documentar essas regras com a skill `business-rules-extractor`.

### **Code Smells & Red Flags (Sintomas de Alerta)**
* **O que é**: Padrões no código que indicam problemas estruturais profundos de manutenção — como funções gigantescas, falta de tratamento de erros ou ausência de *timeouts* em chamadas externas.
* **No Claude Code**: Identifica de forma preventiva riscos operacionais antes que o produto sofra com quedas ou falhas em produção.

### **Clean Code (Código Limpo)**
* **O que é**: Conjunto de boas práticas de escrita de código focadas em clareza, simplicidade e manutenibilidade por seres humanos.

### **Análise de Impacto de Feature**
* **O que é**: A avaliação prévia de quais partes da aplicação (tabelas, APIs, telas) serão afetadas ao criar uma nova funcionalidade, evitando efeitos colaterais indesejados no produto.

---

## 📋 3. Gestão de Produtos Digitais & Metodologias Ágeis

Termos práticos do dia a dia de gestão ágil de produto (Scrum, Kanban, metodologias tradicionais).

### **Product Discovery (Descoberta de Produto)**
* **O que é**: O processo contínuo de entender os problemas reais dos usuários, validar hipóteses e encontrar a solução correta antes de começar a codificar. Divide-se em *Discovery de Negócio* (desejo do usuário, valor comercial) e *Discovery Técnico* (viabilidade e riscos arquiteturais).
* **No Claude Code**: O Claude Code acelera o **Discovery Técnico**, permitindo que o PM valide a complexidade de banco de dados, regras de negócio atuais e APIs sem precisar esperar a agenda de um engenheiro de software.

### **Scrum & Sprint Planning**
* **O que é**: Scrum é um framework ágil para gestão e desenvolvimento de projetos de software baseados em ciclos rápidos de entrega (Sprints). A *Sprint Planning* é a reunião de planejamento das tarefas a serem executadas no ciclo.
* **No Claude Code**: Ao rodar a skill `feature-impact-analysis` antes da planning, o PM consegue entender quais arquivos e módulos serão alterados no código. Isso torna a estimativa de esforço (Story Points) do time de engenharia muito mais precisa e diminui o risco de atrasos.

### **User Story (História de Usuário) & Critérios de Aceite**
* **User Story**: Descrição informal de uma funcionalidade sob a perspectiva do usuário final (ex: *"Como um [papel], eu quero [ação] para [valor]"*).
* **Critérios de Aceite**: Regras claras que definem o comportamento esperado e as condições necessárias para que a história seja dada como concluída.
* **No Claude Code**: O PM pode cruzar a história de usuário com as regras extraídas pela skill `business-rules-extractor` para escrever critérios de aceite técnicos exatos baseados na realidade física do código atual, evitando critérios de aceite fictícios ou inviáveis.

### **PRD (Product Requirements Document / Especificação de Requisitos)**
* **O que é**: O documento de requisitos que reúne o propósito, escopo, regras de negócio e critérios de sucesso de uma funcionalidade.
* **No Claude Code**: O PM pode usar o Claude Code para ler o código legado e preencher a seção de "Requisitos Não Funcionais" ou "Especificações Técnicas" da PRD automaticamente, documentando dependências de banco de dados e APIs existentes.

### **BPMN (Business Process Model and Notation / Modelo e Notação de Processos de Negócio)**
* **O que é**: O padrão para modelagem visual de processos de negócio, representando graficamente o fluxo de tarefas, atores, decisões e eventos em diagramas (fluxogramas).
* **No Claude Code**: O Claude Code ajuda o PM a validar se o diagrama BPMN desenhado pela área de negócios realmente condiz com o fluxo de execução físico codificado nas APIs e controllers do repositório, identificando etapas manuais ou automáticas que divergiram do desenho.

### **Levantamento de Requisitos (Requirements Elicitation)**
* **O que é**: A atividade de mapear e coletar as necessidades dos clientes e stakeholders que devem ser atendidas pelo sistema.
* **No Claude Code**: O PM pode cruzar a entrevista com os stakeholders com o mapeamento feito pelo Claude no código atual. Isso permite identificar inconsistências antes mesmo do desenvolvimento começar, garantindo que novos requisitos não causem regressões ou quebra de lógicas existentes.

### **Caso de Uso (Use Case)**
* **O que é**: Um formato de especificação de requisitos que descreve uma sequência de interações entre um ator (usuário ou outro sistema) e a aplicação para atingir um objetivo específico.
* **No Claude Code**: A skill `business-rules-extractor` ajuda a "redescobrir" casos de uso implícitos no código legado, listando todos os fluxos de sucesso e fluxos alternativos (erros e exceções) programados nas rotas do sistema.

### **UML (Unified Modeling Language / Linguagem de Modelagem Unificada)**
* **O que é**: Linguagem visual padrão para modelagem e especificação de sistemas orientados a objetos (ex: Diagramas de Classes, Diagramas de Sequência e Casos de Uso).
* **No Claude Code**: O Claude Code pode ler o código do repositório e gerar um rascunho em formato textual (como *PlantUML* ou *Mermaid*) representando o diagrama de fluxo ou dependências, facilitando a visualização da arquitetura para PMs e designers.

### **Cenário de Teste (Test Scenario)**
* **O que é**: A descrição de um fluxo ou condição de uso do produto a ser testado para assegurar que ele funciona conforme o esperado em diversas situações (ex: "Testar checkout com cartão expirado").
* **No Claude Code**: O PM pode pedir para o Claude gerar uma lista exaustiva de cenários de teste (casos de sucesso, erros e regras de exceção) baseando-se estritamente nas condicionais (`if/else` e `catch`) mapeadas no código original.

### **Precificação (Pricing Engine / Regras Financeiras)**
* **O que é**: O conjunto de algoritmos, regras e regras fiscais que calcula o preço final de venda de um item, taxas, juros, descontos, frete e margens de lucro de um produto.
* **No Claude Code**: A extração de regras de precificação é uma atividade de altíssimo risco e valor. O PM pode usar a skill `business-rules-extractor` para auditar a pasta de serviços financeiros e garantir que as fórmulas de desconto ou taxas programadas estão em perfeita conformidade com as regras declaradas pela equipe de Marketing e Finanças.

### **Stakeholders (Partes Interessadas)**
* **O que é**: Qualquer pessoa ou área impactada pelo produto (clientes, diretores, time de vendas, marketing, jurídico).
* **No Claude Code**: Ao extrair regras de negócio ocultas do código (ex: regras de reembolso, elegibilidade ou segurança), o PM consegue apresentar ao jurídico e ao comercial o que o sistema *realmente* faz — não o que a documentação desatualizada diz — evitando promessas de entrega incompatíveis com a arquitetura atual.

### **Key User / Power User (Usuário-Chave)**
* **O que é**: Usuários finais que utilizam o produto com extrema frequência e dominam suas regras de uso, sendo essenciais para validar refinamentos de regras de negócio.
* **No Claude Code**: O PM pode cruzar os relatos do Key User ("o sistema faz X em tal situação") com o código mapeado pelo Claude, confirmando se esse comportamento está de fato programado ou se é um workaround que o usuário descobriu — o que são conclusões completamente diferentes para o backlog.

### **Priorização de Backlog (RICE / WSJF)**
* **O que é**: A atividade de ordenar os itens de trabalho com base em esforço, impacto, valor e urgência.
* **No Claude Code**: O PM pode estimar com maior precisão o parâmetro "Esforço/Complexidade" das fórmulas de priorização (como o RICE), utilizando a skill `feature-impact-analysis` para mapear de antemão quão complexa é a arquitetura daquela área do código.

### **Refinamento de Backlog (Backlog Refinement / Grooming)**
* **O que é**: O ritual de detalhar, estimar e fatiar itens do backlog de produto para deixá-los prontos para o desenvolvimento nas próximas Sprints.
* **No Claude Code**: O PM pode utilizar a IA durante o refinamento para tirar dúvidas de código locais em tempo real junto com o time, sem precisar que um desenvolvedor pare de codificar para abrir a IDE e pesquisar a lógica de uma rota.

### **MVP (Mínimo Produto Viável)**
* **O que é**: A versão mais simples de um produto ou funcionalidade que pode ser lançada para validar hipóteses de mercado com o menor esforço possível.
* **No Claude Code**: O Claude Code ajuda a mapear áreas modulares do código onde novas ideias podem ser "acopladas" de forma independente, evitando alterar o núcleo legado (monolítico) principal e acelerando o tempo de lançamento (time-to-market).

### **KPIs & OKRs (Métricas de Sucesso e Objetivos)**
* **KPIs (Indicadores-Chave de Performance)**: Métricas que avaliam o desempenho do produto.
* **OKRs (Objetivos e Resultados-Chave)**: Metodologia de metas para alinhar objetivos estratégicos aos resultados de produto.
* **No Claude Code**: O PM pode usar a IA para investigar quais tabelas e campos do banco de dados armazenam as informações cruciais (ex: receita, conversão de checkout, abandono de tela) para que o time de dados possa extrair as métricas de OKR/KPI corretamente.

### **QA (Quality Assurance) & UAT (Testes de Aceitação de Usuário)**
* **QA**: Atividade de garantir a qualidade do software através de testes antes do lançamento.
* **UAT**: Fase final de teste onde usuários de negócio validam se a feature funciona conforme as regras especificadas.
* **No Claude Code**: O PM pode gerar cenários de teste automatizados ou de UAT baseando-se nos fluxos descobertos pelas skills, garantindo que nenhum cenário de exceção do código original seja esquecido pelo time de QA.

### **SLA (Service Level Agreement) & SLO (Service Level Objective)**
* **SLA**: O acordo oficial de nível de serviço com o cliente (ex: o sistema de pagamento precisa ter 99,9% de uptime).
* **SLO**: A meta técnica interna que sustenta o SLA.
* **No Claude Code**: A skill `tech-debt-evaluator` ajuda o PM a auditar gargalos de performance e de latência no código (como queries pesadas) que colocam em risco o cumprimento do SLA.

### **PMBOK (Project Management Body of Knowledge)**
* **O que é**: O guia definitivo de melhores práticas para gerenciamento de projetos do PMI (Project Management Institute). Foca em gerenciamento de escopo, prazos, custos, qualidade, comunicação e riscos.
* **No Claude Code**: O Claude Code ajuda a materializar três pilares críticos do PMBOK em projetos de software: **Gerenciamento de Riscos** (mapeando gargalos em novas features), **Gerenciamento de Qualidade** (auditando débito técnico) e **Gerenciamento de Escopo** (evitando o aumento descontrolado de escopo ou *scope creep* por falta de entendimento técnico do código legado).

---

## 💻 4. Ferramentas do Ecossistema PM Tech-Savvy

Ferramentas práticas e configurações de ambiente de desenvolvimento.

### **Claude Code**
* **O que é**: A ferramenta da Anthropic executada via terminal ou app desktop que permite interagir com repositórios de código de forma agêntica e conversacional.

### **Terminal (PowerShell / Bash)**
* **O que é**: A interface de linha de comando do sistema operacional. No contexto deste repositório, é a "janela" onde você conversa com o Claude Code.

### **Obsidian Flavored Markdown**
* **O que é**: A sintaxe estendida usada pelo aplicativo de notas [Obsidian](https://obsidian.md). Inclui suporte a propriedades de metadados (`properties`), caixas de destaque (`callouts`) e links bidirecionais entre notas (`[[wikilinks]]`).

### **Git & Repositório**
* **Git**: O sistema de controle de versão que registra o histórico de alterações do código.
* **Repositório (Repo)**: A pasta organizada onde todo o código-fonte, configurações e documentação de um projeto ficam armazenados.

### **Arquivo .claudecode / .cursorrules / .github**
* **O que é**: Arquivos de configuração inseridos na raiz do repositório para definir diretrizes globais, regras arquiteturais, instruções de comportamento e limitações de contexto para assistentes de IA (como Cursor e Claude Code).
* **No Claude Code**: Permite ao PM ou líder do time blindar o comportamento do assistente antes de qualquer execução de tarefas.

---

## 💡 Como usar este Glossário

- **Para PMs e POs**: Use este guia para dominar os termos técnicos ao negociar escopo e débito técnico com engenheiros e Tech Leads.
- **Para Tech Leads e Eng Managers**: Use como material de onboarding para ensinar times de produto a fazerem discovery autônomo e seguro usando IA.
- **Para Designers e Agilistas**: Use para entender as limitações técnicas e dependências de arquitetura durante o refinamento de histórias.
