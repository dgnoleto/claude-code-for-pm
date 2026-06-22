# Instalar a skill `code-discovery`

Uma Skill do Claude Code é só uma pasta com um arquivo `SKILL.md` dentro. O próprio Claude Code lê esse arquivo, entende quando deve usar aquela skill, e aciona ela automaticamente quando você pedir algo relacionado — sem precisar digitar nenhum comando especial.

Existem dois lugares onde uma skill pode morar, e a diferença importa:

| Tipo | Onde fica | Quem tem acesso |
|---|---|---|
| **Pessoal** | `~/.claude/skills/` (uma pasta no seu usuário) | Só você, em qualquer repositório que você abrir |
| **De projeto** | `.claude/skills/` (na raiz do repositório) | Todo mundo que clonar aquele repositório específico |

## Opção A — Instalar como skill pessoal (recomendado pra começar)

1. Copie a pasta `skills/code-discovery` deste repositório.
2. Cole dentro da pasta `~/.claude/skills/` no seu computador. Se essa pasta não existir ainda, crie ela.
   - No Windows, o caminho completo costuma ser algo como `C:\Users\SeuUsuario\.claude\skills\code-discovery`.
   - No Mac, costuma ser `/Users/SeuUsuario/.claude/skills/code-discovery`.
3. Se o Claude Code já estava rodando, rode `/clear` ou inicie uma sessão nova pra ele reconhecer a skill nova.

Pronto — a partir de agora, em qualquer repositório que você abrir com `claude`, a skill `code-discovery` vai estar disponível.

## Opção B — Instalar como skill de projeto (pra compartilhar com o time)

Se você quer que todo mundo que clonar um repositório específico já tenha essa skill disponível:

1. Dentro da pasta desse repositório (a raiz, onde fica o `.git`), crie a pasta `.claude/skills/` se ela não existir.
2. Copie a pasta `code-discovery` (de dentro de `skills/` neste repositório) para dentro de `.claude/skills/`.
3. Faça commit e push dessa pasta — assim, quando outra pessoa clonar o repositório, ela já recebe a skill junto.

## Como confirmar que funcionou

Dentro de uma sessão do Claude Code, peça algo que combine com o propósito da skill, por exemplo:

```
Esse repositório está abandonado e ninguém lembra o que ele faz. Pode investigar?
```

Se a skill foi reconhecida, o Claude Code deve seguir o fluxo dela: fazer uma varredura leve primeiro, e te perguntar o escopo antes de aprofundar — exatamente como os prompts do Code Discovery Toolkit fazem, só que de forma automática.

Se isso não acontecer, confira:
- Se o arquivo está exatamente em `.claude/skills/code-discovery/SKILL.md` (ou `~/.claude/skills/code-discovery/SKILL.md` pro modo pessoal).
- Se você iniciou uma sessão nova depois de copiar a pasta.
