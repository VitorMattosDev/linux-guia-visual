# PROMPT-INICIAL — Guia Visual Linux

Como produzir o projeto no Claude Code: **um volume por sessão**. Abra o Claude Code
com esta pasta (`GUIA VISUAL LINUX`) como diretório de trabalho e a pasta irmã
`manual-linux-master` acessível (é a fonte, só leitura). Cole o prompt do volume,
deixe rodar até o fim, dê `/clear` e cole o do próximo volume.

Antes de começar (uma vez): `/model opus`. E, se ainda não instalou o ambiente,
no Windows, `python -m pip install playwright pypdf && python -m playwright install chromium`
(o `--break-system-packages` é só para Linux).

---

## Prompt (modelo — troque o número do volume)

```
Você vai produzir o VOLUME {N} do Guia Visual Linux nesta sessão inteira.

Leia o CLAUDE.md deste repositório primeiro — ele é a autoridade sobre o fluxo,
o sistema de design (DESIGN.md / template/estilo.css) e a política editorial.
A ficha-demo pronta guias/vol03/guia020-permissoes-de-arquivo-leitura-escrita-e-execucao.html
é a referência de qualidade e densidade.

Regras da sessão:
- Cubra TODAS as fichas do Volume {N}, na ordem, sem parar no meio (só pare em erro real).
- Comece rodando:  python scripts/estrutura.py --vol {N}
  Isso lista cada ficha do volume com o HTML de destino e o capítulo-fonte a ler.
- Para cada ficha: leia o capítulo-fonte em ../manual-linux-master/, DESTILE numa única
  página A4 (não copie), preencha os blocos do template. Toda ficha tem Resumo Rápido,
  Dica de Ouro e o "🐉 No Kali". Comando destrutivo só dentro de bloco .perigo.
- Imagens: SVG/CSS vetorial como padrão; render realista só onde há hardware real.
  Nada de imagem que não ensina. Consistência entre as fichas acima de tudo.
- Commit por ficha: `guia NNN: <título>`, marcando [x] no ROADMAP.md no mesmo commit.
- Só a 1ª ficha do volume: renderize sozinha (python scripts/build.py <num>) como
  smoke test e confira a miniatura antes de seguir.
- No fim do volume: python scripts/build.py --vol {N}  (renderiza tudo, remonta o livro
  e a galeria). Valide as miniaturas em _saida/thumbs/ e faça o commit final
  `vol {N}: fecha volume`. Encerre — eu darei /clear para o próximo volume.

Se em algum ponto o contexto ficar perto de 80%, dê /compact e continue: o ROADMAP.md
guarda o progresso. Trabalhe de forma autônoma; não peça confirmação a cada passo.
```

---

## Volume 1 — pronto para colar

```
Você vai produzir o VOLUME 1 do Guia Visual Linux nesta sessão inteira.

Leia o CLAUDE.md deste repositório primeiro — ele é a autoridade sobre o fluxo,
o sistema de design (DESIGN.md / template/estilo.css) e a política editorial.
A ficha-demo pronta guias/vol03/guia020-permissoes-de-arquivo-leitura-escrita-e-execucao.html
é a referência de qualidade e densidade.

Regras da sessão:
- Cubra TODAS as fichas do Volume 1 (guias 001 a 007), na ordem, sem parar no meio
  (só pare em erro real).
- Comece rodando:  python scripts/estrutura.py --vol 1
  Isso lista cada ficha do volume com o HTML de destino e o capítulo-fonte a ler.
- Para cada ficha: leia o capítulo-fonte em ../manual-linux-master/, DESTILE numa única
  página A4 (não copie), preencha os blocos do template. Toda ficha tem Resumo Rápido,
  Dica de Ouro e o "🐉 No Kali". Comando destrutivo só dentro de bloco .perigo.
- Imagens: SVG/CSS vetorial como padrão; render realista só onde há hardware real.
  Nada de imagem que não ensina. Consistência entre as fichas acima de tudo.
- Commit por ficha: `guia NNN: <título>`, marcando [x] no ROADMAP.md no mesmo commit.
- Só a 1ª ficha (001): renderize sozinha (python scripts/build.py 1) como smoke test
  e confira a miniatura antes de seguir.
- No fim: python scripts/build.py --vol 1  (renderiza tudo, remonta o livro e a galeria).
  Valide as miniaturas em _saida/thumbs/ e faça o commit final `vol 1: fecha volume`.
  Encerre — eu darei /clear para o próximo volume.

Se em algum ponto o contexto ficar perto de 80%, dê /compact e continue: o ROADMAP.md
guarda o progresso. Trabalhe de forma autônoma; não peça confirmação a cada passo.
```

## Ordem dos volumes

1 → 2 → 3 (pule a 020, já pronta) → 4 · 5 → 6 → 7 → 8 · 9 → 10 → 11 → 12 ·
13 → 14 → 15 · 16. Feche cada fase antes de avançar. São 16 sessões no total.
