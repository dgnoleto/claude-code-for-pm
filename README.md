# Claude Code for PM

**Skills para transformar perguntas de produto em investigação técnica, regras de negócio e especificações revisáveis.**

Para PMs, POs e FDEs que trabalham com sistemas legados, integrações ou definição de novos produtos e querem aproximar decisões de negócio das evidências disponíveis no código.

O pacote reúne sete skills em português, guias de instalação e exemplos. O trabalho continua exigindo contexto de negócio, leitura crítica e validação com engenharia.

## Veja uma aplicação

Comece pelo [caso de regras de negócio](examples/exemplo-regras-de-negocio.md): código de demonstração, solicitação de análise, regras esperadas, divergência com uma especificação e decisão proposta.

O exemplo é didático e usa uma base fictícia incluída no repositório. Não representa um cliente, uma execução medida do Claude Code ou resultado em produção.

## As sete skills

| Necessidade | Skill | Saída esperada |
|---|---|---|
| Entender um sistema pouco documentado | [code-discovery](skills/code-discovery/SKILL.md) | Mapeamento, referências ao código e perguntas abertas |
| Recuperar regras de negócio | [business-rules-extractor](skills/business-rules-extractor/SKILL.md) | Regras, evidências e divergências com documentos |
| Avaliar uma nova funcionalidade | [feature-impact-analysis](skills/feature-impact-analysis/SKILL.md) | Dependências e riscos para discutir no refinamento |
| Priorizar débito técnico | [tech-debt-evaluator](skills/tech-debt-evaluator/SKILL.md) | Hipóteses de impacto e alternativas para decisão |
| Investigar possíveis lacunas de segurança | [security-blind-spot-reviewer](skills/security-blind-spot-reviewer/SKILL.md) | Achados para revisão técnica, sem certificação de segurança |
| Questionar uma especificação | [spec-challenger](skills/spec-challenger/SKILL.md) | Ambiguidades, exceções e perguntas para completar o escopo |
| Planejar um sistema novo | [system-bootstrap-architect](skills/system-bootstrap-architect/SKILL.md) | Proposta de estrutura e decisões a validar antes da construção |

## Comece a usar

1. Siga o guia de instalação para [Windows](guia-instalacao/01-instalar-windows.md) ou [Mac](guia-instalacao/02-instalar-mac.md).
2. Confira os [primeiros passos](guia-instalacao/03-primeiros-passos-claude-code.md) e o [guia de instalação das skills](guia-instalacao/04-instalar-a-skill.md).
3. Trabalhe em uma base que você tenha autorização para analisar. Defina escopo, destino dos relatórios e permissões da ferramenta.
4. Escolha uma pergunta pequena e confira as referências retornadas antes de ampliar a investigação.

Exemplo de solicitação:

> Use a skill business-rules-extractor para analisar apenas examples/checkout-demo/checkout.py e comparar com examples/checkout-demo/politica-legada.md. Apresente as regras observadas, as divergências e as perguntas de produto. Responda nesta conversa, sem alterar arquivos. Não presuma que a documentação antiga representa a política vigente.

As condições de acesso e instalação do Claude Code pertencem à ferramenta externa e podem mudar. Consulte sua documentação oficial ao configurar o ambiente.

## Como transformar a saída em trabalho de produto

1. **Pergunta:** qual decisão precisa ser tomada?
2. **Evidência:** em quais arquivos e comportamentos a análise se apoia?
3. **Incerteza:** o que o código não permite concluir?
4. **Alternativas:** corrigir, documentar, investigar mais ou manter?
5. **Validação:** quem confirma a regra e quais cenários comprovam a entrega?

Esse fluxo ajuda tanto na preparação de backlog quanto no entendimento de operações e soluções junto a clientes. Uma lista de achados só vira uma demanda implementável quando tem contexto, prioridade e critérios de aceite.

## O que está validado — e o que ainda precisa ser medido

| Material | O que permite verificar | O que não comprova |
|---|---|---|
| Arquivos SKILL.md | Escopo, instruções e formato de saída | Obediência garantida do modelo |
| Evals de gatilho e notas | Casos de acionamento e raciocínio de refinamento documentado | Qualidade da investigação ou benchmark automatizado |
| Exemplos | Estrutura de uma entrega e forma de citar evidências | Resultado obtido em cliente |
| Demonstração de checkout | Regras de uma pequena base sintética, com testes locais | Desempenho das skills no Claude Code |

Veja o [protocolo de avaliação de respostas](docs/avaliacao-de-respostas.md) para registrar uma execução, conferir regras esperadas e avaliar omissões e afirmações sem evidência. Resultados só devem ser publicados após execução e revisão.

## Limites de uso

As skills orientam comportamento por instruções em linguagem natural. Aprovações, permissões de escrita e isolamento precisam ser configurados na ferramenta e no ambiente; o texto de uma skill não implementa esses controles.

Uma investigação pode deixar de encontrar chamadas dinâmicas, dependências externas ou comportamentos de produção. O código também pode divergir da intenção do negócio. Registre essas lacunas e valide conclusões com as pessoas responsáveis.

A proposta de arquitetura da skill de bootstrap é um ponto de partida. Cada mecanismo sugerido deve ser justificado pelo problema, pelo risco e pelo custo de operação.

## Relação com o Code Discovery Toolkit

O [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit) oferece metodologia, prompts, templates e um analisador Python que pode ser executado localmente.

Este repositório organiza procedimentos em skills específicas para Claude Code. Os projetos são complementares: o toolkit ajuda a levantar sinais; as skills orientam investigação e documentação com IA.

## Outros exemplos e documentação

- [Mapeamento em Obsidian](examples/exemplo-code-discovery-obsidian.md).
- [Blueprint de sistema](examples/exemplo-system-blueprint.md).
- [Glossário](GLOSSARIO.md).
- [Regras de contribuição e manutenção](CLAUDE.md).

Ao propor mudanças, descreva a necessidade do usuário, um exemplo de entrada, a saída desejada e como avaliar se a alteração ajudou. Para modificar skills e avaliações existentes, siga as regras de manutenção do repositório.

## Autor e referências

**Danilo Nolêto** — produto, discovery técnico, integrações e IA aplicada.  
[Perfil](https://github.com/dgnoleto) · [LinkedIn](https://www.linkedin.com/in/danilog-noleto)

Referências: [skills da Anthropic](https://github.com/anthropics/skills), [obsidian-skills](https://github.com/kepano/obsidian-skills) e [agency-agents-app](https://github.com/msitarzewski/agency-agents-app).

Licença MIT — [LICENSE](LICENSE).
