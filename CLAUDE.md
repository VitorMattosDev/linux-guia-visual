# CLAUDE.md — Guia Visual Linux & Shell

Instruções de trabalho para o Claude Code neste repositório.

## O que é este projeto

Coleção de **fichas visuais** (infográficos A4) para **consulta rápida** dos assuntos
do *Manual de Linux e Shell Scripting*. Cada ficha condensa **um** capítulo do manual
em **uma página** — no mesmo estilo do "Guia Visual de Redes, Fibra Óptica e Telecom":
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
- **Não renderize a cada ficha.** Renderize UMA vez, no fim do volume, com
  `python scripts/build.py --vol NN` (mais rápido e evita encher o contexto com imagens).
  Exceção: a **primeira** ficha do volume — renderize-a sozinha para o smoke test.

## Fluxo de um volume (siga nesta ordem)

1. **Abra a fila do volume:** `python scripts/estrutura.py --vol NN`. Ela lista, na ordem,
   cada ficha do volume com o **destino HTML** e o **capítulo-fonte** a ler. Esse é o mapa
   da sessão. Confira também no `ROADMAP.md` o que já está `[x]` (pule essas).
2. **Smoke test (só na 1ª ficha do volume):** faça a primeira ficha inteira, renderize com
   `python scripts/build.py <num>` e confira a miniatura antes de seguir. Garante que o
   estilo/paths estão certos para o volume todo.
3. **Para cada ficha restante do volume, na ordem** — repita o ciclo abaixo:

   a. **Leia o capítulo-fonte** (`../manual-linux-master/volNN/capNNN-*.qmd`). Extraia: o
      problema de abertura, os 4–6 conceitos que mais importam, os comandos essenciais, a
      tabela/decodificação central, a seção **🐉 No Kali** e o **Laboratório**.
   b. **Destile, não copie.** A ficha cabe em UMA A4. O que um técnico consultaria com pressa.
      Corte o resto. Densidade acima de volume.
   c. O stub HTML da ficha já existe (`guias/volNN/...`). Se faltar, `python scripts/novo-guia.py NNN`.
   d. **Preencha os blocos** (ver `DESIGN.md`). Ordem típica: topo → cabeçalho → fluxo →
      cards → duas colunas → na prática (terminal + comparação) → **Resumo + Dica** → rodapé.
   e. **Gere as imagens** que o assunto pedir (ver "Imagens").
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

Alvo de texto: enxuto. Se não cabe numa A4 confortável, cortou de menos.

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

6. Cada ficha **cabe em UMA página** sem cortar conteúdo nem sobrar meia página vazia.
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

## Estratégia de produção

Uma sessão = um volume, do Volume 1 ao 16, em ordem (fecha a Fase antes de avançar).
O usuário dá `/clear` entre volumes. Dentro da sessão: smoke test na 1ª ficha, depois
as demais em sequência com commit por ficha, e o `build --vol` só no fim.

O guia-demo **020 (Permissões)** é a referência de qualidade e densidade — abra-o quando
tiver dúvida de "quanto conteúdo" ou "como fica um bloco". Já está `[x]`: ao chegar no
Volume 3, pule a ficha 020.
