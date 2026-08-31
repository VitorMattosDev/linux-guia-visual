#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Renderiza as fichas e monta os artefatos de saída.

Gera, para cada guia HTML presente em guias/volNN/:
  _saida/pdf/guiaNNN.pdf     (uma página A4)
  _saida/thumbs/guiaNNN.png  (miniatura para a galeria)
E ao final:
  _saida/guia-visual-linux.pdf   (livro único, todos os guias na ordem)
  index.html                     (galeria HTML de consulta rápida)

Uso:
    python scripts/build.py            # tudo
    python scripts/build.py 20 12      # só os guias 20 e 12
    python scripts/build.py --vol 1    # todos os guias do Volume 1
    python scripts/build.py --galeria  # só regenera a galeria/index

Requer: playwright (chromium) e pypdf. Instale com:
    pip install playwright pypdf --break-system-packages && playwright install chromium
"""
import sys, re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUIAS = RAIZ / "guias"
SAIDA = RAIZ / "_saida"
sys.path.insert(0, str(RAIZ / "scripts"))
from estrutura import FASES, slug  # noqa

def todos_guias():
    """(num, titulo, fase, vol, path_html_ou_None) na ordem canônica."""
    for fase, vols in FASES:
        fase_n = fase.split("—")[0].replace("Fase","").strip()
        for vol, vtit, caps in vols:
            for num, tit in caps:
                p = GUIAS / f"vol{vol:02d}" / f"guia{num:03d}-{slug(tit)}.html"
                yield num, tit, fase_n, vol, (p if p.exists() else None)

def render(nums=None):
    from playwright.sync_api import sync_playwright
    (SAIDA/"pdf").mkdir(parents=True, exist_ok=True)
    (SAIDA/"thumbs").mkdir(parents=True, exist_ok=True)
    alvo = [g for g in todos_guias() if g[4] and (nums is None or g[0] in nums)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for num, tit, fase_n, vol, html in alvo:
            pg.goto("file://" + str(html.resolve())); pg.wait_for_timeout(300)
            pg.pdf(path=str(SAIDA/"pdf"/f"guia{num:03d}.pdf"), format="A4",
                   print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
            # A4 a 96dpi = 794x1123 px. Viewport menor CORTAVA a ficha (não reduzia):
            # tira a foto do próprio <article class="guia">, que é a página inteira.
            pg.set_viewport_size({"width":900,"height":1200})
            pg.wait_for_timeout(150)
            pg.locator("article.guia").screenshot(
                path=str(SAIDA/"thumbs"/f"guia{num:03d}.png"))
            print(f"  render guia {num:03d}")
        b.close()

def merge_livro():
    from pypdf import PdfWriter
    w = PdfWriter()
    n = 0
    for num, *_ in todos_guias():
        f = SAIDA/"pdf"/f"guia{num:03d}.pdf"
        if f.exists(): w.append(str(f)); n += 1
    if n:
        out = SAIDA/"guia-visual-linux.pdf"
        with open(out,"wb") as fh: w.write(fh)
        print(f"Livro montado: {out.name} ({n} guias).")

def prontos():
    """Números marcados [x] no ROADMAP.md — a verdade sobre o que está pronto
    (um stub existir em disco não significa ficha pronta)."""
    rm = RAIZ / "ROADMAP.md"
    if not rm.exists(): return set()
    return {int(m.group(1)) for m in
            re.finditer(r"- \[x\] \*\*guia (\d{3})\*\*", rm.read_text(encoding="utf-8"))}

def galeria():
    feitos = prontos()
    cards = []
    for num, tit, fase_n, vol, html in todos_guias():
        thumb = SAIDA/"thumbs"/f"guia{num:03d}.png"
        # "pronto" = marcado [x] no ROADMAP E com miniatura renderizada
        feito = (num in feitos) and thumb.exists() and html is not None
        link = str(html.relative_to(RAIZ)) if feito else "#"
        estado = "" if feito else " pend"
        img = (f'<img loading="lazy" src="_saida/thumbs/guia{num:03d}.png" alt="Guia {num:03d}">'
               if feito else '<div class="vazio">em breve</div>')
        cards.append(f'''<a class="c{estado}" href="{link}">
      <div class="tb">{img}</div>
      <div class="mt"><b>{num:03d}</b> {tit}<span>Vol {vol:02d} · Fase {fase_n}</span></div></a>''')
    html = GALERIA.replace("<!--CARDS-->", "\n    ".join(cards))\
                  .replace("<!--N-->", str(len(feitos)))
    (RAIZ/"index.html").write_text(html, encoding="utf-8")
    print(f"Galeria: index.html ({len(feitos)}/103 prontas)")

GALERIA = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guia Visual Linux — Consulta rápida</title>
<style>
 :root{--navy:#16336b;--azul:#1f6fd0}
 *{box-sizing:border-box;margin:0;padding:0}
 body{font-family:"Inter",system-ui,sans-serif;background:#eef2f7;color:#1f2b3a}
 header{background:linear-gradient(135deg,#16336b,#0f2547);color:#fff;padding:26px 22px}
 header h1{font-size:26px;letter-spacing:-.01em}header p{opacity:.85;margin-top:4px;font-size:14px}
 .busca{margin-top:14px}.busca input{width:100%;max-width:420px;padding:10px 14px;border:0;border-radius:8px;font-size:14px}
 .grade{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:16px;padding:22px}
 a.c{background:#fff;border-radius:10px;overflow:hidden;text-decoration:none;color:inherit;box-shadow:0 2px 8px rgba(20,40,80,.1);transition:.15s;display:flex;flex-direction:column}
 a.c:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(20,40,80,.18)}
 a.c.pend{opacity:.5;pointer-events:none}
 .tb{aspect-ratio:210/297;background:#f3f6fa;overflow:hidden;border-bottom:1px solid #e3e9f0}
 .tb img{width:100%;display:block}
 .vazio{height:100%;display:flex;align-items:center;justify-content:center;color:#9aa7b6;font-size:13px}
 .mt{padding:10px 12px;font-size:12.5px;line-height:1.35}
 .mt b{color:var(--azul)}.mt span{display:block;color:#7d8896;font-size:11px;margin-top:3px}
</style></head><body>
<header>
 <h1>Guia Visual Linux &amp; Shell</h1>
 <p>Consulta rápida · <!--N--> de 103 fichas prontas · uma ficha por assunto do manual</p>
 <div class="busca"><input id="q" placeholder="Buscar assunto, comando… (ex.: permissões, systemd, awk)"></div>
</header>
<main class="grade" id="grade">
    <!--CARDS-->
</main>
<script>
 const q=document.getElementById('q'),cs=[...document.querySelectorAll('a.c')];
 q.addEventListener('input',()=>{const t=q.value.toLowerCase();
   cs.forEach(c=>c.style.display=c.textContent.toLowerCase().includes(t)?'':'none')});
</script>
</body></html>'''

def nums_do_volume(vol):
    return {num for f, vols in FASES for v, vt, caps in vols if v == vol for num, t in caps}

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--galeria" in args:
        galeria()
    else:
        nums = set()
        resto = list(args)
        if "--vol" in resto:
            i = resto.index("--vol")
            nums |= nums_do_volume(int(resto[i+1]))
            del resto[i:i+2]              # consome "--vol N" para não recontar N como guia
        nums |= {int(a) for a in resto if a.isdigit()}
        render(nums or None)
        try: merge_livro()
        except Exception as e: print("merge pulado:", e)
        galeria()
