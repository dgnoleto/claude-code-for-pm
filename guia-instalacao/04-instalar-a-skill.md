# Instalar as skills

Escolha a tarefa na [página inicial](../README.md). Há nove skills; você pode instalar uma ou várias. Não é necessário ter um repositório de código para usar priorização ou preparar um briefing de protótipo.

## Pessoal ou por projeto

| Uso | Destino |
|---|---|
| Pessoal, disponível nos seus projetos | `~/.claude/skills/` |
| Compartilhado em um projeto | `.claude/skills/` na raiz desse projeto |

Copie **as pastas das skills desejadas que estão dentro de `skills/`**, não a pasta externa `skills` para dentro de outra pasta de mesmo nome. Copie cada pasta completa, inclusive `references/`, quando existir.

Exemplo de instalação pessoal:

```text
~/.claude/skills/
├── product-prioritization/
│   ├── SKILL.md
│   └── references/
│       └── metodos.md
└── product-prototyping/
    ├── SKILL.md
    └── references/
        └── ferramentas.md
```

No Windows, `~` normalmente corresponde a `C:\Users\SeuUsuario`; no Mac, a `/Users/SeuUsuario`. Não sobrescreva uma skill personalizada sem comparar a versão e preservar suas adaptações.

## Primeiro resultado

1. Copie [a entrada de priorização](../examples/priorizacao/entrada.md) para uma pasta de trabalho como `iniciativas.md`.
2. Abra Claude Code nessa pasta.
3. Peça: `Use product-prioritization para analisar iniciativas.md. Responda aqui, sem inventar dados ausentes.`
4. Confira se a resposta distingue itens comparáveis de itens sem dados e informa o período e as unidades.

Também é possível chamar diretamente `/product-prioritization` ou `/product-prototyping`. Se a skill não aparecer, confira o caminho `<destino>/<nome-da-skill>/SKILL.md`, as referências copiadas e abra uma sessão nova.

A seleção automática depende do modelo e da descrição; não é garantida por uma frase de exemplo. Para avaliar a qualidade, siga o [protocolo](../docs/avaliacao-de-respostas.md).

## Integrações opcionais

Instalar a skill de prototipação não instala Stitch, Figma ou servidores MCP. A skill pode produzir um briefing sem conexões externas ou construir um protótipo local quando solicitado. Consulte [os caminhos disponíveis](../skills/product-prototyping/references/ferramentas.md).

Fonte: [documentação oficial de skills do Claude Code](https://code.claude.com/docs/en/skills), consultada em 2026-09-23.
