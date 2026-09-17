# Avaliação de respostas das skills

Este protocolo avalia a utilidade e a correção da saída. Ele complementa os casos de gatilho existentes e não representa um benchmark já executado.

## Preparação

1. Escolha a skill e registre o commit, a versão da skill, a versão do Claude Code, o modelo, as permissões e a data.
2. Copie apenas [checkout.py](../examples/checkout-demo/checkout.py) e [politica-legada.md](../examples/checkout-demo/politica-legada.md) para uma pasta isolada.
3. Disponibilize a skill nessa sessão, seguindo o [guia de instalação](../guia-instalacao/04-instalar-a-skill.md). Não disponibilize o gabarito, este protocolo ou os testes ao modelo avaliado.
4. Faça a solicitação de extração sobre os dois arquivos, em uma sessão sem histórico anterior do exemplo. Confirme o escopo e a saída quando solicitado.
5. Salve prompt, confirmações, saída integral e erros. Não ajuste o resultado depois para fazê-lo coincidir com o gabarito.

## Critérios para business-rules-extractor

O revisor deve usar o [caso didático](../examples/exemplo-regras-de-negocio.md) como gabarito. A saída precisa:

- Identificar bloqueio apenas acima de 15% de oferta, teto de 10.000 centavos e descarte de frações de centavo.
- Distinguir os limites de frete por região e usar comparação estrita: igualdade não concede frete grátis.
- Apontar a divergência de 150 para 199 reais no Sudeste sem escolher arbitrariamente a política correta.
- Reconhecer que o arquivo não permite concluir a existência da expiração BEMVINDO em outro módulo.
- Citar arquivos e linhas verificáveis na versão analisada.
- Respeitar o escopo e não implementar uma correção.

Avalie cada item como **atendido**, **parcial** ou **não atendido**, com trecho da resposta e justificativa. Uma afirmação inventada sobre comportamento externo deve ser registrada mesmo quando os demais itens foram atendidos.

## Registro de uma rodada

| Campo | Preencher após execução |
|---|---|
| Data, base e commit | Identificação do material |
| Skill e versão | Versão efetivamente carregada |
| Ferramenta e modelo | Configuração efetiva |
| Prompt e confirmações | Texto integral |
| Saída | Arquivo ou link acessível ao revisor |
| Critérios atendidos/parciais/não atendidos | Contagem com denominador explícito |
| Afirmações sem evidência | Lista com trechos |
| Omissões | Lista com evidência esperada |
| Tempo, tokens e custo | Medidos separadamente; indisponível quando não coletado |
| Revisor e limitações | Escopo real da avaliação |

## Repetição e limites

Repita em sessões independentes e mantenha os resultados desfavoráveis. Para comparar versões de uma skill, fixe os outros fatores.

A demonstração é pequena e pública: pode servir de exercício, mas não sustenta conclusões gerais sobre sistemas reais. Antes de divulgar uma taxa de qualidade, amplie os casos, inclua ambiguidades e dependências ausentes e registre como as respostas foram julgadas.

Os testes Python verificam o comportamento do exemplo; os arquivos de gatilho verificam outro aspecto. Nenhum dos dois substitui executar e revisar a resposta da skill.
