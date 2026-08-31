# Guia Visual Linux & Shell

Fichas visuais de **consulta rápida** para os assuntos do *Manual de Linux e Shell
Scripting* — no estilo do guia visual de FTTH/Telecom: uma página A4 limpa e colorida
por assunto. **103 fichas · 16 volumes · 5 fases**, uma por capítulo do manual.

Produto final:
- **`_saida/guia-visual-linux.pdf`** — o livro único com todas as fichas.
- **`index.html`** — galeria HTML com busca, para consultar no navegador.

## Estrutura

```
GUIA VISUAL LINUX/
├── CLAUDE.md          # como o Claude Code trabalha aqui (leia primeiro)
├── DESIGN.md          # catálogo de blocos e paleta
├── ROADMAP.md         # fila autoritativa das 103 fichas + status
├── index.html         # galeria de consulta (gerada pelo build)
├── template/
│   ├── estilo.css     # sistema de design (todas as cores/medidas)
│   └── guia-template.html
├── guias/volNN/       # as fichas .html (uma por assunto)
├── assets/
│   ├── icones/        # SVGs compartilhados (logo, ícones)
│   └── img/           # imagens/renders por ficha
├── scripts/
│   ├── estrutura.py   # estrutura canônica → stubs e ROADMAP
│   ├── novo-guia.py   # cria UMA ficha do template
│   └── build.py       # renderiza PDFs + monta o livro + galeria
└── _saida/            # PDFs, miniaturas e o livro (gerado)
```

## Preparar o ambiente (uma vez)

```bash
pip install playwright pypdf --break-system-packages
playwright install chromium
```

## Uso

Produção com o Claude Code: **um volume por sessão** (veja `PROMPT-INICIAL.md`).

```bash
python scripts/estrutura.py --vol 1     # fila do Volume 1: fichas + capítulos-fonte
python scripts/build.py 1               # renderiza só a ficha 001 (smoke test)
# ...preencher as fichas do volume...
python scripts/build.py --vol 1         # renderiza o volume, remonta o livro + galeria
python scripts/build.py                 # renderiza TODAS + monta o livro PDF final
```

Referência de estilo e densidade: a ficha-demo pronta
**`guias/vol03/guia020-permissoes-de-arquivo-leitura-escrita-e-execucao.html`**.

O manual-fonte é a pasta irmã `../manual-linux-master/` (somente leitura).
