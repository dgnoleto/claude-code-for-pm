# Instalar o PM Skill Pack

O **PM Skill Pack** é um conjunto de 7 Skills do Claude Code, cada uma com uma responsabilidade única. Uma Skill é uma pasta com um arquivo `SKILL.md` dentro — o próprio Claude Code lê esse arquivo, entende quando deve usar aquela skill, e a aciona automaticamente quando você pedir algo relacionado.

## As 7 Skills do pacote

| Skill | O que faz |
|---|---|
| `system-bootstrap-architect` | Planeja a arquitetura de novos sistemas do zero (13 pontos) |
| `code-discovery` | Investiga repositórios legados ou esquecidos |
| `business-rules-extractor` | Extrai regras de negócio ocultas no código |
| `feature-impact-analysis` | Analisa impacto de novas features antes do refinamento |
| `tech-debt-evaluator` | Audita débito técnico e traduz em riscos de negócio |
| `security-blind-spot-reviewer` | Revisa pontos cegos de segurança em código ou specs |
| `spec-challenger` | Questiona sua spec como um dev sênior até sanear todas as pontas soltas |

## Onde instalar: pessoal vs. projeto

| Tipo | Onde fica | Quem tem acesso |
|---|---|---|
| **Pessoal** | `~/.claude/skills/` (pasta no seu usuário) | Só você, em qualquer repositório que abrir |
| **De projeto** | `.claude/skills/` (na raiz do repositório) | Todo mundo que clonar aquele repositório |

---

## Opção A — Instalar como skills pessoais (recomendado para começar)

1. Copie a pasta `skills/` deste repositório inteira.
2. Cole dentro de `~/.claude/skills/` no seu computador. Se essa pasta não existir, crie ela.
   - **Windows:** `C:\Users\SeuUsuario\.claude\skills\`
   - **Mac:** `/Users/SeuUsuario/.claude/skills/`
3. A estrutura final deve ficar assim:
   ```
   ~/.claude/skills/
   ├── system-bootstrap-architect/
   │   └── SKILL.md
   ├── code-discovery/
   │   └── SKILL.md
   ├── business-rules-extractor/
   │   └── SKILL.md
   ├── feature-impact-analysis/
   │   └── SKILL.md
   ├── tech-debt-evaluator/
   │   └── SKILL.md
   ├── security-blind-spot-reviewer/
   │   └── SKILL.md
   └── spec-challenger/
       └── SKILL.md
   ```
4. Se o Claude Code já estava rodando, execute `/clear` ou inicie uma sessão nova para ele reconhecer as skills novas.

---

## Opção B — Instalar como skills de projeto (para compartilhar com o time)

1. Dentro da pasta do repositório onde quer usar as skills (a raiz, onde fica o `.git`), crie a pasta `.claude/skills/` se não existir.
2. Copie as pastas das skills desejadas para dentro de `.claude/skills/`.
3. Faça commit e push — quem clonar o repositório já recebe as skills junto.

---

## Como confirmar que funcionou

Dentro de uma sessão do Claude Code, teste com frases naturais:

```
"Quero planejar a arquitetura de um novo SaaS de telemedicina."
→ Deve acionar: system-bootstrap-architect

"Ninguém lembra o que esse repositório faz. Pode investigar?"
→ Deve acionar: code-discovery

"Quais as regras de desconto ativas no checkout?"
→ Deve acionar: business-rules-extractor

"Se eu criar uma feature de Pix Parcelado, o que afeta no código?"
→ Deve acionar: feature-impact-analysis

"Faz uma auditoria de débito técnico nesse módulo."
→ Deve acionar: tech-debt-evaluator

"Revisa essa PRD por pontos cegos de segurança."
→ Deve acionar: security-blind-spot-reviewer

"Questiona essa spec como um dev backend sênior irritado."
→ Deve acionar: spec-challenger
```

Se alguma skill não for reconhecida, confirme se o arquivo está exatamente em `~/.claude/skills/<nome-da-skill>/SKILL.md` e reinicie a sessão do Claude Code.

## Instalando skills uma a uma

Se preferir instalar apenas algumas skills por enquanto, basta copiar só as pastas desejadas — cada skill funciona de forma independente e não depende das outras.
