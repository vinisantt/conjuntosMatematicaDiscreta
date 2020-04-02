#from pylatex import Document, Section
import Conjuntos

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, 3)
B = Conjunto("B", 4, 5, 6)

# AIB = A.intersecao(B)

# AIB.imprimir()

X = Conjunto("X", 5, {1, 2}, 4, 3)
Z = Conjunto("Z", 1, 4, {}, {1, 2})

# Y = X.diferenca(Z)
# Y.imprimir()

# V = X.complementar(Z)
# V.imprimir()

X.conjuntoDasPartes()
