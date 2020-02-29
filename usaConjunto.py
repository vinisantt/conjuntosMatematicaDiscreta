import Conjuntos
from pylatex import Document, Section

Conjunto = Conjuntos.Conjunto

conjunto_numeros1 = Conjunto("D", 1, 2, 3)
conjunto_numeros = Conjunto("B", 2, 1, 3)
conjunto_letras = Conjunto("C", 'd', "e", "g")
conjunto_mesclado = Conjunto(
    "A", conjunto_numeros, "a", "c", conjunto_letras)

unido3 = conjunto_numeros1.uniao(conjunto_numeros)


unido3.imprimir()
