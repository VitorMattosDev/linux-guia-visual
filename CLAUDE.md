# CLAUDE.md — Guia Visual Linux & Shell

Instruções de trabalho para o Claude Code neste repositório.

## O que é este projeto

Coleção de **fichas visuais** (infográficos A4) para **consulta rápida** dos assuntos
do *Manual de Linux e Shell Scripting*. Cada ficha condensa **um** capítulo do manual
em **uma ficha** (uma ou duas páginas A4) — no mesmo estilo do "Guia Visual de Redes, Fibra Óptica e Telecom":
limpo, colorido, didático, feito para bater o olho e lembrar.

**103 fichas · 16 volumes · 5 fases**, espelhando 1:1 os capítulos do manual.
Produto final: um **livro PDF único** (`_saida/guia-visual-linux.pdf`) + uma
**galeria HTML** de busca (`index.html`). A fila autoritativa está no `ROADMAP.md`.
A estrutura canônica vive em `scripts/estrutura.py` — mudança de fichas começa por lá.

O manual-fonte fica na pasta irmã `../manual-linux-master/` (mesmo nível desta pasta,
no Desktop). **Ela é só leitura**: a ficha é a destilação visual do capítulo, nunca
uma cópia. Se o Claude Code não tiver acesso a ela, peça para o usuário adicioná-la
(ou confirme o caminho com `python scripts/estrutura.py --vol 1`, que imprime onde
o manual foi localizado).

## Modo de execução

Execução autônoma. Você está pré-aprovado para criar/editar fichas, gerar imagens,
renderizar PDFs e commitar sem pedir confirmação a cada passo. **Única condição de
parada:** erro real de bloqueio.

**Um VOLUME inteiro por sessão.** A sessão cobre todas as fichas de um volume (6 ou 7),
na ordem. O usuário dá `/clear` e abre a próxima sessão para o próximo volume. Trabalhe
o volume até o fim; não pare no meio a não ser por erro de bloqueio.

- `/model opus` para desenhar as fichas; `/model sonnet` para tarefa mecânica (ROADMAP, mover arquivo).
- **Contexto:** fichas são pesadas de imagem. Se chegar perto de ~80% do contexto no meio
  do volume, dê `/compact` e continue — o `ROADMAP.md` marca o que já ficou pronto, então
  dá para retomar sem perder o fio. Faça **commit por ficha** (não acumule): assim um
  `/compact` ou uma interrupção nunca perde trabalho.
- **Renderize ficha a ficha** (`python scripts/build.py NNN`) e confira a miniatura antes do
  commit. Revisto depois do Volume 1: quase toda ficha precisou de um ajuste de layout que
  só aparece no render, e consertar sete no fim sai mais caro. Cada miniatura custa ~1,5k
  tokens — se o contexto apertar, dê `/compact` (o ROADMAP guarda o progresso) em vez de
  parar de conferir. O `python scripts/build.py --vol NN` no fim do volume continua
  obrigatório: é ele que remonta o livro e a galeria.

## Fluxo de um volume (siga nesta ordem)

1. **Abra a fila do volume:** `python scripts/estrutura.py --vol NN`. Ela lista, na ordem,
   cada ficha do volume com o **destino HTML** e o **capítulo-fonte** a ler. Esse é o mapa
   da sessão. Confira também no `ROADMAP.md` o que já está `[x]` (pule essas).
2. **Smoke test (1ª ficha do volume):** faça a primeira ficha inteira, renderize com
   `python scripts/build.py <num>` e confira a miniatura antes de seguir. Garante que o
   estilo/paths estão certos para o volume todo. Depois dela, siga rendendo e conferindo
   ficha a ficha (ver "Modo de execução").
3. **Para cada ficha restante do volume, na ordem** — repita o ciclo abaixo:

   a. **Leia o capítulo-fonte** (`../manual-linux-master/volNN/capNNN-*.qmd`). Extraia: o
      problema de abertura, os 4–6 conceitos que mais importam, os comandos essenciais, a
      tabela/decodificação central, a seção **🐉 No Kali** e o **Laboratório**.
   b. **Destile, não copie.** O que um técnico consultaria com pressa; corte o resto.
      Mire UMA A4 (até 1077 px em print). Se o assunto não couber sem perder o essencial,
      **use duas páginas cheias** — nunca corte conteúdo para forçar uma só.
   c. O stub HTML da ficha já existe (`guias/volNN/...`). Se faltar, `python scripts/novo-guia.py NNN`.
   d. **Preencha os blocos** (ver `DESIGN.md`). Ordem típica: topo → cabeçalho → fluxo →
      cards → duas colunas → na prática (terminal + comparação) → **Resumo + Dica** → rodapé.
   e. **Gere as imagens** que o assunto pedir (ver "Imagens"). O visual central costuma ser
      a figura TikZ do próprio capítulo, traduzida para CSS.
   e2. **Renderize e confira** (`python scripts/build.py NNN` → `_saida/thumbs/guiaNNN.png`
      e `python scripts/paginacao.py NNN`): nada cortado na direita? sai inteira no PDF?
   f. Marque a ficha como `[x]` no `ROADMAP.md` e **commit**: `guia NNN: <título>`.

