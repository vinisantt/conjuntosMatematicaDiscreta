import Conjuntos

c = Conjuntos.Conjunto("teste")
d = Conjuntos.Conjunto("testando")
d.inserir('a')

c.inserir('a')
c.inserir('b')
c.inserir(d)
c.imprimir()