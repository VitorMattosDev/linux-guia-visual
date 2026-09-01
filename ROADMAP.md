# ROADMAP — Guia Visual Linux

Fila autoritativa. Status: `[ ]` pendente · `[~]` em andamento · `[x]` concluído.
Um guia por sessão. Commit: `guia NNN: <titulo>` com o status no mesmo commit.

## Dívida técnica em aberto — reequilíbrio de página (Vols 1 a 6)

Desde o Volume 13 a ficha **flui pelas páginas que precisar** e nada mais é cortado do PDF
(ver `template/estilo.css`, bloco `@media print`, e `scripts/paginacao.py`). Ficaram, porém,
**17 fichas íntegras mas mal equilibradas**: a segunda página leva só o Resumo e a Dica,
com menos de 20% de ocupação. Elas precisam de 100 a 210 px — já não sai do respiro
(`--gap-blocos`), é redistribuição editorial: dar mais corpo à página 2, ou passar um bloco
da 1 para a 2 e deixar as duas cheias.

    001 010 011 016 017 019 020 022 023 027 028 029 030 033 038 042 043

A lista se regenera sozinha com `python scripts/paginacao.py` (elas saem na seção
PROBLEMAS). **Não é urgente e não bloqueia volume nenhum** — o livro já está completo.
Decisão do Vitor sobre quando encarar: pode ser antes do Volume 14 ou depois do 16.

## Fase 1 — Fundamentos do Linux

### Volume 1 — Primeiros Passos: Linux e Kali

- [x] **guia 001** - O que é Linux: kernel, distribuições e software livre - `guias/vol01/guia001-o-que-e-linux-kernel-distribuicoes-e-software-li.html`
- [x] **guia 002** - Por que Kali Linux: propósito, filosofia e quando não usá-lo - `guias/vol01/guia002-por-que-kali-linux-proposito-filosofia-e-quando-.html`
- [x] **guia 003** - Instalando o Kali: VM, bare metal, WSL e live USB - `guias/vol01/guia003-instalando-o-kali-vm-bare-metal-wsl-e-live-usb.html`
- [x] **guia 004** - Primeiro contato: sessão, ambiente Xfce e organização - `guias/vol01/guia004-primeiro-contato-sessao-ambiente-xfce-e-organiza.html`
- [x] **guia 005** - A estrutura de diretórios do Linux (FHS) - `guias/vol01/guia005-a-estrutura-de-diretorios-do-linux-fhs.html`
- [x] **guia 006** - Anatomia de um comando: shell, argumentos e opções - `guias/vol01/guia006-anatomia-de-um-comando-shell-argumentos-e-opcoes.html`
- [x] **guia 007** - Obtendo ajuda: man, info, tldr e a doc do Kali - `guias/vol01/guia007-obtendo-ajuda-man-info-tldr-e-a-doc-do-kali.html`

### Volume 2 — O Terminal e o Shell

- [x] **guia 008** - Emulador de terminal e shell: bash, zsh e o padrão do Kali - `guias/vol02/guia008-emulador-de-terminal-e-shell-bash-zsh-e-o-padrao.html`
- [x] **guia 009** - Navegação: pwd, cd, ls e caminhos absolutos e relativos - `guias/vol02/guia009-navegacao-pwd-cd-ls-e-caminhos-absolutos-e-relat.html`
- [x] **guia 010** - Manipulando arquivos e diretórios: cp, mv, rm, mkdir - `guias/vol02/guia010-manipulando-arquivos-e-diretorios-cp-mv-rm-mkdir.html`
- [x] **guia 011** - Visualizando conteúdo: cat, less, head, tail e more - `guias/vol02/guia011-visualizando-conteudo-cat-less-head-tail-e-more.html`
- [x] **guia 012** - Redirecionamento e pipes: stdin, stdout e stderr - `guias/vol02/guia012-redirecionamento-e-pipes-stdin-stdout-e-stderr.html`
- [x] **guia 013** - Curingas, globbing e expansão de chaves - `guias/vol02/guia013-curingas-globbing-e-expansao-de-chaves.html`
- [x] **guia 014** - Histórico, atalhos de teclado e produtividade - `guias/vol02/guia014-historico-atalhos-de-teclado-e-produtividade.html`

