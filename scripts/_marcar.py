import io,sys
p='ROADMAP.md'
s=io.open(p,encoding='utf-8').read()
for n in sys.argv[1:]:
    a='- [ ] **guia %s**'%n; b='- [x] **guia %s**'%n
    assert a in s, n
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8',newline='\n').write(s)
