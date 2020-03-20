from pylatex import Document, Section
import Conjuntos

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, 3)
B = Conjunto("B", 4, 5, 6)

AIB = A.intersecao(B)

AIB.imprimir()
