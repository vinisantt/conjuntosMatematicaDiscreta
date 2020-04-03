#from pylatex import Document, Section
import Conjuntos
from Conjuntos import universo

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, 3)
B = Conjunto("B", 4, 5, {6, 2}, {6, {7, 5}, 2})

print(universo)

# AIB = A.intersecao(B)

# AIB.imprimir()

# X = Conjunto("X", 4, 5)
# Z = Conjunto("Z", 5, 6)

# Y = X.diferenca(Z)
# Y.imprimir()

# V = X.complementar(Z)
# V.imprimir()

# X.diferenca(Z).imprimir()
