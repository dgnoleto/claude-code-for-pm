# Instalar o Claude Code no Windows

Boa notícia: hoje em dia o Claude Code instala nativamente no Windows — não precisa mais configurar WSL (Linux dentro do Windows) pra usar. Esse guia segue o caminho mais simples.

## Requisitos

- Windows 10 (build 1809 ou mais recente) ou Windows 11.
- Pelo menos 4 GB de RAM.
- Conexão com a internet.
- Uma conta Claude paga (Pro, Max, Team ou Enterprise) — o plano gratuito do Claude.ai não dá acesso ao Claude Code.

## Passo 1 — Abrir o PowerShell

Aperte a tecla `Windows`, digite `PowerShell` e abra o "Windows PowerShell". Não precisa abrir como administrador.

## Passo 2 — Instalar

Cole o comando abaixo no PowerShell e aperte Enter:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Se aparecer o erro `'irm' is not recognized as an internal or external command`, você está no Prompt de Comando (CMD), não no PowerShell — veja a janela: se tiver escrito `PS C:\>`, é PowerShell; se for só `C:\>`, é CMD. Nesse caso, use este comando no lugar:

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

## Passo 3 — Confirmar que instalou

Ainda no terminal, digite:

```powershell
claude --version
```

Se aparecer um número de versão, está instalado.

## Passo 4 — Git para Windows (opcional, mas recomendado)

Instalar o [Git para Windows](https://git-scm.com/downloads/win) é opcional, mas recomendado: ele permite que o Claude Code use comandos no estilo Linux (Bash) em vez de só PowerShell, o que deixa algumas tarefas mais previsíveis. Se você seguiu nosso guia anterior e já instalou o Git (pra usar com o GitHub Desktop), você já tem isso.

## Alternativas de instalação

- Pelo WinGet: `winget install Anthropic.ClaudeCode`
- Prefere um programa com interface gráfica, sem terminal? Existe um aplicativo Desktop do Claude Code — baixe em [claude.com/download](https://claude.com/download).

## Próximo passo

Siga para [`03-primeiros-passos-claude-code.md`](03-primeiros-passos-claude-code.md) para fazer login e rodar o Claude Code dentro de um repositório.

---
Fonte oficial e atualizada: [docs.claude.com/en/docs/claude-code/setup](https://docs.claude.com/en/docs/claude-code/setup)
