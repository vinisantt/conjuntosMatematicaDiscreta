import Conjuntos

c = Conjuntos.Conjunto('teste')
d = Conjuntos.Conjunto('in')

d.inserir('a')
d.inserir('c')

c.inserir('a')
c.inserir('b')

c.imprimir()
d.imprimir()

print(c.contem(d))