4. **Ao fim do volume:** `python scripts/build.py --vol NN` — renderiza todas as fichas do
   volume, atualiza as miniaturas, remonta o livro `_saida/guia-visual-linux.pdf` e a galeria.
5. **Valide o volume** (ver "Validação") e faça um commit final: `vol NN: fecha volume`.
   Encerre — o usuário dará `/clear` para o próximo volume.

## Anatomia de uma ficha (o que toda ficha tem)

- **Cabeçalho** com título curto em caixa-alta e um subtítulo que situa o problema
  (nunca definição de dicionário — um cenário real de quem administra Linux).
- **2 a 4 blocos de conteúdo** escolhidos conforme o assunto: fluxo de etapas, grade
  de cards, comparação A×B, tabela, bloco de terminal.
- **🐉 No Kali** — o que muda no Kali (rolling, root, metapacotes, kali-tweaks). Cabe
  na Dica de Ouro ou num card próprio. **Obrigatório** em toda ficha.
- **Resumo Rápido** (bloco verde, 3–5 bullets) — **obrigatório**.
- **Dica de Ouro** (bloco azul) — o atalho/pegadinha que só se aprende usando. **Obrigatório.**

Alvo de texto: enxuto. Mas **conteúdo inteiro vem antes de página única**: se não couber
confortavelmente numa A4, a ficha ocupa duas páginas — as duas razoavelmente cheias.

## Política editorial (herdada do manual)

- **Comandos destrutivos** (`rm -rf`, `dd`, `mkfs`, `fdisk`, `cryptsetup luksFormat`)
  **sempre** dentro de um bloco `.perigo` com aviso claro e, quando possível, a versão
  segura de ensaio (arquivo-imagem via `losetup`, VM descartável, `--dry-run`).
- **Conteúdo ofensivo (Vol 14, ferramentas do Kali):** caráter educacional e defensivo.
  Explica mecanismo e uso legítimo (laboratório próprio, teste autorizado); menciona que
  uso não autorizado é crime (Lei 12.737/2012). Nunca passo a passo contra alvo real.
- Todo comando mostrado é para ser digitado: comando → saída esperada → o que interpretar.

## Imagens (o ponto que o Vitor mais quer: "limpas, coloridas e reais")

Três níveis, do mais usado ao menos:

1. **SVG/CSS vetorial** (padrão) — ícones, diagramas de fluxo, a decodificação de bits,
   pilhas, árvores. É o que dá o visual limpo e colorido da maioria das fichas e imprime
   perfeito. O guia-demo (020) é feito 100% assim. **Prefira isto** para conceitos
   abstratos (permissões, pipes, processos, regex): fica mais nítido que foto forçada.
2. **Render realista** — só onde existe *hardware/objeto real* que ajuda a fixar
   (servidor, notebook com terminal, pendrive/USB, disco, roteador, o mascote Tux).
   Gere a imagem, salve em `assets/img/guiaNNN-<algo>.png` e referencie no HTML.
   Mantenha fundo claro/limpo e paleta coerente com a ficha (navy/verde/laranja/roxo).
3. **Captura de tela** de terminal real — quando a saída verdadeira vale mais que um
   desenho. Recorte, mantenha legível a 100%.

Regra: a imagem serve à compreensão. Nada de enfeite que não ensina. Consistência de
cor e traço entre as 103 fichas é mais importante que capricho numa só.

## Sistema de design

Tudo (cores, fontes, medidas, componentes) vive em `template/estilo.css`. **Nunca
redefina cor ou fonte numa ficha.** Use as classes do catálogo em `DESIGN.md`. Visual
específico de um assunto (ex.: o decodificador rwx da ficha 020) pode ir num `<style>`
local **curto** na própria ficha, reusando as variáveis `--navy`, `--azul`, etc.

