#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
estrutura.py — Estrutura canônica do GUIA VISUAL LINUX.

Fonte única da verdade: os 103 guias, 16 volumes, 5 fases, espelhados
1:1 dos capítulos do "Manual de Linux e Shell Scripting".

Uso:
    python scripts/estrutura.py --stubs     # cria HTML faltantes a partir do template
    python scripts/estrutura.py --roadmap   # reescreve ROADMAP.md (preserva [x]/[~])
    python scripts/estrutura.py --tudo       # stubs + roadmap
    python scripts/estrutura.py --lista      # imprime a fila

Regra de ouro (herdada do manual): --roadmap e --tudo PRESERVAM os
marcadores [x] e [~] relendo o ROADMAP.md antes de reescrever. Não
altere o formato da linha `- [x] **guia NNN**` ou o regex para de casar.
Na dúvida, use só --stubs.
"""
import re, sys, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TEMPLATE = RAIZ / "template" / "guia-template.html"
ROADMAP = RAIZ / "ROADMAP.md"

def _achar_manual():
    """Localiza a pasta do manual-fonte (só leitura). Espelha o padrão do PC:
    manual-linux-master é irmã de GUIA VISUAL LINUX. Ordem de tentativa:
    ../manual-linux-master, ./manual-linux-master, ./fonte."""
    for c in (RAIZ.parent/"manual-linux-master", RAIZ/"manual-linux-master", RAIZ/"fonte"):
        if c.is_dir():
            return c
    return RAIZ.parent/"manual-linux-master"   # esperado, mesmo se ainda não existir

MANUAL = _achar_manual()

def fonte_de(num, vol):
    """Caminho do capítulo-fonte .qmd para o guia `num` (cap == guia)."""
    achados = sorted((MANUAL/f"vol{vol:02d}").glob(f"cap{num:03d}-*.qmd"))
    return achados[0] if achados else None

# (fase, volume_num, volume_titulo, [(num, titulo), ...])
FASES = [
 ("Fase 1 — Fundamentos do Linux", [
   (1, "Primeiros Passos: Linux e Kali", [
     (1,"O que é Linux: kernel, distribuições e software livre"),
     (2,"Por que Kali Linux: propósito, filosofia e quando não usá-lo"),
     (3,"Instalando o Kali: VM, bare metal, WSL e live USB"),
     (4,"Primeiro contato: sessão, ambiente Xfce e organização"),
     (5,"A estrutura de diretórios do Linux (FHS)"),
     (6,"Anatomia de um comando: shell, argumentos e opções"),
     (7,"Obtendo ajuda: man, info, tldr e a doc do Kali")]),
   (2, "O Terminal e o Shell", [
     (8,"Emulador de terminal e shell: bash, zsh e o padrão do Kali"),
     (9,"Navegação: pwd, cd, ls e caminhos absolutos e relativos"),
     (10,"Manipulando arquivos e diretórios: cp, mv, rm, mkdir"),
     (11,"Visualizando conteúdo: cat, less, head, tail e more"),
     (12,"Redirecionamento e pipes: stdin, stdout e stderr"),
     (13,"Curingas, globbing e expansão de chaves"),
     (14,"Histórico, atalhos de teclado e produtividade")]),
   (3, "Arquivos e o Sistema de Arquivos", [
     (15,"Tipos de arquivo, inodes e a árvore de diretórios"),
     (16,"Links simbólicos e hard links"),
     (17,"Localizando arquivos: find, locate, which e type"),
     (18,"Compactação e arquivamento: tar, gzip, xz e zip"),
     (19,"Montagem de dispositivos e o comando mount"),
     (20,"Permissões de arquivo: leitura, escrita e execução")]),
   (4, "Usuários, Grupos e Permissões", [
     (21,"Usuários, grupos e o arquivo /etc/passwd"),
     (22,"O root, sudo e a elevação de privilégios"),
     (23,"Permissões especiais: SUID, SGID e sticky bit"),
     (24,"ACLs e atributos estendidos de arquivo"),
     (25,"Gerenciamento de usuários, senhas e o PAM"),
     (26,"Trabalhando como root no Kali com segurança")]),
 ]),
 ("Fase 2 — Administração do Sistema", [
   (5, "Processos e Controle de Tarefas", [
     (27,"O que é um processo: PID, estados e a árvore"),
     (28,"Monitoramento: ps, top e htop"),
     (29,"Sinais e controle: kill, killall, nice e prioridades"),
     (30,"Jobs, primeiro e segundo plano, nohup e disown"),
     (31,"Multiplexação de terminal: tmux e screen"),
     (32,"Recursos do sistema: memória, CPU, uptime e limites")]),
   (6, "Gerenciamento de Pacotes", [
     (33,"APT e o modelo Debian: repositórios e o Kali rolling"),
     (34,"Instalando, removendo e atualizando pacotes com apt"),
     (35,"dpkg, arquivos .deb e resolução de dependências"),
     (36,"Repositórios do Kali, metapacotes e kali-tweaks"),
     (37,"Compilando a partir do código-fonte"),
     (38,"Alternativas: pipx, snap, flatpak e AppImage")]),
   (7, "Boot, systemd e Serviços", [
     (39,"O processo de inicialização: UEFI, GRUB e o kernel"),
     (40,"systemd: units, targets e o modelo de serviços"),
     (41,"Gerenciando serviços com systemctl"),
     (42,"Logs com journald e o syslog tradicional"),
     (43,"Agendamento: cron, at e timers do systemd"),
     (44,"Targets, recuperação e problemas de boot")]),
   (8, "Armazenamento e Sistemas de Arquivos", [
     (45,"Discos, partições e a nomenclatura de dispositivos"),
     (46,"Particionamento com fdisk, parted e gdisk"),
     (47,"Sistemas de arquivos: ext4, Btrfs, XFS e formatação"),
     (48,"LVM: volumes lógicos flexíveis"),
     (49,"RAID por software com mdadm"),
     (50,"Criptografia de disco com LUKS e persistência no Kali")]),
 ]),
 ("Fase 3 — Shell Scripting", [
   (9, "Fundamentos de Shell Scripting", [
     (51,"Do comando ao script: o primeiro script Bash"),
     (52,"Variáveis, o ambiente e o escopo de exportação"),
     (53,"Aspas, expansões e substituição de comandos"),
     (54,"Entrada e saída: read, echo e printf"),
     (55,"Condicionais: test, colchetes duplos e if"),
     (56,"Códigos de saída e o encadeamento de comandos"),
     (57,"Boas práticas: shebang, permissões e portabilidade")]),
   (10, "Scripting Intermediário", [
     (58,"Laços: for, while e until"),
     (59,"Funções, retorno e escopo de variáveis"),
     (60,"Arrays indexados e associativos"),
     (61,"Parâmetros posicionais e getopts"),
     (62,"Expansão de parâmetros avançada"),
     (63,"Aritmética e manipulação de números no shell")]),
   (11, "Processamento de Texto", [
     (64,"Expressões regulares: fundamentos e sabores"),
     (65,"grep e a busca de padrões"),
     (66,"sed: o editor de fluxo"),
     (67,"awk: processamento por campos e registros"),
     (68,"cut, sort, uniq, tr e a caixa de ferramentas de texto"),
     (69,"Dados estruturados: jq, JSON e CSV"),
     (70,"Juntando tudo: pipelines de processamento de dados")]),
   (12, "Scripting Avançado e Robusto", [
     (71,"Tratamento de erros: set -euo pipefail e traps"),
     (72,"Depuração de scripts: set -x e ShellCheck"),
     (73,"Arquivos, descritores e processos em scripts"),
     (74,"Subshells, agrupamento e here-documents"),
     (75,"Sinais, processos filhos e execução em paralelo"),
     (76,"Interação: menus, cores e caixas de diálogo"),
     (77,"Estruturando scripts grandes e bibliotecas")]),
 ]),
 ("Fase 4 — Redes, Segurança e Automação", [
   (13, "Redes no Linux", [
     (78,"Fundamentos: interfaces, IP e a pilha de rede"),
     (79,"Configuração de rede: ip, NetworkManager e arquivos"),
     (80,"Diagnóstico: ping, traceroute, ss, dig e mtr"),
     (81,"Acesso remoto: SSH, scp e rsync"),
     (82,"HTTP na linha de comando: curl, wget e netcat"),
     (83,"Firewall no Linux: nftables e iptables"),
     (84,"Captura de tráfego: tcpdump e tshark")]),
   (14, "Segurança e o Ambiente Kali", [
     (85,"Hardening do Linux: superfície de ataque e princípios"),
     (86,"Gerenciamento de segredos: chaves SSH e GPG"),
     (87,"Capabilities, isolamento e menor privilégio"),
     (88,"Confinamento: AppArmor, SELinux e sandboxing"),
     (89,"Auditoria, integridade e detecção de alterações"),
     (90,"O ecossistema de ferramentas do Kali: categorias e fluxos"),
     (91,"Anonimato e privacidade: proxychains, Tor e VPN")]),
   (15, "Automação e Produtividade", [
     (92,"Personalizando o shell: .bashrc, aliases e funções"),
     (93,"Zsh, plugins e o prompt do Kali"),
     (94,"Automatizando tarefas com cron e scripts agendados"),
     (95,"Controle de versão com Git na linha de comando"),
     (96,"Editores no terminal: vim e nano"),
     (97,"Dotfiles e ambientes reproduzíveis")]),
 ]),
 ("Fase 5 — Fronteira e Aprofundamento", [
   (16, "Kernel, Contêineres e Virtualização", [
     (98,"O kernel Linux: módulos, /proc e /sys"),
     (99,"Contêineres por dentro: namespaces, cgroups e Docker"),
     (100,"Virtualização: KVM, QEMU e o laboratório de estudos"),
     (101,"Compilação, toolchains e o ecossistema de dev"),
     (102,"Observabilidade e desempenho: strace, ltrace e perf"),
     (103,"Para onde ir depois: certificações, comunidade e prática")]),
 ]),
]

def slug(txt):
    txt = unicodedata.normalize("NFKD", txt).encode("ascii","ignore").decode()
    txt = re.sub(r"[^a-zA-Z0-9]+","-", txt).strip("-").lower()
    return re.sub(r"-+","-", txt)[:48]

def caminho(vol, num, titulo):
    return RAIZ / f"vol{vol:02d}".replace("vol","guias/vol") / f"guia{num:03d}-{slug(titulo)}.html"

def iter_guias():
    for fase, vols in FASES:
        for vol, vtit, caps in vols:
            for num, tit in caps:
                yield fase, vol, vtit, num, tit

# ---- stubs ---------------------------------------------------------------
def fazer_stubs():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    criados = 0
    for fase, vol, vtit, num, tit in iter_guias():
        dest = RAIZ / f"guias/vol{vol:02d}/guia{num:03d}-{slug(tit)}.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            continue
        fase_n = fase.split("—")[0].replace("Fase","").strip()
        html = (tpl.replace("GUIA NNN — Título", f"GUIA {num:03d} — {tit}")
                   .replace("Guia Visual NNN", f"Guia Visual {num:03d}")
                   .replace("Título do<br>Assunto", tit)
                   .replace(">103<", f">{num:03d}<")
                   .replace("Vol NN · Fase N", f"Vol {vol:02d} · Fase {fase_n}")
                   .replace('class="n">NNN<', f'class="n">{num:03d}<'))
        dest.write_text(html, encoding="utf-8")
        criados += 1
    print(f"{criados} stubs criados.")

# ---- roadmap (preserva status) ------------------------------------------
def status_atuais():
    st = {}
    if ROADMAP.exists():
        for m in re.finditer(r"- \[([ x~])\] \*\*guia (\d{3})\*\*", ROADMAP.read_text(encoding="utf-8")):
            st[int(m.group(2))] = m.group(1)
    return st

def fazer_roadmap():
    st = status_atuais()
    preservados = sum(1 for v in st.values() if v in "x~")
    L = ["# ROADMAP — Guia Visual Linux","",
         "Fila autoritativa. Status: `[ ]` pendente · `[~]` em andamento · `[x]` concluído.",
         "Um guia por sessão. Commit: `guia NNN: <titulo>` com o status no mesmo commit.",""]
    for fase, vols in FASES:
        L += [f"## {fase}",""]
        for vol, vtit, caps in vols:
            L += [f"### Volume {vol} — {vtit}",""]
            for num, tit in caps:
                marca = st.get(num, " ")
                arq = f"guias/vol{vol:02d}/guia{num:03d}-{slug(tit)}.html"
                L.append(f"- [{marca}] **guia {num:03d}** - {tit} - `{arq}`")
            L.append("")
    ROADMAP.write_text("\n".join(L), encoding="utf-8")
    print(f"ROADMAP.md reescrito. {preservados} status preservados.")

def lista():
    for fase, vol, vtit, num, tit in iter_guias():
        print(f"  guia {num:03d} · vol{vol:02d} · {tit}")

def worklist(vol_alvo):
    """Imprime a fila de trabalho de UM volume: cada ficha com o destino HTML
    e o capítulo-fonte a ler. É o mapa da sessão de um volume."""
    st = status_atuais()
    achou = False
    for fase, vol, vtit, num, tit in iter_guias():
        if vol != vol_alvo:
            continue
        achou = True
        if fase not in (getattr(worklist, "_f", None),):
            pass
        dest = f"guias/vol{vol:02d}/guia{num:03d}-{slug(tit)}.html"
        src = fonte_de(num, vol)
        src_rel = src.name if src else "(fonte não encontrada)"
        marca = st.get(num, " ")
        print(f"[{marca}] guia {num:03d}  {tit}")
        print(f"      ficha : {dest}")
        print(f"      fonte : {MANUAL.name}/vol{vol:02d}/{src_rel}")
    if not achou:
        print(f"Volume {vol_alvo} não existe (use 1..16).")
    else:
        print(f"\nManual-fonte em: {MANUAL}")
        print("Após terminar o volume: python scripts/build.py --vol %d" % vol_alvo)

if __name__ == "__main__":
    args = sys.argv[1:]
    aset = set(args)
    if "--vol" in aset:
        i = args.index("--vol")
        worklist(int(args[i+1]))
    elif not args or "--lista" in aset:
        if "--stubs" not in aset and "--roadmap" not in aset and "--tudo" not in aset:
            lista()
    if "--stubs" in aset or "--tudo" in aset: fazer_stubs()
    if "--roadmap" in aset or "--tudo" in aset: fazer_roadmap()