### Volume 3 — Arquivos e o Sistema de Arquivos

- [x] **guia 015** - Tipos de arquivo, inodes e a árvore de diretórios - `guias/vol03/guia015-tipos-de-arquivo-inodes-e-a-arvore-de-diretorios.html`
- [x] **guia 016** - Links simbólicos e hard links - `guias/vol03/guia016-links-simbolicos-e-hard-links.html`
- [x] **guia 017** - Localizando arquivos: find, locate, which e type - `guias/vol03/guia017-localizando-arquivos-find-locate-which-e-type.html`
- [x] **guia 018** - Compactação e arquivamento: tar, gzip, xz e zip - `guias/vol03/guia018-compactacao-e-arquivamento-tar-gzip-xz-e-zip.html`
- [x] **guia 019** - Montagem de dispositivos e o comando mount - `guias/vol03/guia019-montagem-de-dispositivos-e-o-comando-mount.html`
- [x] **guia 020** - Permissões de arquivo: leitura, escrita e execução - `guias/vol03/guia020-permissoes-de-arquivo-leitura-escrita-e-execucao.html`

### Volume 4 — Usuários, Grupos e Permissões

- [x] **guia 021** - Usuários, grupos e o arquivo /etc/passwd - `guias/vol04/guia021-usuarios-grupos-e-o-arquivo-etc-passwd.html`
- [x] **guia 022** - O root, sudo e a elevação de privilégios - `guias/vol04/guia022-o-root-sudo-e-a-elevacao-de-privilegios.html`
- [x] **guia 023** - Permissões especiais: SUID, SGID e sticky bit - `guias/vol04/guia023-permissoes-especiais-suid-sgid-e-sticky-bit.html`
- [x] **guia 024** - ACLs e atributos estendidos de arquivo - `guias/vol04/guia024-acls-e-atributos-estendidos-de-arquivo.html`
- [x] **guia 025** - Gerenciamento de usuários, senhas e o PAM - `guias/vol04/guia025-gerenciamento-de-usuarios-senhas-e-o-pam.html`
- [x] **guia 026** - Trabalhando como root no Kali com segurança - `guias/vol04/guia026-trabalhando-como-root-no-kali-com-seguranca.html`

## Fase 2 — Administração do Sistema

### Volume 5 — Processos e Controle de Tarefas

- [x] **guia 027** - O que é um processo: PID, estados e a árvore - `guias/vol05/guia027-o-que-e-um-processo-pid-estados-e-a-arvore.html`
- [x] **guia 028** - Monitoramento: ps, top e htop - `guias/vol05/guia028-monitoramento-ps-top-e-htop.html`
- [x] **guia 029** - Sinais e controle: kill, killall, nice e prioridades - `guias/vol05/guia029-sinais-e-controle-kill-killall-nice-e-prioridade.html`
- [x] **guia 030** - Jobs, primeiro e segundo plano, nohup e disown - `guias/vol05/guia030-jobs-primeiro-e-segundo-plano-nohup-e-disown.html`
- [x] **guia 031** - Multiplexação de terminal: tmux e screen - `guias/vol05/guia031-multiplexacao-de-terminal-tmux-e-screen.html`
- [x] **guia 032** - Recursos do sistema: memória, CPU, uptime e limites - `guias/vol05/guia032-recursos-do-sistema-memoria-cpu-uptime-e-limites.html`

### Volume 6 — Gerenciamento de Pacotes

