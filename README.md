# Claude Code for PM

**Fluxos práticos de trabalho de produto com Claude Code: priorizar iniciativas, prototipar soluções e preparar decisões e entregas.**

Para PMs e POs que querem trabalhar com IA sobre seus materiais e problemas do dia a dia. Comece pela tarefa que precisa concluir. As skills ajudam a esclarecer o contexto, aplicar métodos quando fazem sentido e produzir artefatos revisáveis.

Não é necessário ter código para começar. Uma lista de iniciativas, um problema de usuário ou um rascunho de requisitos já pode ser a entrada.

## O que você precisa fazer hoje?

| Situação | Skill | Resultado esperado |
|---|---|---|
| Escolher iniciativas ou negociar o escopo de uma entrega | [product-prioritization](skills/product-prioritization/SKILL.md) | Comparação com RICE ou MoSCoW, premissas, lacunas e recomendação |
| Tornar uma ideia testável antes de desenvolver | [product-prototyping](skills/product-prototyping/SKILL.md) | Briefing, protótipo ou material para a ferramenta escolhida e roteiro de avaliação |
| Questionar uma especificação antes do refinamento | [spec-challenger](skills/spec-challenger/SKILL.md) | Bloqueadores, decisões adiáveis e resumo do que foi esclarecido |
| Definir um novo produto e seu MVP | [system-bootstrap-architect](skills/system-bootstrap-architect/SKILL.md) | Escopo, regras, perguntas abertas e proposta técnica proporcional ao contexto |
| Entender regras existentes antes de mudá-las | [business-rules-extractor](skills/business-rules-extractor/SKILL.md) | Regras rastreáveis, divergências e decisões pendentes |
| Antecipar consequências de uma mudança | [feature-impact-analysis](skills/feature-impact-analysis/SKILL.md) | Dependências, riscos e cenários para refinamento |
| Discutir um investimento em manutenção | [tech-debt-evaluator](skills/tech-debt-evaluator/SKILL.md) | Evidências e alternativas; dados necessários para avaliar retorno |
| Revisar requisitos e possíveis lacunas de segurança | [security-blind-spot-reviewer](skills/security-blind-spot-reviewer/SKILL.md) | Questões e achados para revisão especializada |

[code-discovery](skills/code-discovery/SKILL.md) permanece como apoio opcional para quem precisa entender uma base existente. As nove skills funcionam individualmente; não é necessário executar uma sequência inteira.

## Experimente dois fluxos

### Priorizar com dados incompletos

> Use product-prioritization. Precisamos melhorar a ativação neste trimestre. Tenho três iniciativas no arquivo iniciativas.md. Verifique se RICE faz sentido, mostre o que falta e compare apenas os itens com dados suficientes. Não invente alcance nem esforço. Responda aqui.

Comece pelo [exercício de priorização](examples/priorizacao/entrada.md). A [referência editorial](examples/priorizacao/referencia.md) permite conferir os cálculos e os limites, mas não deve ser mostrada ao modelo em uma avaliação.

### Prototipar para aprender

> Use product-prototyping. Quero testar se uma pessoa consegue reagendar um atendimento sem ligar para o suporte. Use o contexto em briefing.md. Prepare um protótipo local simples com dados fictícios e um roteiro de avaliação. Antes de construir, esclareça somente as regras que impedem representar o fluxo.

Veja o [briefing de prototipação](examples/prototipacao/entrada.md). O caminho pode ser código local, um briefing para [Stitch](https://stitch.withgoogle.com/) ou uma integração disponível com Figma. Nenhuma integração é obrigatória. Consulte [ferramentas e alternativas](skills/product-prototyping/references/ferramentas.md).

## Como começar

1. Configure Claude Code pelo guia de [Windows](guia-instalacao/01-instalar-windows.md) ou [Mac](guia-instalacao/02-instalar-mac.md).
2. [Instale apenas as skills desejadas](guia-instalacao/04-instalar-a-skill.md).
3. Abra Claude Code na pasta com os materiais que você tem autorização para usar; siga os [primeiros passos](guia-instalacao/03-primeiros-passos-claude-code.md).
4. Informe o problema, a decisão desejada e suas restrições. Pode pedir a resposta na conversa ou um arquivo.
5. Confira fontes, premissas e lacunas antes de usar a saída para decidir.

## Métodos e ferramentas têm papéis diferentes

- **Tarefas:** priorizar, prototipar, definir escopo e preparar refinamento.
- **Métodos:** RICE e MoSCoW apoiam decisões diferentes; a skill explica a escolha e respeita um método já definido pelo time.
- **Ferramentas:** Claude Code trabalha com os arquivos e recursos disponíveis. Integrações ampliam os caminhos, mas não substituem contexto nem validação com usuários.

**ROI e OKRs estão planejados, sem skills dedicadas nesta versão.** Veja o [plano de evolução](docs/EVOLUCAO.md). A análise de manutenção atual não equivale a um fluxo financeiro completo.

## Relação com o Code Discovery Toolkit

O [Code Discovery Toolkit](https://github.com/dgnoleto/code-discovery-toolkit) se concentra em investigar sistemas e levantar evidências técnicas.

O Claude Code for PM se concentra no trabalho cotidiano de produto. Código é uma fonte possível, junto a requisitos, dados e contexto de negócio. Quando uma tarefa exigir investigação ampla, use o Toolkit e traga seus achados como entrada, sem repetir toda a metodologia aqui.

## Estado da validação

As skills são instruções em linguagem natural; não garantem obediência do modelo, segurança, retorno financeiro ou qualidade da decisão. Exemplos são sintéticos e referências editoriais, não resultados de clientes nem execuções medidas do Claude Code.

Os casos de gatilho documentam quando acionar uma skill. Os testes Python verificam somente o checkout didático. O [protocolo de avaliação](docs/avaliacao-de-respostas.md) distingue essas verificações da avaliação de respostas e inclui os novos fluxos. Não há benchmark de qualidade publicado nesta versão.

## Documentação

- [Caso de regras de negócio](examples/exemplo-regras-de-negocio.md)
- [Mapeamento em Obsidian](examples/exemplo-code-discovery-obsidian.md)
- [Exemplo de planejamento de sistema](examples/exemplo-system-blueprint.md)
- [Glossário](GLOSSARIO.md)
- [Manutenção e contribuição](CLAUDE.md)
- [Mudanças de posicionamento e compatibilidade](docs/EVOLUCAO.md)

**Danilo Nolêto** — produto, discovery técnico, integrações e IA aplicada.  
[Perfil](https://github.com/dgnoleto) · [LinkedIn](https://www.linkedin.com/in/danilog-noleto)

Referências: [skills da Anthropic](https://github.com/anthropics/skills), [obsidian-skills](https://github.com/kepano/obsidian-skills) e [agency-agents-app](https://github.com/msitarzewski/agency-agents-app).

Licença MIT — [LICENSE](LICENSE).
