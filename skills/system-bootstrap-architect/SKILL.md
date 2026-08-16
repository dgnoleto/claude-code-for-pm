---
name: system-bootstrap-architect
description: Use sempre que o usuário pedir para planejar, conceber, modelar ou arquitetar um novo projeto, sistema ou SaaS do zero (especialmente em contextos de Vibe Coding ou desenvolvimento rápido com IA). Esta skill força o planejamento estrutural seguro em 13 pontos (requisitos, banco, segurança, isolamento, auditoria e decisões) antes de gerar arquivos de código. Cobre pedidos como "quero iniciar um novo sistema de...", "planeja a arquitetura de um SaaS de...", ou "vamos começar um app do zero, por onde começo?".
---

# System Bootstrap Architect — Concepção Segura de Sistemas do Zero (13 Pontos)

Esta skill guia o usuário (PM, PO ou Dev) na criação de uma fundação arquitetural extremamente segura, robusta e escalável antes da escrita do código de programação, blindando projetos de "Vibe Coding" contra falhas graves de segurança e acoplamento.

## Princípios não negociáveis (valem durante toda a sessão)

- **Arquitetura Segura Primeiro:** Nunca pule etapas de segurança básica (como isolamento de tenants, RLS e RBAC) para codificar telas mais rápido.
- **Tradução Amigável:** Explique a arquitetura e banco de dados de modo didático que o PM e stakeholders de negócios entendam.
- **Estruturação por Fases:** Sempre gere o documento de Blueprint e ADR primeiro, obtenha a aprovação do usuário e só depois inicie a criação do código-fonte.

## Fluxo

### Etapa 1 — Coleta da Ideia do Produto

Pare e pergunte ao usuário:
"Qual é a ideia do novo produto ou SaaS que você deseja criar? Descreva brevemente o propósito dele (ex: um SaaS de agendamento de barbearias, um e-commerce multi-tenant de nicho, etc.)"

Espere a resposta antes de prosseguir.

### Etapa 2 — Confirmação de Diretório e Formato

Sugira salvar o planejamento em `arquitetura/AAAA-MM-DD-blueprint-<nome-sistema>.md`. Pergunte qual formato de saída ele prefere:
- **Markdown padrão:** Ideal para exportar para Notion, Confluence ou Wiki.
- **Obsidian Flavored Markdown:** Com properties (metadados), callouts e wikilinks.

Espere a confirmação do usuário antes de realizar a análise profunda.

### Etapa 3 — Elaboração do Blueprint Técnico (13 Pontos)

Analise a ideia proposta e elabore o documento de arquitetura cobrindo detalhadamente as seguintes frentes:

1. **PRD (Product Requirements Document):** Resumo do objetivo, personas e principais jornadas.
2. **UML & Mapa do Sistema:** Diagrama de sequência ou arquitetura textual em Mermaid (quem chama quem e onde o dado passa).
3. **Matriz RBAC (Níveis de Acesso):** Tabela mapeando perfis (ex: Dono, Administrador, Cliente) e suas permissões exatas de leitura/escrita.
4. **Multi-tenancy (Isolamento de Clientes):** Estratégia de uso de `tenant_id` nas tabelas e chaves primárias/estrangeiras.
5. **RLS (Row Level Security):** Modelo de políticas no banco de dados para travar o acesso físico aos dados por tenant ou usuário.
6. **Secrets Management (Gestão de Senhas):** Modelo de arquivo `.env.example` e lista de credenciais que nunca devem subir para o repositório.
7. **Arquitetura Modular & Feature Flags:** Catálogo de módulos independentes e chaves de controle (Rollout gradual).
8. **Erro Boundary & Logs:** Mecanismo de captura de erro na tela (botão de reportar bug que captura tela + logs) e fila de logs.
9. **Estratégia de Testes Automatizados:** Planos para testes unitários, testes de integração e testes de ponta a ponta (E2E).
10. **Security Audit Gate:** Lista de verificações de segurança antes do deploy (análise de vulnerabilidades).
11. **Escudo de Proteção (WAF & Rate Limiting):** Configuração recomendada de firewall e limites de requisições por IP para bloquear bots.
12. **HTTPS Strict (TLS/SSL + HSTS):** Configuração de segurança de transporte rígida (Full strict).
13. **ADR (Architecture Decision Record):** O registro oficial da decisão arquitetural que justifica a pilha tecnológica escolhida.

### Etapa 4 — Escrita do Blueprint

Escreva o Blueprint no caminho confirmado na Etapa 2.

**Modelo de Saída (Markdown Padrão):**

```markdown
# 🗺️ Blueprint de Arquitetura — [Nome do Sistema]

**Data de Concepção:** [data atual]
**Propósito:** [resumo da ideia]

## 1. PRD (Product Requirements Document)
- **Objetivo:** [...]
- **Personas principais:** [...]

## 2. UML & Mapa do Sistema (Diagrama Mermaid)
```mermaid
sequenceDiagram
  # Mapeamento do fluxo
```

## 3. Matriz RBAC
| Perfil | Entidade | Visualizar | Criar | Atualizar | Deletar |
|---|---|---|---|---|---|
| Dono | Faturamento | Sim | Sim | Sim | Sim |
| Gerente | Faturamento | Sim (do Tenant) | Não | Não | Não |

## 4. Multi-tenancy
- **Isolamento:** Uso de coluna `tenant_id` em todas as tabelas.

## 5. RLS (Row Level Security)
- **Política Postgres/Supabase:** `CREATE POLICY tenant_isolation_policy ON table FOR ALL USING (tenant_id = current_setting('app.current_tenant_id'));`

## 6. Secrets Management (.env.example)
- Exemplo de chaves estruturadas.

## 7. Módulos & Feature Flags
- Lista de módulos.

## 8. Error Reporting
- Fluxo do botão de reporte e captura de logs.

## 9. Plano de Testes
- Casos críticos para Unit, Integration e E2E.

## 10. Security Audit (Deployment Check)
- Lista de verificações.

## 11. Proteção de Rede (WAF & Rate Limiting)
- Parâmetros recomendados.

## 12. HTTPS Strict
- Exigências de TLS/HSTS.

## 13. ADR (Architecture Decision Record)
- **Status:** Proposto
- **Decisão:** [Ex: Usar Next.js + Supabase + PostgreSQL]
- **Contexto:** [Justificativa técnica e de produto]
```

Avise o usuário onde o Blueprint de criação foi salvo ao final da etapa.
