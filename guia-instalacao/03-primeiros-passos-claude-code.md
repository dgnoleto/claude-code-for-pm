# Primeiros passos com o Claude Code

Esse guia parte do princípio que você já instalou o Claude Code (veja o guia de [Windows](01-instalar-windows.md) ou [Mac](02-instalar-mac.md)) e que já sabe clonar um repositório (se não souber, é o mesmo processo que usamos com o GitHub Desktop no Code Discovery Toolkit).

## Passo 1 — Fazer login

Abra o terminal (PowerShell no Windows, Terminal no Mac) e digite:

```bash
claude
```

Na primeira vez, isso vai abrir o seu navegador pra você fazer login com sua conta Claude (Pro, Max, Team ou Enterprise). Depois de logar, volte pro terminal — a sessão já vai estar ativa.

## Passo 2 — Entrar na pasta do repositório

O Claude Code trabalha "dentro" da pasta onde você o inicia — ele lê e entende os arquivos daquela pasta específica. Por isso, antes de rodar `claude`, você precisa navegar até a pasta do repositório clonado.

No Windows (PowerShell), exemplo:

```powershell
cd D:\Github\code-discovery-toolkit
```

No Mac, exemplo:

```bash
cd ~/Github/code-discovery-toolkit
```

## Passo 3 — Iniciar o Claude Code nessa pasta

Ainda dentro da pasta, digite:

```bash
claude
```

Isso abre uma sessão interativa. Você vai ver um prompt esperando você digitar algo.

## Passo 4 — Fazer sua primeira pergunta

Dentro da sessão, digite algo simples pra testar, por exemplo:

```
Explique o que esse repositório faz, baseado no README.
```

O Claude Code vai ler os arquivos da pasta sozinho e te responder — sem você precisar copiar e colar nada manualmente, diferente do que fazemos com os prompts do Code Discovery Toolkit.

## Comandos úteis pra começar

- `/help` — lista os comandos disponíveis.
- `/clear` — começa uma conversa nova, limpando o contexto.
- `/exit` — sai da sessão do Claude Code.

## Um ponto de atenção importante

O Claude Code tem permissão pra ler e, se você autorizar, também editar arquivos do repositório onde ele está rodando. Antes de pedir qualquer alteração de código, vale sempre confirmar o que ele vai fazer — principalmente em repositórios de produção. Isso é o mesmo princípio de "não refatorar sem autorização" que já vimos no Code Discovery Toolkit, só que agora a IA tem ferramentas reais pra agir, não só pra sugerir.

## Próximo passo

Agora que o Claude Code está rodando, siga para [`04-instalar-a-skill.md`](04-instalar-a-skill.md) para instalar a skill `code-discovery` e começar a usar a metodologia de investigação de repositórios de forma autônoma.
