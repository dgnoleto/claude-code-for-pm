# Instalar o Claude Code no Mac

## Requisitos

- macOS 13.0 ou mais recente.
- Pelo menos 4 GB de RAM.
- Conexão com a internet.
- Uma conta Claude paga (Pro, Max, Team ou Enterprise) — o plano gratuito do Claude.ai não dá acesso ao Claude Code.

## Passo 1 — Abrir o Terminal

Aperte `Cmd + Espaço`, digite `Terminal` e aperte Enter.

## Passo 2 — Instalar

Cole o comando abaixo no Terminal e aperte Enter:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

## Passo 3 — Confirmar que instalou

Ainda no terminal, digite:

```bash
claude --version
```

Se aparecer um número de versão, está instalado.

## Alternativa: Homebrew

Se você já usa o [Homebrew](https://brew.sh) no seu Mac, pode instalar assim:

```bash
brew install --cask claude-code
```

Importante: instalações via Homebrew não atualizam automaticamente — de vez em quando rode `brew upgrade claude-code` pra pegar as novidades.

## Prefere não usar terminal?

Existe um aplicativo Desktop do Claude Code, com interface gráfica — baixe em [claude.com/download](https://claude.com/download).

## Próximo passo

Siga para [`03-primeiros-passos-claude-code.md`](03-primeiros-passos-claude-code.md) para fazer login e rodar o Claude Code dentro de um repositório.

---
Fonte oficial e atualizada: [docs.claude.com/en/docs/claude-code/setup](https://docs.claude.com/en/docs/claude-code/setup)
