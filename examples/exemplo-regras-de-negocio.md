# Caso didático: do código de checkout às perguntas de produto

Esta demonstração usa [código fictício incluído no repositório](checkout-demo/checkout.py) e uma [política legada fictícia](checkout-demo/politica-legada.md). Os resultados abaixo são uma referência editorial conferível, não uma saída medida do Claude Code.

## 1. Problema e escopo

Um time precisa documentar as regras de cupom e frete antes de modificar o checkout. Existe uma política antiga, mas o comportamento implementado pode ser diferente.

Escopo: `desconto_cupom` e `frete_gratis` em `checkout-demo/checkout.py`. A demonstração presume entradas válidas; não representa um checkout completo.

## 2. Solicitação para a skill

> Use business-rules-extractor para analisar apenas examples/checkout-demo/checkout.py e comparar com examples/checkout-demo/politica-legada.md. Apresente regras observadas, referências ao código, divergências e perguntas de produto. Responda nesta conversa sem alterar arquivos. Não use os demais arquivos de exemplo como evidência do comportamento.

Para uma avaliação sem acesso ao gabarito, copie apenas o código e a política para uma pasta isolada antes de executar a skill. Veja o [protocolo](../docs/avaliacao-de-respostas.md).

## 3. Regras que a análise deve encontrar

| Regra observada | Evidência | Limite da conclusão |
|---|---|---|
| Cupom é bloqueado quando a maior oferta supera 15% | `desconto_cupom`, condição `maior_oferta_percentual > 15` | Exatamente 15% não bloqueia |
| O desconto de cupom é limitado a 10.000 centavos | `desconto_cupom`, chamada a `min` | Entradas inválidas não são tratadas nesta base |
| No Sudeste, frete grátis exige subtotal maior que 19.900 centavos | `frete_gratis`, escolha do limite e comparação `>` | Exatamente R$ 199,00 não dá frete grátis |
| Nas demais regiões, exige subtotal maior que 29.900 centavos | `frete_gratis` | Não há uma lista de regiões válidas |
| Desconto percentual descarta frações de centavo | `desconto_cupom`, divisão inteira `//` | A política não explica o arredondamento |

Todos os símbolos estão em [checkout.py](checkout-demo/checkout.py). Ao executar a skill, exija também referências às linhas da versão efetivamente analisada.

## 4. Divergências e informação insuficiente

A política legada indica frete grátis acima de R$ 150,00 para Sudeste; o código usa R$ 199,00. Isso comprova uma divergência entre os dois artefatos, sem determinar qual representa a intenção atual.

A política menciona expiração do cupom BEMVINDO. O arquivo analisado não recebe código do cupom nem data de cadastro. Não é possível concluir se essa validação existe em outro módulo.

## 5. Decisão proposta para discussão

Confirmar com o responsável pelo produto o limite vigente do frete e o local da validação do cupom BEMVINDO antes de especificar uma mudança.

Alternativas: atualizar a documentação, corrigir o código ou ampliar a investigação. Nenhuma dessas alternativas deve ser tratada como decisão já aprovada.

Critérios de aceite após a definição da política: valores abaixo, iguais e acima do limite devem ter comportamento explícito; aplicação de cupom com oferta de 15% e superior a 15% deve ser coberta; teto do desconto e arredondamento devem estar documentados.

## 6. Confira o comportamento da base

Na raiz do repositório, usando Python 3.11+:

```bash
python -m unittest discover -s examples/checkout-demo -p "test_*.py" -v
```

Os testes verificam a base sintética. Não executam uma skill, não acessam serviços externos e não medem precisão de IA.

## 7. Como avaliar a resposta da IA

Confira as cinco regras, a divergência e a lacuna sobre BEMVINDO. Registre omissões e afirmações sem evidência. Uma resposta que invente a implementação de expiração deve ser reprovada nesse critério, mesmo que esteja bem escrita.

Use o [protocolo de avaliação](../docs/avaliacao-de-respostas.md) para registrar modelo, versão, prompt, saída e revisão.
