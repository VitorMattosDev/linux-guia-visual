#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
paginacao.py — a prova objetiva de que a ficha sai INTEIRA no PDF.

Substitui a antiga checagem "cada PDF tem 1 pagina", que era vazia: o
`.guia` tinha height fixa + overflow:hidden, entao o PDF SEMPRE saia com uma
pagina e o que passava de uma A4 era descartado em silencio. Hoje a ficha flui
pelas paginas que precisar, e o que se verifica e outra coisa:

  1. o rodape aparece no PDF  -> nada foi perdido;
  2. a ultima pagina nao esta quase vazia -> nao sobrou meia pagina de nada;
  3. nenhum bloco atomico foi partido ao meio pela quebra.

Orcamento por pagina (media=print): A4 = 1122,5 px a 96dpi, menos 12mm de
margem superior da @page = ~1077 px. Uma ficha ate 1077 px cabe em UMA pagina.
Passou disso, ela ocupa duas — o que e legitimo: melhor duas paginas cheias que
uma pagina cortada. O que nao vale e a segunda pagina levar so o rodape; nesse
caso aperte o respiro com `--gap-blocos` no <style> local da ficha.

Uso:
    python scripts/paginacao.py             # todas as fichas marcadas [x]
    python scripts/paginacao.py 84 20       # so estas
    python scripts/paginacao.py 84 --blocos # detalha bloco a bloco (ver abaixo)

O modo `--blocos` e a ferramenta de trabalho enquanto voce DESENHA a ficha: ele
lista a altura de cada filho direto do `.guia` e dos blocos internos que costumam
mandar na altura (o `.terminal`, as colunas do `.grade2`, o Resumo e a Dica).
Serve para saber ONDE cortar em vez de adivinhar. Dois padroes que aparecem toda
hora e so ficam visiveis aqui:

  - num grid de duas colunas, a coluna MAIS ALTA manda; encurtar a outra nao
    muda nada. Equilibre as duas (ou mexa na proporcao de `grid-template-columns`);
  - o Resumo e a Dica ficam sempre com a MESMA altura (sao celulas do mesmo grid),
    entao aparar so um dos dois nao encolhe o bloco: apare os dois.
"""
import glob
import io
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

PAG_PX = 1122.5                      # A4 297mm @96dpi
MARGEM_TOPO = 12 / 25.4 * 96         # @page { margin: 12mm 0 0 }
UTIL = PAG_PX - MARGEM_TOPO          # ~1077 px por pagina

# blocos que nao podem ser partidos ao meio (espelha o @media print do estilo.css)
ATOMICOS = (".topo,.cabecalho,.fluxo,.cards,.card,.duas-colunas,.coluna,.terminal,"
            ".perigo,.bloco,.rodape-blocos,.rodape,.secao-titulo,.regra,.nota")

JS = """(sel) => {
  const g = document.querySelector('article.guia');
  if (!g) return null;
  const base = g.getBoundingClientRect().top + window.scrollY;
  const blocos = [];
  document.querySelectorAll(sel).forEach(el => {
    const r = el.getBoundingClientRect();
    blocos.push([el.className || el.tagName.toLowerCase(),
                 r.top + window.scrollY - base, r.height]);
  });
  const filhos = [...g.children].map(el => [
    el.tagName.toLowerCase() + '.' + (el.className || '-'),
    Math.round(el.getBoundingClientRect().height)]);
  const dentro = [];
  for (const s of ['.terminal', '.grade2 > *', '.bloco', '.perigo', '.regra', '.nota'])
    document.querySelectorAll(s).forEach((el, i) =>
      dentro.push([s + '[' + i + ']', Math.round(el.getBoundingClientRect().height)]));
  return {alt: g.getBoundingClientRect().height, blocos, filhos, dentro};
}"""


def prontas():
    """Numeros marcados [x] no ROADMAP.md."""
    rm = RAIZ / "ROADMAP.md"
    if not rm.exists():
        return set()
    txt = io.open(rm, encoding="utf-8").read()
    return {int(m.group(1)) for m in re.finditer(r"- \[x\] \*\*guia (\d{3})\*\*", txt)}


def fichas(nums):
    for f in sorted(glob.glob(str(RAIZ / "guias" / "vol*" / "*.html"))):
        n = int(os.path.basename(f)[4:7])
        if nums is None or n in nums:
            yield n, f


def pdf_ok(num):
    """(paginas, rodape_presente) do PDF ja gerado; (None, None) se nao existe."""
    p = RAIZ / "_saida" / "pdf" / ("guia%03d.pdf" % num)
    if not p.exists():
        return None, None
    try:
        from pypdf import PdfReader
    except ImportError:
        return None, None
    r = PdfReader(str(p))
    txt = "".join(pg.extract_text() or "" for pg in r.pages)
    return len(r.pages), ("Guia Visual" in txt)


def main():
    detalhe = "--blocos" in sys.argv
    args = {int(a) for a in sys.argv[1:] if a.isdigit()}
    nums = args or prontas()
    if not nums:
        print("nada a verificar (nenhuma ficha [x] no ROADMAP)")
        return 0

    from playwright.sync_api import sync_playwright

    linhas, problemas = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.emulate_media(media="print")
        for num, f in fichas(nums):
            pg.goto("file://" + os.path.abspath(f))
            pg.wait_for_timeout(120)
            d = pg.evaluate(JS, ATOMICOS)
            if d is None:
                problemas.append((num, "sem <article class='guia'>"))
                continue
            alt = d["alt"]
            paginas = max(1, int(-(-alt // UTIL)))
            resto = alt - (paginas - 1) * UTIL      # quanto a ultima pagina usa
            ocup = 100.0 * resto / UTIL

            n_pdf, rodape = pdf_ok(num)
            if n_pdf is not None and not rodape:
                problemas.append((num, "PDF SEM RODAPE — conteudo perdido"))
            if paginas > 1 and ocup < 20:
                falta = alt - (paginas - 1) * UTIL
                problemas.append(
                    (num, "ultima pagina com %.0f%% — sobra so %.0f px; "
                          "aperte --gap-blocos ou corte %d px" % (ocup, falta, int(falta))))
            linhas.append((num, alt, paginas, ocup, n_pdf))

            if detalhe:
                falta = alt - UTIL if paginas == 1 else 0
                print("\nguia %03d — %.0f px de %.0f (%s)"
                      % (num, alt, UTIL,
                         "sobra %.0f px" % -falta if falta < 0 else "PASSOU %.0f px" % falta))
                print("  filhos diretos do .guia (o gap entre eles tambem custa):")
                for nome, h in d["filhos"]:
                    print("    %5d px  %s" % (h, nome[:64]))
                print("  blocos internos que costumam mandar na altura:")
                for nome, h in d["dentro"]:
                    print("    %5d px  %s" % (h, nome[:64]))
                print()
        b.close()

    print("%-5s %8s %5s %9s %6s" % ("ficha", "altura", "pag", "ult.pag", "pdf"))
    for num, alt, paginas, ocup, n_pdf in linhas:
        print("%-5d %7.0fpx %5d %8.0f%% %6s"
              % (num, alt, paginas, ocup, n_pdf if n_pdf is not None else "-"))

    import collections
    c = collections.Counter(l[2] for l in linhas)
    print("\n%d fichas | paginas por ficha: %s" % (len(linhas), dict(sorted(c.items()))))
    if problemas:
        print("\nPROBLEMAS (%d):" % len(problemas))
        for num, msg in problemas:
            print("  guia %03d: %s" % (num, msg))
        return 1
    print("OK: nenhuma ficha perde conteudo nem deixa pagina quase vazia.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