Paleta: navy `#16336b` · azul `#1f6fd0` · verde `#2e9b4e` · laranja `#e8720c` ·
roxo `#6a3fa0` · vermelho `#d23b3b` (perigo). Fichas A4 retrato (210×297mm).

## Validação

**Por ficha** (antes do commit da ficha, sem renderizar): reveja o HTML que você
acabou de escrever e confirme —

1. Título, subtítulo, número (badge e rodapé), volume e fase corretos.
2. Resumo Rápido e Dica de Ouro presentes; **🐉 No Kali** contemplado.
3. Nenhum comando destrutivo sem bloco `.perigo`.
4. Comandos e saídas conferem com o capítulo-fonte (sem inventar flag).
5. Caminhos de imagem e CSS com `../../` correto.

**Por volume** (depois de `python scripts/build.py --vol NN`): abra cada miniatura
em `_saida/thumbs/guiaNNN.png` e confirme —

6. Cada ficha sai **inteira** no PDF (o rodapé aparece) e nenhuma página fica quase vazia.
   Rode `python scripts/paginacao.py` — ele responde isso de forma objetiva.
7. Imagens carregaram (sem quadrado quebrado) e combinam com a paleta.
8. As fichas do volume parecem uma família — mesma linguagem visual, sem uma destoando.

Só então o commit final do volume: `git commit -m "vol NN: fecha volume"`.

## Regras que evitam retrabalho

- **Stub-first / estrutura canônica:** qualquer mudança de fichas (número, título,
  volume) começa em `scripts/estrutura.py`. Depois `python scripts/estrutura.py --stubs`.
- **`--roadmap` preserva `[x]`/`[~]`** relendo o arquivo antes de reescrever. Não altere
  o formato `- [x] **guia NNN**` ou o regex para de casar e tudo volta a `[ ]`. Na dúvida,
  use só `--stubs` e edite o status na mão.
- **Caminho das imagens é relativo à ficha:** de `guias/volNN/` use `../../assets/img/...`
  e `../../template/estilo.css`. Errar o `../../` é a causa nº 1 de imagem/estilo sumido.
- **Não edite `manual-linux-master/`** — é a fonte, só leitura.
- **Commits:** apenas `-m "..."` simples.
- **Um assunto por ficha.** Se um capítulo é dois assuntos grandes, ainda assim é UMA
  ficha — priorize o núcleo e deixe o resto para o Resumo. Não crie ficha fora dos 103.

## Aprendizados de produção (Volume 1) — leia antes de começar

Tudo aqui já custou tempo uma vez. Não redescubra.

### Ambiente (Windows + Git Bash)

- **Instalação:** `python -m pip install playwright pypdf pymupdf` e
  `python -m playwright install chromium`. O `pymupdf` serve para **olhar o PDF de
  verdade** (o `pdftoppm` não existe aqui):
  `python -c "import fitz; d=fitz.open('_saida/pdf/guia084.pdf'); d[0].get_pixmap(dpi=96).save('p1.png')"`
  — e aí sim dá para conferir onde a quebra de página caiu numa ficha de duas páginas.
  O `--break-system-packages` do PROMPT-INICIAL é de Linux e **não** se usa aqui.
- **Escreva o HTML da ficha com a ferramenta Write, nunca com heredoc no Bash.** Heredoc com
  ficha inteira quebra o parser (`unexpected EOF while looking for matching '`).
- **Mensagens de commit em ASCII** (sem acento): o console mangla acentuação.
- **Editar o ROADMAP** por script Python com `io.open(..., encoding="utf-8", newline="\n")`;
  o `print` no console sai truncado, mas o arquivo fica correto — confira com `git diff`, não
  com o print. Padrão que funciona:
  `s.replace("- [ ] **guia 0NN**", "- [x] **guia 0NN**")`.

### O orçamento de altura (revisto no Volume 13 — leia antes de cortar conteúdo)

**A ficha pode ocupar mais de uma A4.** Até o Volume 13 o `.guia` tinha, no modo print,
`height: 297mm` + `overflow: hidden`: o PDF sempre saía com uma página e **tudo o que
passava de uma A4 era descartado em silêncio** — o Resumo Rápido, a Dica e o rodapé das
fichas dos Volumes 9 a 12 nunca chegaram ao livro. Hoje a ficha **flui** pelas páginas que
precisar, com margem de 12 mm no topo de cada uma e os blocos marcados para não serem
partidos ao meio (`break-inside: avoid`).