- [x] **guia 033** - APT e o modelo Debian: repositórios e o Kali rolling - `guias/vol06/guia033-apt-e-o-modelo-debian-repositorios-e-o-kali-roll.html`
- [x] **guia 034** - Instalando, removendo e atualizando pacotes com apt - `guias/vol06/guia034-instalando-removendo-e-atualizando-pacotes-com-a.html`
- [x] **guia 035** - dpkg, arquivos .deb e resolução de dependências - `guias/vol06/guia035-dpkg-arquivos-deb-e-resolucao-de-dependencias.html`
- [x] **guia 036** - Repositórios do Kali, metapacotes e kali-tweaks - `guias/vol06/guia036-repositorios-do-kali-metapacotes-e-kali-tweaks.html`
- [x] **guia 037** - Compilando a partir do código-fonte - `guias/vol06/guia037-compilando-a-partir-do-codigo-fonte.html`
- [x] **guia 038** - Alternativas: pipx, snap, flatpak e AppImage - `guias/vol06/guia038-alternativas-pipx-snap-flatpak-e-appimage.html`

### Volume 7 — Boot, systemd e Serviços

- [x] **guia 039** - O processo de inicialização: UEFI, GRUB e o kernel - `guias/vol07/guia039-o-processo-de-inicializacao-uefi-grub-e-o-kernel.html`
- [x] **guia 040** - systemd: units, targets e o modelo de serviços - `guias/vol07/guia040-systemd-units-targets-e-o-modelo-de-servicos.html`
- [x] **guia 041** - Gerenciando serviços com systemctl - `guias/vol07/guia041-gerenciando-servicos-com-systemctl.html`
- [x] **guia 042** - Logs com journald e o syslog tradicional - `guias/vol07/guia042-logs-com-journald-e-o-syslog-tradicional.html`
- [x] **guia 043** - Agendamento: cron, at e timers do systemd - `guias/vol07/guia043-agendamento-cron-at-e-timers-do-systemd.html`
- [x] **guia 044** - Targets, recuperação e problemas de boot - `guias/vol07/guia044-targets-recuperacao-e-problemas-de-boot.html`

### Volume 8 — Armazenamento e Sistemas de Arquivos

- [x] **guia 045** - Discos, partições e a nomenclatura de dispositivos - `guias/vol08/guia045-discos-particoes-e-a-nomenclatura-de-dispositivo.html`
- [x] **guia 046** - Particionamento com fdisk, parted e gdisk - `guias/vol08/guia046-particionamento-com-fdisk-parted-e-gdisk.html`
- [x] **guia 047** - Sistemas de arquivos: ext4, Btrfs, XFS e formatação - `guias/vol08/guia047-sistemas-de-arquivos-ext4-btrfs-xfs-e-formatacao.html`
- [x] **guia 048** - LVM: volumes lógicos flexíveis - `guias/vol08/guia048-lvm-volumes-logicos-flexiveis.html`
- [x] **guia 049** - RAID por software com mdadm - `guias/vol08/guia049-raid-por-software-com-mdadm.html`
- [x] **guia 050** - Criptografia de disco com LUKS e persistência no Kali - `guias/vol08/guia050-criptografia-de-disco-com-luks-e-persistencia-no.html`

## Fase 3 — Shell Scripting

### Volume 9 — Fundamentos de Shell Scripting

- [x] **guia 051** - Do comando ao script: o primeiro script Bash - `guias/vol09/guia051-do-comando-ao-script-o-primeiro-script-bash.html`
- [x] **guia 052** - Variáveis, o ambiente e o escopo de exportação - `guias/vol09/guia052-variaveis-o-ambiente-e-o-escopo-de-exportacao.html`
- [x] **guia 053** - Aspas, expansões e substituição de comandos - `guias/vol09/guia053-aspas-expansoes-e-substituicao-de-comandos.html`
- [x] **guia 054** - Entrada e saída: read, echo e printf - `guias/vol09/guia054-entrada-e-saida-read-echo-e-printf.html`
- [x] **guia 055** - Condicionais: test, colchetes duplos e if - `guias/vol09/guia055-condicionais-test-colchetes-duplos-e-if.html`
- [x] **guia 056** - Códigos de saída e o encadeamento de comandos - `guias/vol09/guia056-codigos-de-saida-e-o-encadeamento-de-comandos.html`
- [x] **guia 057** - Boas práticas: shebang, permissões e portabilidade - `guias/vol09/guia057-boas-praticas-shebang-permissoes-e-portabilidade.html`

### Volume 10 — Scripting Intermediário

