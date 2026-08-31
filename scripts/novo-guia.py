#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
novo-guia.py — Cria (ou reabre) UM guia a partir do template, já preenchido
com número, título, volume e fase corretos. Use no início da sessão do guia.

    python scripts/novo-guia.py 12      # cria/garante o guia 012 e imprime o caminho
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from estrutura import iter_guias, slug, TEMPLATE, RAIZ

def main(num):
    for fase, vol, vtit, n, tit in iter_guias():
        if n == num:
            dest = RAIZ / f"guias/vol{vol:02d}/guia{n:03d}-{slug(tit)}.html"
            if not dest.exists():
                fase_n = fase.split("—")[0].replace("Fase","").strip()
                html = (TEMPLATE.read_text(encoding="utf-8")
                        .replace("GUIA NNN — Título", f"GUIA {n:03d} — {tit}")
                        .replace("Guia Visual NNN", f"Guia Visual {n:03d}")
                        .replace("Título do<br>Assunto", tit)
                        .replace(">103<", f">{n:03d}<")
                        .replace("Vol NN · Fase N", f"Vol {vol:02d} · Fase {fase_n}")
                        .replace('class="n">NNN<', f'class="n">{n:03d}<'))
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(html, encoding="utf-8")
                print("criado:", dest.relative_to(RAIZ))
            else:
                print("já existe:", dest.relative_to(RAIZ))
            print("Assunto:", tit, f"(Vol {vol:02d})")
            return
    print("guia não encontrado:", num)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("uso: python scripts/novo-guia.py <NNN>"); sys.exit(1)
    main(int(sys.argv[1]))
