#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
navegacao.py — Liga as 103 fichas numa fila navegavel.

Faz duas coisas, as duas idempotentes:

  1. Gera template/fichas.js — a fila canonica (numero, titulo, caminho) lida
     de estrutura.py. E o unico lugar com dado; o comportamento (setas do
     teclado, arrastar no celular) vive em template/navegacao.js, que e fixo.
  2. Injeta, em cada ficha de guias/volNN/, as duas tags <script> antes de
     </body> — so onde ainda faltam.

Uso:
    python scripts/navegacao.py            # fichas.js + injeta nas fichas
    python scripts/navegacao.py --dados    # so regenera fichas.js

Chamado automaticamente por build.py (na galeria), para a fila nunca
desencontrar da estrutura canonica.
"""
import io, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estrutura import iter_guias, slug, RAIZ  # noqa

TAGS = ('<script src="../../template/fichas.js"></script>\n'
        '<script src="../../template/navegacao.js" defer></script>\n')


def fila():
    """[(num, titulo, Path)] na ordem canonica, so as fichas que existem."""
    saida = []
    for fase, vol, vtit, num, tit in iter_guias():
        p = RAIZ / f"guias/vol{vol:02d}/guia{num:03d}-{slug(tit)}.html"
        if p.exists():
            saida.append((num, tit, p))
    return saida


def gerar_dados(itens):
    dados = [{"n": num, "t": tit, "href": p.relative_to(RAIZ).as_posix()}
             for num, tit, p in itens]
    corpo = ",\n ".join(json.dumps(d, ensure_ascii=False) for d in dados)
    js = ("/* fichas.js — GERADO por scripts/navegacao.py a partir de "
          "scripts/estrutura.py.\n   Nao edite na mao: rode "
          "`python scripts/navegacao.py`. A fila alimenta\n   "
          "template/navegacao.js (setas do teclado e arrastar no celular). */\n"
          "window.FICHAS = [\n " + corpo + "\n];\n")
    destino = RAIZ / "template" / "fichas.js"
    io.open(destino, "w", encoding="utf-8", newline="\n").write(js)
    print(f"fichas.js: {len(dados)} fichas na fila")


def injetar(itens):
    tocadas = 0
    for num, tit, p in itens:
        s = io.open(p, encoding="utf-8").read()
        if "template/navegacao.js" in s:
            continue
        if "</body>" not in s:
            print(f"  !! guia {num:03d} sem </body> — pulado")
            continue
        s = s.replace("</body>", TAGS + "</body>", 1)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        tocadas += 1
    print(f"navegacao injetada em {tocadas} ficha(s)"
          f" ({len(itens) - tocadas} ja tinham)")


if __name__ == "__main__":
    itens = fila()
    gerar_dados(itens)
    if "--dados" not in sys.argv[1:]:
        injetar(itens)