- [x] **guia 058** - Laços: for, while e until - `guias/vol10/guia058-lacos-for-while-e-until.html`
- [x] **guia 059** - Funções, retorno e escopo de variáveis - `guias/vol10/guia059-funcoes-retorno-e-escopo-de-variaveis.html`
- [x] **guia 060** - Arrays indexados e associativos - `guias/vol10/guia060-arrays-indexados-e-associativos.html`
- [x] **guia 061** - Parâmetros posicionais e getopts - `guias/vol10/guia061-parametros-posicionais-e-getopts.html`
- [x] **guia 062** - Expansão de parâmetros avançada - `guias/vol10/guia062-expansao-de-parametros-avancada.html`
- [x] **guia 063** - Aritmética e manipulação de números no shell - `guias/vol10/guia063-aritmetica-e-manipulacao-de-numeros-no-shell.html`

### Volume 11 — Processamento de Texto

- [x] **guia 064** - Expressões regulares: fundamentos e sabores - `guias/vol11/guia064-expressoes-regulares-fundamentos-e-sabores.html`
- [x] **guia 065** - grep e a busca de padrões - `guias/vol11/guia065-grep-e-a-busca-de-padroes.html`
- [x] **guia 066** - sed: o editor de fluxo - `guias/vol11/guia066-sed-o-editor-de-fluxo.html`
- [x] **guia 067** - awk: processamento por campos e registros - `guias/vol11/guia067-awk-processamento-por-campos-e-registros.html`
- [x] **guia 068** - cut, sort, uniq, tr e a caixa de ferramentas de texto - `guias/vol11/guia068-cut-sort-uniq-tr-e-a-caixa-de-ferramentas-de-tex.html`
- [x] **guia 069** - Dados estruturados: jq, JSON e CSV - `guias/vol11/guia069-dados-estruturados-jq-json-e-csv.html`
- [x] **guia 070** - Juntando tudo: pipelines de processamento de dados - `guias/vol11/guia070-juntando-tudo-pipelines-de-processamento-de-dado.html`

### Volume 12 — Scripting Avançado e Robusto

- [x] **guia 071** - Tratamento de erros: set -euo pipefail e traps - `guias/vol12/guia071-tratamento-de-erros-set-euo-pipefail-e-traps.html`
- [x] **guia 072** - Depuração de scripts: set -x e ShellCheck - `guias/vol12/guia072-depuracao-de-scripts-set-x-e-shellcheck.html`
- [x] **guia 073** - Arquivos, descritores e processos em scripts - `guias/vol12/guia073-arquivos-descritores-e-processos-em-scripts.html`
- [x] **guia 074** - Subshells, agrupamento e here-documents - `guias/vol12/guia074-subshells-agrupamento-e-here-documents.html`
- [x] **guia 075** - Sinais, processos filhos e execução em paralelo - `guias/vol12/guia075-sinais-processos-filhos-e-execucao-em-paralelo.html`
- [x] **guia 076** - Interação: menus, cores e caixas de diálogo - `guias/vol12/guia076-interacao-menus-cores-e-caixas-de-dialogo.html`
- [x] **guia 077** - Estruturando scripts grandes e bibliotecas - `guias/vol12/guia077-estruturando-scripts-grandes-e-bibliotecas.html`

## Fase 4 — Redes, Segurança e Automação

### Volume 13 — Redes no Linux

- [x] **guia 078** - Fundamentos: interfaces, IP e a pilha de rede - `guias/vol13/guia078-fundamentos-interfaces-ip-e-a-pilha-de-rede.html`
- [x] **guia 079** - Configuração de rede: ip, NetworkManager e arquivos - `guias/vol13/guia079-configuracao-de-rede-ip-networkmanager-e-arquivo.html`
- [x] **guia 080** - Diagnóstico: ping, traceroute, ss, dig e mtr - `guias/vol13/guia080-diagnostico-ping-traceroute-ss-dig-e-mtr.html`
- [x] **guia 081** - Acesso remoto: SSH, scp e rsync - `guias/vol13/guia081-acesso-remoto-ssh-scp-e-rsync.html`
- [x] **guia 082** - HTTP na linha de comando: curl, wget e netcat - `guias/vol13/guia082-http-na-linha-de-comando-curl-wget-e-netcat.html`
- [x] **guia 083** - Firewall no Linux: nftables e iptables - `guias/vol13/guia083-firewall-no-linux-nftables-e-iptables.html`
- [x] **guia 084** - Captura de tráfego: tcpdump e tshark - `guias/vol13/guia084-captura-de-trafego-tcpdump-e-tshark.html`

