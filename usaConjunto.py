# from pylatex import Document, Section
import Conjuntos
from Conjuntos import operacoes

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, (2, 9))
B = Conjunto("B", (2, 9))

print(A.contemProp(B))


# B = Conjunto("B", 4, 5, 6)
# AIB = A.intersecao(B)

# AIB.imprimir()

# X = Conjunto("X", 4, 5)
# Z = Conjunto("Z", 5, 6)

# Y = X.diferenca(Z)
# Y.imprimir()

# V = X.complementar(Z)
# V.imprimir()

# X.diferenca(Z).imprimir()
