# Exemplo didático — MVP de reagendamento

Referência editorial, sem execução medida da skill e sem arquitetura validada em produção. Demonstra o fluxo atual de `system-bootstrap-architect`, cujo nome histórico foi preservado.

## Problema e hipótese

Clientes de uma assistência técnica precisam ligar para mudar um atendimento. Hipótese a avaliar: um fluxo de autoatendimento reduz a necessidade de contato. Não há baseline nem resultado medido neste exemplo.

## Primeiro recorte

- Consultar um atendimento e horários disponíveis.
- Escolher outro horário e confirmar a troca.
- Preservar a reserva original se a troca falhar.
- Informar indisponibilidade e alternativa de contato.

Fora desta primeira proposta: pagamentos, campanhas, múltiplos estabelecimentos e gestão completa da agenda.

## Regras a decidir

- Até quanto tempo antes o cliente pode reagendar?
- Como a pessoa comprova acesso ao atendimento?
- Quantas trocas são permitidas?
- Qual sistema é responsável pela disponibilidade?

Essas escolhas afetam o comportamento; não devem ser inventadas como política vigente.

## Proposta técnica condicionada

Se já existe serviço de agenda, avaliar sua API e a forma de reservar atomicamente o novo horário. Escolher um banco transacional, sozinho, não elimina duplo agendamento: é preciso definir a operação e testar concorrência.

Verificar acesso ao atendimento e proteger dados de contato. Multi-tenancy e RLS só entram se o contexto de clientes e armazenamento justificar. Não escolher infraestrutura adicional apenas para completar uma lista.

## Cenários de aceite para discussão

- Troca confirmada libera a reserva antiga conforme a regra acordada.
- Falha preserva a reserva original ou aciona recuperação explicitamente definida.
- Horário ocupado durante a operação não gera duas reservas.
- Pessoa sem acesso ao atendimento não consegue alterá-lo.

## Próximo passo

Confirmar regras com produto/operação e capacidade da API com engenharia. Prototipar o fluxo pode esclarecer entendimento antes da implementação real.

## ADR proposto

Status: proposto. Preferência inicial: reutilizar a agenda existente se sua API suportar o fluxo e as garantias necessárias. Alternativa: ampliar a API. Decisão pendente da investigação; nenhuma stack aprovada neste exemplo.