A ordem de preferência é esta, e ela vale mais que a estética:
**ficha inteira em duas páginas cheias > ficha inteira em uma página > ficha cortada.**
Nunca sacrifique conteúdo para forçar uma página só.

- **Cabe em UMA página** a ficha com até **1077 px** de altura em `media=print`
  (A4 = 1122,5 px @96dpi − 12 mm da margem superior). Largura útil: **703 px** (186 mm).
- **Passou disso, use duas páginas** — mas as duas têm de ficar razoavelmente cheias.
  Segunda página com menos de 20% é o único resultado inaceitável: ou você aperta o
  respiro, ou redistribui conteúdo para equilibrar as duas.
- **O respiro entre blocos é uma variável:** `--gap-blocos` (padrão 7 mm) no `<style>`
  local da ficha, e o print respeita o mesmo valor. Baixar de 7 mm para 5 mm numa ficha
  de 13 blocos recupera ~75 px **sem cortar uma palavra** — é sempre a primeira alavanca.
  Abaixo de 4 mm a ficha começa a parecer apertada; aí é hora de aceitar a segunda página.
- Cuidado com `gap` no print: o `.guia` vira `display: block`, então o espaço entre blocos
  vem de `margin-bottom`, e **margens adjacentes colapsam**. Um `.secao-titulo` com
  `margin` própria não soma ao respiro como somava no flex.

Custo aproximado de cada bloco (medido no Volume 1, ainda válido):

| Bloco | Altura |
|---|---|
| `.topo` + `.cabecalho` | ~38 mm |
| `.secao-titulo` | ~8 mm (cada) |
| `.cards` (uma linha) · `.fluxo` | ~30 mm |
| `.duas-colunas` (5 itens) | ~38 mm |
| `table.comparacao` | ~7 mm por linha + 8 de cabeçalho |
| `.terminal` (6 linhas) | ~35 mm |
| `.perigo` (3–4 linhas) | ~16 mm |
| `.rodape-blocos` + `.rodape` | ~60 mm |

Se a conta passar de ~250 mm, corte **antes** de renderizar: junte dois blocos pequenos
num grid de duas colunas (economiza um `.secao-titulo` e um gap de 7 mm) — foi o que
resolveu 005 (matriz + tabela lado a lado) e 006 (códigos de saída + operadores).

### Armadilhas de CSS que já morderam

- **`white-space:nowrap` em token largo estoura os 703 px** e o conteúdo some no corte à
  direita (ficha 006, o `192.168.56.0/24`). Em token longo use `white-space:normal;
  word-break:break-all` e baixe a fonte para ~12.5px.
- **Não use `code.inl` dentro de `<th>`**: o fundo claro sobre o navy vira um borrão.
  Escreva o cabeçalho em texto puro.
- **Seletor de tag dentro de componente vaza para o texto**: `.lib b { display:block }`
  pegou também os `<b>` do corpo. Escopo com filho direto (`.lib > b`).
- **Linha de fundo posicionada em `px` precisa conferir com o conteúdo**: o `::before` da
  linha do tempo (002) nasceu riscando os anos; a posição correta é o centro da bolinha.
- **Réguas verticais com altura fixa em `px` são frágeis** (001): prefira dividir em zonas
  flex, cada uma com sua régua, em vez de calcular `calc(100% - 96px)`.
- `code.inl` tem padding lateral: **evite terminar frase com `<code>` seguido de ponto** —
  fica um espaço feio antes do `.`.

### Renderização e validação

- **`scripts/build.py` já foi corrigido**: as miniaturas saíam de um viewport de 595 px
  contra uma A4 de 794 px, ou seja, **cortavam** a ficha em vez de reduzi-la (o thumb do
  guia-demo 020 estava assim). Hoje fotografa o próprio `article.guia`. Não volte a usar
  `set_viewport_size({"width":595...})` + `page.screenshot()`.
- **Vale renderizar ficha a ficha** (`python scripts/build.py NNN`) e olhar a miniatura antes
  do commit, não só a 1ª do volume: quase toda ficha do Volume 1 precisou de um ajuste de
  layout que só aparece no render (estouro de largura, linha fora de lugar). É mais barato
  que consertar sete fichas no fim. O `build --vol NN` no fechamento continua obrigatório.
- **Prova objetiva de que a ficha saiu INTEIRA**: `python scripts/paginacao.py` (sem
  argumento audita tudo que está `[x]`; com números, só essas fichas). Ele verifica as três
  coisas que importam: o **rodapé aparece no PDF** (nada foi perdido), a **última página
  não está quase vazia** e nenhum bloco atômico foi partido. Sai com status 1 se achar
  problema. **Não volte à checagem antiga de "cada PDF tem 1 página"**: ela passava sempre,
  porque o corte era silencioso — e foi por isso que 77 fichas ficaram incompletas no livro.
