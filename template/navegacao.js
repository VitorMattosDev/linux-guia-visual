/* ==========================================================================
   navegacao.js — Passar de ficha em ficha sem voltar à galeria.

   No notebook: setas <- e -> do teclado (Esc volta para a galeria).
   No celular:  arrastar o dedo para a esquerda (proxima) ou direita (anterior).
   Em qualquer um: os dois botoes redondos nas laterais da tela.

   Carregue SEMPRE depois de fichas.js, que traz a fila canonica em
   window.FICHAS (gerado por scripts/navegacao.py a partir de estrutura.py).

   Nada daqui entra no PDF: a UI vive fora do <article class="guia"> e o
   estilo .navf desaparece em @media print (ver template/estilo.css).
   ========================================================================== */
(function () {
  "use strict";

  var fichas = window.FICHAS;
  if (!Array.isArray(fichas) || !fichas.length) return;

  // Qual ficha e esta? O numero esta no proprio nome do arquivo.
  var achado = location.pathname.match(/guia(\d{3})/);
  if (!achado) return;
  var num = parseInt(achado[1], 10);
  var i = -1;
  for (var k = 0; k < fichas.length; k++) {
    if (fichas[k].n === num) { i = k; break; }
  }
  if (i < 0) return;

  var RAIZ = "../../";                     // de guias/volNN/ para a raiz
  var ant  = i > 0 ? fichas[i - 1] : null;
  var prox = i < fichas.length - 1 ? fichas[i + 1] : null;

  function url(f) { return f ? RAIZ + f.href : null; }
  function ir(f) { if (f) location.href = url(f); }
  function galeria() { location.href = RAIZ + "index.html"; }

  /* ---- UI: botoes laterais + atalho para a galeria ---------------------- */
  var barra = document.createElement("nav");
  barra.className = "navf";
  barra.setAttribute("aria-label", "Navegacao entre fichas");

  function botao(classe, ficha, glifo, rotulo) {
    var a = document.createElement("a");
    a.className = "navf-btn " + classe;
    a.innerHTML = '<span aria-hidden="true">' + glifo + "</span>";
    if (ficha) {
      a.href = url(ficha);
      a.title = rotulo + ": " + ("00" + ficha.n).slice(-3) + " — " + ficha.t;
      a.setAttribute("aria-label", a.title);
    } else {
      a.className += " navf-off";
      a.setAttribute("aria-disabled", "true");
    }
    return a;
  }

  barra.appendChild(botao("navf-ant", ant, "&#10094;", "Ficha anterior"));
  barra.appendChild(botao("navf-prox", prox, "&#10095;", "Proxima ficha"));

  var volta = document.createElement("a");
  volta.className = "navf-galeria";
  volta.href = RAIZ + "index.html";
  volta.title = "Voltar para a galeria (Esc)";
  volta.textContent = "galeria · " + ("00" + num).slice(-3) + "/" + fichas.length;
  barra.appendChild(volta);

  document.body.appendChild(barra);

  // Carrega as vizinhas de antemao: a troca fica instantanea.
  [ant, prox].forEach(function (f) {
    if (!f) return;
    var l = document.createElement("link");
    l.rel = "prefetch";
    l.href = url(f);
    document.head.appendChild(l);
  });

  /* ---- Teclado (notebook) ---------------------------------------------- */
  document.addEventListener("keydown", function (e) {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    var alvo = e.target;
    if (alvo && (alvo.isContentEditable ||
                 /^(INPUT|TEXTAREA|SELECT)$/.test(alvo.tagName || ""))) return;

    if (e.key === "ArrowLeft")       { e.preventDefault(); ir(ant); }
    else if (e.key === "ArrowRight") { e.preventDefault(); ir(prox); }
    else if (e.key === "Escape")     { e.preventDefault(); galeria(); }
  });

  /* ---- Arrastar o dedo (celular) --------------------------------------- */
  // Guardas: so gesto claramente horizontal, rapido, sem zoom de pinca e com a
  // pagina no fim da rolagem lateral — senao o arrasto e panoramica, nao troca.
  var x0 = 0, y0 = 0, t0 = 0, vale = false;

  function naBorda(dx) {
    var el = document.scrollingElement || document.documentElement;
    var sobra = el.scrollWidth - el.clientWidth;
    if (sobra <= 2) return true;
    return dx < 0 ? el.scrollLeft >= sobra - 2 : el.scrollLeft <= 2;
  }

  document.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) { vale = false; return; }
    var t = e.touches[0];
    x0 = t.clientX; y0 = t.clientY; t0 = Date.now(); vale = true;
  }, { passive: true });

  document.addEventListener("touchmove", function (e) {
    if (e.touches.length > 1) vale = false;   // virou pinca
  }, { passive: true });

  document.addEventListener("touchend", function (e) {
    if (!vale) return;
    vale = false;
    var vv = window.visualViewport;
    if (vv && vv.scale > 1.05) return;        // com zoom, o dedo e para panoramica
    var t = e.changedTouches[0];
    var dx = t.clientX - x0, dy = t.clientY - y0;
    if (Date.now() - t0 > 800) return;
    if (Math.abs(dx) < 70 || Math.abs(dx) < Math.abs(dy) * 2) return;
    if (!naBorda(dx)) return;
    ir(dx < 0 ? prox : ant);
  }, { passive: true });

  /* ---- Celular: a ficha cabe na tela ----------------------------------- */
  // A ficha tem 210 mm (794 px) fixos. Sem reduzir, ela nasce mais larga que o
  // celular: ilegivel e com rolagem lateral que competiria com o arrasto.
  var guia = document.querySelector("article.guia");
  function ajustar() {
    if (!guia) return;
    var larg = document.documentElement.clientWidth;
    var fit = larg / 794;
    guia.style.zoom = fit < 0.995 ? fit : "";
  }
  ajustar();
  window.addEventListener("resize", ajustar);
  window.addEventListener("orientationchange", ajustar);

  /* ---- Dica, uma vez por navegador ------------------------------------- */
  var toque = window.matchMedia && window.matchMedia("(hover: none)").matches;
  var chave = "navf-dica-vista";
  var visto = false;
  try { visto = localStorage.getItem(chave) === "1"; } catch (err) { visto = false; }
  if (!visto) {
    var dica = document.createElement("div");
    dica.className = "navf-dica";
    dica.textContent = toque
      ? "Arraste para o lado para mudar de ficha"
      : "Use ← e → para mudar de ficha · Esc volta para a galeria";
    document.body.appendChild(dica);
    setTimeout(function () { dica.classList.add("sai"); }, 4200);
    setTimeout(function () { dica.remove(); }, 5000);
    try { localStorage.setItem(chave, "1"); } catch (err) { /* file://, modo privado */ }
  }
})();
