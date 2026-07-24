# Instalar o PM Skill Pack (Skills para PMs)

Uma Skill do Claude Code é uma pasta com um arquivo `SKILL.md` dentro. O Claude Code lê estes arquivos automaticamente e decide qual skill acionar com base na sua pergunta — sem que você precise digitar nenhum comando especial.

Este repositório fornece um **PM Skill Pack** com 4 habilidades essenciais:
1. `code-discovery`: Mapeamento de repositórios legados/desconhecidos.
2. `business-rules-extractor`: Extração de regras de negócio ocultas no código.
3. `feature-impact-analysis`: Análise de impacto técnico de novas features antes do refinamento.
4. `tech-debt-evaluator`: Diagnóstico de débitos técnicos e tradução em riscos/ROI.

Existem dois locais onde uma skill pode morar:

| Tipo | Onde fica | Quem tem acesso |
|---|---|---|
| **Pessoal (Global)** | `~/.claude/skills/` (pasta no seu usuário do computador) | Só você, em qualquer repositório que abrir no terminal |
| **De Projeto (Local)** | `.claude/skills/` (na raiz do repositório investigado) | Todos do time que clonarem aquele repositório específico |

---

## Opção A — Instalar como skills pessoais (recomendado para uso diário)

Se você quer ter acesso a todas as 4 skills em qualquer projeto que abrir no seu computador:

1. **Localize a pasta de skills pessoais** no seu computador. Se ela não existir, crie-a:
   - **No Windows:** `C:\Users\SeuUsuario\.claude\skills\`
   - **No Mac:** `/Users/SeuUsuario/.claude/skills/`
2. **Copie as 4 pastas** que estão dentro da pasta `skills/` deste repositório (`code-discovery`, `business-rules-extractor`, `feature-impact-analysis`, `tech-debt-evaluator`).
3. **Cole todas elas** dentro da pasta `skills/` do seu computador. O resultado deve ser:
   - `~/.claude/skills/code-discovery/SKILL.md`
   - `~/.claude/skills/business-rules-extractor/SKILL.md`
   - `~/.claude/skills/feature-impact-analysis/SKILL.md`
   - `~/.claude/skills/tech-debt-evaluator/SKILL.md`
4. Se o Claude Code já estava rodando, execute `/clear` ou reinicie a sessão para carregar as novas skills.

---

## Opção B — Instalar como skills de projeto (para compartilhar com o time)

Se você deseja que todos os desenvolvedores e PMs que trabalham em um projeto específico usem o mesmo padrão de discovery e documentação:

1. Vá até a pasta raiz do repositório em que o time trabalha.
2. Crie a estrutura `.claude/skills/` na raiz do projeto (onde fica o arquivo `.git`).
3. Copie as pastas das skills deste repositório para lá.
4. Faça commit e push da pasta `.claude/` para o repositório Git do time.

---

## Como confirmar que funcionou

Inicie o Claude Code e pergunte algo que acione uma das habilidades do pacote:

```text
# Para testar a extração de regras
Quais as regras de validação aplicadas no checkout deste projeto?

# Para testar o impacto de feature
Se eu quiser adicionar pagamento por Pix parcelado, o que isso afeta?
```

Se a IA foi configurada corretamente, ela identificará a skill e seguirá o fluxo estruturado (como varredura leve, solicitação de documentos de apoio e confirmação de escopo) antes de aprofundar a análise.

Se a IA responder como um chat comum, certifique-se de que os arquivos `SKILL.md` estão localizados exatamente no caminho correto e que você reiniciou a sessão do Claude Code.

