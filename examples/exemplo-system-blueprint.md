# 🗺️ Blueprint de Arquitetura — ClinicaSync SaaS (Multi-Tenant)

**Data de Concepção:** 2026-08-10
**Propósito:** SaaS multi-tenant para agendamento de consultas médicas e odontológicas voltado para clínicas e consultórios individuais.

---

## 1. PRD (Product Requirements Document)
- **Visão Geral:** Permitir que clínicas gerenciem sua agenda de médicos, pacientes e prontuários eletrônicos de forma autônoma.
- **Personas:**
  - *Dono da Clínica (Tenant Owner):* Administra planos, faturamento e acessos da equipe.
  - *Recepcionista (Manager):* Realiza agendamentos e cadastros de pacientes.
  - *Profissional de Saúde (Doctor):* Visualiza a própria agenda e edita prontuários.
  - *Paciente (End User):* Agenda consultas de forma online.

---

## 2. UML & Mapa do Sistema
```mermaid
sequenceDiagram
  autonumber
  Paciente->>+Frontend: Acessa rota pública /agendar
  Frontend->>+API Gateway: POST /api/v1/appointments (Auth + tenant_id no header)
  API Gateway->>+AppointmentController: Valida token e tenant_id
  AppointmentController->>+Database: Verifica disponibilidade e insere registro
  Database-->>-AppointmentController: Confirmação da transação
  AppointmentController-->>-API Gateway: Resposta HTTP 201 (Sucesso)
  API Gateway-->>-Frontend: Exibe confirmação na tela
  Frontend-->>-Paciente: Consulta confirmada
```

---

## 3. Matriz RBAC (Níveis de Acesso)
| Perfil | Recurso (Entidade) | Visualizar (Read) | Criar (Create) | Atualizar (Update) | Deletar (Delete) |
|---|---|---|---|---|---|
| Tenant Owner | Prontuário, Faturamento, Agenda | Sim (Geral) | Sim | Sim | Sim |
| Doctor | Prontuário, Agenda | Sim (Do Paciente) | Sim | Sim | Não |
| Manager | Agenda, Paciente | Sim (Geral) | Sim | Sim | Não |
| Paciente | Agenda (Própria) | Sim (Apenas sua) | Sim (Agendar) | Sim (Cancelar) | Não |

---

## 4. Multi-tenancy (Separação de Clientes)
- **Estratégia:** Banco de dados unificado com isolamento lógico via coluna `tenant_id` (tipo `UUID`) em todas as tabelas transacionais (`users`, `appointments`, `medical_records`).
- **Chave Composta:** Consultas ao banco sempre exigem filtro explícito `WHERE tenant_id = :tenant_id` para impedir vazamento cruzado de dados.

---

## 5. RLS (Row Level Security)
- **Implementação:** Uso de Row Level Security ativo no PostgreSQL.
- **Políticas de Acesso (Exemplo):**
  ```sql
  -- Ativa RLS nas tabelas críticas
  ALTER TABLE appointments ENABLE ROW LEVEL SECURITY;
  
  -- Cria política para garantir isolamento por tenant ativo na sessão
  CREATE POLICY tenant_isolation_policy ON appointments 
    FOR ALL 
    USING (tenant_id = current_setting('app.current_tenant_id', true));
  ```

---

## 6. Secrets Management (.env.example)
```bash
# Servidor e Banco
PORT=3000
DATABASE_URL="postgresql://user:password@localhost:5432/clinicasync?schema=public"

# Autenticação JWT (Assinatura digital)
JWT_SECRET="substitua_por_uma_hash_segura_de_32_caracteres"

# Gateway de Pagamentos (Stripe)
STRIPE_API_KEY="sk_test_..."
STRIPE_WEBHOOK_SECRET="whsec_..."

# Auditoria de Erros e Logs (Sentry)
SENTRY_DSN="https://..."
```

---

## 7. Arquitetura Modular & Feature Flags
- **Arquitetura:** Estrutura organizada por módulos isolados na pasta `/modules` (ex: `/auth`, `/appointments`, `/billing`, `/records`).
- **Feature Flags:**
  - `flag_prontuario_eletronico`: Libera ou bloqueia a edição de prontuários com base no plano contratado da clínica.
  - `flag_notificacao_whatsapp`: Habilita o disparo de lembretes automáticos de consulta no módulo de agendamento.

---

## 8. Error Reporting (Botão de Bug)
- **Frontend Boundary:** Componente `<ErrorBoundary>` encapsulando as rotas do dashboard. Em caso de falha, exibe tela amigável e captura automaticamente a pilha de erros (Stack Trace).
- **Botão de Suporte Rápido:** No menu lateral, um botão fixo de feedback de erro. Ao clicar, tira um print automatizado da tela (via `html2canvas`), captura os últimos logs do console e envia em lote para a fila do Sentry/Bugsnag.

---

## 9. Plano de Testes Automatizados
- **Unitários:** Validação de algoritmos de cálculo de horários vagos e regras de cálculo de faturamento (usando *Jest*).
- **Integração:** Inserção e leitura de dados no banco de testes validando se a rota `/api/v1/records` retorna dados bloqueados caso o `tenant_id` seja inválido.
- **E2E:** Fluxo completo do paciente acessando a tela de agendamento, escolhendo médico, inserindo dados e visualizando a confirmação (usando *Playwright*).

---

## 10. Security Audit Gate
- **Pipeline Check:**
  - Execução de `npm audit` ou `snyk test` no CI para travar deploys com dependências vulneráveis.
  - Verificação de rotas expostas sem middleware de autenticação (`npm run test:routes-auth`).

---

## 11. Proteção de Rede (WAF & Rate Limiting)
- **Cloudflare WAF:** Ativado em modo "Full Protection" com "Bot Fight Mode" habilitado para mitigar raspagem de dados de médicos e agendas por robôs.
- **Rate Limiting:** Máximo de 100 requisições por minuto por IP para rotas comuns, e máximo de 5 tentativas de login por minuto por IP nas rotas de autenticação.

---

## 12. HTTPS Strict (TLS/SSL + HSTS)
- **Segurança de Transporte:** Redirecionamento forçado de HTTP para HTTPS na Cloudflare.
- **HSTS (HTTP Strict Transport Security):** Ativado com cabeçalho rígido:
  `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`

---

## 13. ADR (Architecture Decision Record)

### ADR-001: Escolha do Banco de Dados e ORM

* **Status:** Aprovado
* **Data:** 2026-08-10
* **Decisão:** Usar PostgreSQL como banco relacional e Prisma como ORM.
* **Contexto:** Precisamos de um banco de dados ACID robusto para lidar com transações e agendamentos simultâneos sem risco de concorrência (duplo agendamento). O suporte nativo do PostgreSQL a Row Level Security (RLS) é fundamental para a governança de isolamento de dados das clínicas (multi-tenancy). O ORM Prisma simplifica a modelagem e mapeamento de chaves estrangeiras.