### Volume 14 — Segurança e o Ambiente Kali

- [x] **guia 085** - Hardening do Linux: superfície de ataque e princípios - `guias/vol14/guia085-hardening-do-linux-superficie-de-ataque-e-princi.html`
- [x] **guia 086** - Gerenciamento de segredos: chaves SSH e GPG - `guias/vol14/guia086-gerenciamento-de-segredos-chaves-ssh-e-gpg.html`
- [x] **guia 087** - Capabilities, isolamento e menor privilégio - `guias/vol14/guia087-capabilities-isolamento-e-menor-privilegio.html`
- [x] **guia 088** - Confinamento: AppArmor, SELinux e sandboxing - `guias/vol14/guia088-confinamento-apparmor-selinux-e-sandboxing.html`
- [x] **guia 089** - Auditoria, integridade e detecção de alterações - `guias/vol14/guia089-auditoria-integridade-e-deteccao-de-alteracoes.html`
- [x] **guia 090** - O ecossistema de ferramentas do Kali: categorias e fluxos - `guias/vol14/guia090-o-ecossistema-de-ferramentas-do-kali-categorias-.html`
- [ ] **guia 091** - Anonimato e privacidade: proxychains, Tor e VPN - `guias/vol14/guia091-anonimato-e-privacidade-proxychains-tor-e-vpn.html`

### Volume 15 — Automação e Produtividade

- [ ] **guia 092** - Personalizando o shell: .bashrc, aliases e funções - `guias/vol15/guia092-personalizando-o-shell-bashrc-aliases-e-funcoes.html`
- [ ] **guia 093** - Zsh, plugins e o prompt do Kali - `guias/vol15/guia093-zsh-plugins-e-o-prompt-do-kali.html`
- [ ] **guia 094** - Automatizando tarefas com cron e scripts agendados - `guias/vol15/guia094-automatizando-tarefas-com-cron-e-scripts-agendad.html`
- [ ] **guia 095** - Controle de versão com Git na linha de comando - `guias/vol15/guia095-controle-de-versao-com-git-na-linha-de-comando.html`
- [ ] **guia 096** - Editores no terminal: vim e nano - `guias/vol15/guia096-editores-no-terminal-vim-e-nano.html`
- [ ] **guia 097** - Dotfiles e ambientes reproduzíveis - `guias/vol15/guia097-dotfiles-e-ambientes-reproduziveis.html`

## Fase 5 — Fronteira e Aprofundamento

### Volume 16 — Kernel, Contêineres e Virtualização

- [ ] **guia 098** - O kernel Linux: módulos, /proc e /sys - `guias/vol16/guia098-o-kernel-linux-modulos-proc-e-sys.html`
- [ ] **guia 099** - Contêineres por dentro: namespaces, cgroups e Docker - `guias/vol16/guia099-conteineres-por-dentro-namespaces-cgroups-e-dock.html`
- [ ] **guia 100** - Virtualização: KVM, QEMU e o laboratório de estudos - `guias/vol16/guia100-virtualizacao-kvm-qemu-e-o-laboratorio-de-estudo.html`
- [ ] **guia 101** - Compilação, toolchains e o ecossistema de dev - `guias/vol16/guia101-compilacao-toolchains-e-o-ecossistema-de-dev.html`
- [ ] **guia 102** - Observabilidade e desempenho: strace, ltrace e perf - `guias/vol16/guia102-observabilidade-e-desempenho-strace-ltrace-e-per.html`
- [ ] **guia 103** - Para onde ir depois: certificações, comunidade e prática - `guias/vol16/guia103-para-onde-ir-depois-certificacoes-comunidade-e-p.html`
