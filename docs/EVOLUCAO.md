# Evolução do Claude Code for PM

## Direção

O pacote ajuda PMs a executar tarefas de produto com Claude Code. Métodos apoiam essas tarefas; ferramentas e integrações são caminhos de execução. Uma nova skill deve explicar qual tarefa conclui, quais decisões exige e qual artefato deixa pronto.

O Code Discovery Toolkit continua sendo a referência para investigação ampla de sistemas. Aqui, código é uma fonte opcional. Não duplicar analisadores e metodologia de varredura.

## Esta revisão — 2026-09-23

- Adiciona priorização com RICE/MoSCoW e prototipação com alternativas locais, Stitch e Figma.
- Revisa as sete skills existentes: decisões proporcionais, evidências e aproveitamento do contexto fornecido.
- Preserva nomes e caminhos para não quebrar instalações; `system-bootstrap-architect` passa a começar pelo produto e MVP.
- Move a versão para `metadata.version`, um campo de metadados documentado pelo formato de skills. Atualiza os changelogs.
- Mantém os evals históricos existentes intactos. Mudanças de escopo exigem nova avaliação; os resultados antigos não comprovam os novos comportamentos.
- Não modifica o glossário nesta revisão.

## Próximos fluxos — ainda não disponíveis como skills

| Fluxo | Resultado pretendido | Condição para desenvolver |
|---|---|---|
| Avaliar investimento/ROI | Cenários, custos recorrentes, benefício incremental e premissas | Definir exemplos com horizonte e bases financeiras verificáveis, sem retorno garantido |
| Definir e acompanhar OKRs | Objetivos, resultados mensuráveis e rotina de revisão | Exemplos com baseline, fonte, responsável e distinção entre entrega e resultado |
| Sintetizar feedbacks | Evidências organizadas e perguntas para discovery | Dados de exemplo com origem, contexto e limites de representatividade |

## Critério para expansão

Antes de adicionar mais skills, avaliar os dois fluxos novos com entradas realistas, versões registradas e resultados desfavoráveis preservados. Comparar com uma solicitação equivalente sem skill. Não usar quantidade de skills como medida de utilidade.

## Compatibilidade e limites

Reinstale a pasta completa de cada skill atualizada, incluindo `references/` quando existir. As skills não dependem do CLAUDE.md deste repositório para seus comportamentos essenciais. Não há conexão MCP pré-instalada, publicação automática nem garantia de funcionamento em ferramentas diferentes do Claude Code.

Fonte do formato: [Claude Code — skills](https://code.claude.com/docs/en/skills), consultada em 2026-09-23.
