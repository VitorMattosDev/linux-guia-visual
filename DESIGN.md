# DESIGN.md — Sistema de design da ficha visual

Referência dos blocos. Tudo é definido em `template/estilo.css`. As fichas apenas
**usam** estas classes — não redefinem cor nem fonte. Copie os trechos daqui.

## Paleta

| Papel        | Cor        | Variável        |
|--------------|------------|-----------------|
| Navy (base)  | `#16336b`  | `--navy`        |
| Azul acento  | `#1f6fd0`  | `--azul`        |
| Verde        | `#2e9b4e`  | `--verde`       |
| Laranja      | `#e8720c`  | `--laranja`     |
| Roxo         | `#6a3fa0`  | `--roxo`        |
| Vermelho     | `#d23b3b`  | `--vermelho`    |

Cada bloco colorido tem um fundo claro correspondente (`--verde-claro`, etc.).
Tipografia: títulos em Archivo/Montserrat (fallback system-ui), texto em Inter,
código em JetBrains Mono. As fontes têm fallback de sistema — funciona offline.

## A página

`<article class="guia">` = uma A4 retrato (210×297mm), com textura pontilhada sutil.
Estrutura fixa: **topo → cabeçalho → [blocos] → rodape-blocos → rodape**.
No print, cada `.guia` vira uma página (`page-break-after`).

## Blocos (catálogo)

### Topo + Cabeçalho
```html
<div class="topo"><span class="selo">Guia Visual 012</span></div>
<header class="cabecalho">
  <img class="logo" src="../../assets/icones/logo.svg" alt="">
  <div class="titulo"><h1>Título<br>Curto</h1><div class="sub">Frase que situa o problema.</div></div>
  <div class="badge"><b>012</b><span>Guias Linux</span></div>
</header>
```

### Fluxo numerado (etapas 1→N)
Passos com bolinha numerada e seta. Cores por passo: `verde`, `laranja`, `roxo`, `vermelho`.
```html
<section class="fluxo">
  <div class="passo"><span class="num">1</span><h3>Etapa</h3><p>Texto.</p></div>
  <span class="seta">→</span>
  <div class="passo verde"><span class="num">2</span><h3>Etapa</h3><p>Texto.</p></div>
</section>
```

### Título de seção (régua + texto centralizado)
```html
<div class="secao-titulo">Na prática</div>
```

### Grade de cards (2–4 colunas via `--col`)
Variações: `azul`, `verde`, `laranja`, `roxo`.
```html
<section class="cards" style="--col:3">
  <div class="card azul"><h3>Item</h3><p>Descrição.</p></div>
</section>
```

### Duas colunas (Conceito A × B)
```html
<section class="duas-colunas">
  <div class="coluna verde"><h3>A</h3><ul><li>Ponto.</li></ul></div>
  <div class="coluna azul"><h3>B</h3><ul><li>Ponto.</li></ul></div>
</section>
```

### Bloco de terminal
```html
<section class="terminal">
  <div class="barra"><i class="r"></i><i class="y"></i><i class="g"></i><span>kali@kali: ~</span></div>
<pre><span class="prompt">$</span> comando
<span class="out">saída</span>
<span class="cmt"># comentário</span></pre>
</section>
```

### Tabela de comparação
```html
<table class="comparacao">
  <thead><tr><th>A</th><th>B</th></tr></thead>
  <tbody><tr><td>...</td><td><code>cmd</code></td></tr></tbody>
</table>
```

### Aviso de perigo (comando destrutivo — obrigatório sinalizar)
```html
<div class="perigo"><b>Cuidado:</b> apaga dados. Ensaie em VM ou arquivo-imagem.</div>
```

### Rodapé: Resumo Rápido (verde) + Dica de Ouro (azul) — obrigatórios
```html
<section class="rodape-blocos">
  <div class="bloco resumo"><div class="cabeca">⚡ Resumo rápido</div>
    <div class="corpo"><ul><li>Ponto.</li></ul></div></div>
  <div class="bloco dica"><div class="cabeca">🐉 No Kali</div>
    <div class="corpo">A pegadinha.</div></div>
</section>
```
(A cabeça do bloco azul pode ser "◆ Dica de ouro" ou "🐉 No Kali" conforme o conteúdo.)

### Rodapé da página
```html
<footer class="rodape">
  <span class="marca">Linux &amp; Shell • Guia Visual</span>
  <span class="pag">Vol 02 · Fase 1 <span class="n">012</span></span>
</footer>
```

## Utilitários
- `code.inl` — código inline em texto corrido.
- `selo-kali` / `selo-lab` — pílulas 🐉 No Kali / 🧪 Laboratório.
- Visual específico de um assunto: `<style>` local **curto** na ficha, reusando as
  variáveis. Veja o decodificador rwx em `guias/vol03/guia020-permissoes-de-arquivo.html`.

## Princípios
1. Uma ficha = uma A4 = um assunto. Se não cabe, cortou de menos.
2. Consistência entre as 103 fichas > capricho isolado.
3. A cor tem função (verde=ok/resumo, laranja=atenção, vermelho=perigo, azul=info).
4. Imagem que não ensina não entra.