- **Checagem dos obrigatórios do volume**, de uma vez (o `grep` do Git Bash não casa o 🐉;
  use Python):
  ```bash
  python -c "import io,glob,re,os;[print(os.path.basename(f)[:7], s.count('🐉'), 'resumo' in s and 'dica' in s) for f in sorted(glob.glob('guias/volNN/*.html')) for s in [io.open(f,encoding='utf-8').read()]]"
  ```

### Densidade que funcionou

Sete fichas, sete visuais distintos, mesma família: pilha de camadas (001), linha do tempo
(002), fluxo numerado (003), cadeia de pílulas (004), árvore em duas colunas colorida por
classe (005), dissecação token a token (006), grade numerada (007). **O visual central da
ficha é sempre a figura que o capítulo já tem em TikZ** — traduza-a para CSS em vez de
inventar outra. Tudo saiu em SVG/CSS: o Volume 1 não pediu nenhuma imagem realista nem
captura de tela, e `assets/img/` segue vazio.

## Aprendizados de produção (Volume 13)

### Desenhe já dentro do orçamento, e meça em vez de adivinhar

`python scripts/paginacao.py NNN --blocos` lista a altura de cada bloco da ficha. Use isso
**enquanto escreve**, não só no fim: no Volume 13 as três primeiras fichas custaram muitas
rodadas de tentativa e erro até eu medir direito; as quatro últimas saíram quase de primeira.

Orçamento que funcionou para uma ficha de UMA página (1077 px em print), com
`--gap-blocos: 5mm` e 7 filhos diretos (topo, cabeçalho, 3 seções, rodapé-blocos, rodapé):

| Parte | Altura |
|---|---|
| `.topo` + `.cabecalho` (subtítulo de 3 linhas) | ~142 px |
| cada seção de conteúdo (título + figura/grade) | ~195 px |
| `.rodape-blocos` (Resumo 5–6 bullets + Dica) | ~190 px |
| `.rodape` | 35 px |
| os 6 gaps de 5 mm | ~113 px |

### As três armadilhas que consumiram tempo

- **Em grid de duas colunas, a coluna mais alta manda.** Aparar a coluna curta não muda
  nada — e foi o erro que mais repeti. Equilibre as duas, ou mexa na proporção do
  `grid-template-columns` (alargar a coluna de texto costuma eliminar duas linhas).
- **Resumo e Dica têm sempre a mesma altura** (células do mesmo grid): cortar só a Dica
  não encolhe o bloco. Corte os dois, ou aproveite a folga para engordar o Resumo de graça.
- **Trocar palavras raramente tira uma linha.** Se precisa de 30 px, mexa no que muda
  altura de verdade: `--gap-blocos`, `line-height`, uma linha a menos no terminal, uma
  linha a menos na tabela. Reescrever frase por frase gasta rodadas e não entrega px.

### Um detalhe de HTML que pega

Bloco de "terminal" feito com `<div>` em vez de `<pre>` **colapsa as quebras de linha**:
o conteúdo vira um parágrafo só e a ficha parece 60 px mais curta do que é. Se usar um
`<div>` estilizado como terminal, ponha `white-space: pre-wrap` (aconteceu na ficha 082).

### Densidade do Volume 13

Sete fichas, sete visuais distintos, todos tradução direta da figura TikZ do capítulo:
pilha TCP/IP + encapsulamento (078), as três camadas que disputam a interface (079), a
escada de diagnóstico em seis degraus (080), senha × chave pública e os três túneis (081),
decodificador do `curl -v` (082), o caminho do pacote pelos ganchos do Netfilter (083),
o que o TLS esconde (084). Tudo em SVG/CSS — `assets/img/` segue vazio.

## Estratégia de produção

Uma sessão = um volume, do Volume 1 ao 16, em ordem (fecha a Fase antes de avançar).
O usuário dá `/clear` entre volumes. Dentro da sessão: smoke test na 1ª ficha, depois
as demais em sequência com commit por ficha, e o `build --vol` só no fim.

O guia-demo **020 (Permissões)** é a referência de qualidade e densidade — abra-o quando
tiver dúvida de "quanto conteúdo" ou "como fica um bloco". Já está `[x]`: ao chegar no
Volume 3, pule a ficha 020.
