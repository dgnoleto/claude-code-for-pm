# 🤖 Claude Code para PM/PO

Um guia de instalação e uma Skill real do Claude Code para times de produto que já usam (ou querem começar a usar) IA agêntica no dia a dia — sem precisar ser dev.

## Nunca usou Claude Code? Comece aqui

1. Veja o guia de instalação pro seu sistema: [Windows](guia-instalacao/01-instalar-windows.md) ou [Mac](guia-instalacao/02-instalar-mac.md).
2. Depois, siga [`03-primeiros-passos-claude-code.md`](guia-instalacao/03-primeiros-passos-claude-code.md) pra rodar o Claude Code dentro de um repositório clonado.
3. Por fim, [`04-instalar-a-skill.md`](guia-instalacao/04-instalar-a-skill.md) explica como instalar a skill `code-discovery` deste repositório, pra começar a usar de verdade.

## Esse repositório é irmão do Code Discovery Toolkit

Esse projeto nasceu do [Code Discovery Toolkit](https://github.com/SEU-USUARIO/code-discovery-toolkit) — um conjunto de prompts e metodologia para investigar repositórios esquecidos, que funciona com **qualquer IA** (ChatGPT, Gemini, Cursor, Claude, etc.).

Este repositório aqui é diferente de propósito: ele é centrado numa ferramenta específica (Claude Code) e num público específico (PM/PO que querem usar IA agêntica sem depender de um dev pra isso). A skill abaixo aplica a mesma metodologia do toolkit, mas de um jeito autônomo — o próprio Claude Code decide quando usar, lê o código com suas próprias ferramentas, e só para pra perguntar o que realmente precisa de confirmação humana.

## O que tem aqui

| Pasta | Conteúdo | Pra quem |
|---|---|---|
| `guia-instalacao/` | Passo a passo de instalação do Claude Code (Windows e Mac) e primeiros passos | Qualquer pessoa, mesmo sem experiência técnica |
| `skills/code-discovery/` | A skill real do Claude Code, no formato `SKILL.md` que a própria IA reconhece e aciona automaticamente | Quem já tem o Claude Code instalado |

## Glossário rápido

- **Claude Code**: uma ferramenta da Anthropic que roda no terminal (ou num app, se preferir interface gráfica) e consegue ler, entender e trabalhar com o código de um repositório de forma autônoma.
- **Skill**: uma pasta com um arquivo `SKILL.md` que ensina o Claude Code a fazer algo específico. A própria IA decide quando usar uma skill, com base na descrição dela — você não precisa "ativar" nada manualmente toda vez.
- **Terminal**: o programa de linha de comando (PowerShell no Windows, Terminal no Mac) onde você digita comandos em vez de clicar em botões.

## Princípios (os mesmos do toolkit original)

A skill segue exatamente os mesmos princípios do Code Discovery Toolkit: não inventar conclusões sem evidência, não refatorar ou alterar código sem autorização explícita, e não sair do escopo que foi confirmado com a pessoa.

## Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.
[LinkedIn](https://linkedin.com/in/danilog-noleto)

## Licença

MIT — veja [`LICENSE`](LICENSE).
