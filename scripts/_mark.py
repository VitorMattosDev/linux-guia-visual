import io,sys
p="ROADMAP.md"
s=io.open(p,encoding="utf-8").read()
for n in sys.argv[1:]:
    s=s.replace("- [ ] **guia %s**"%n, "- [x] **guia %s**"%n)
io.open(p,"w",encoding="utf-8",newline="\n").write(s)
