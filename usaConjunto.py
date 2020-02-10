import Conjuntos

Conjunto = Conjuntos.Conjunto

conjunto_numeros = Conjunto("B", 1, 2, 3)
conjunto_letras = Conjunto("C", 'd', "e", "g")
conjunto_mesclado = Conjunto(
    "A", conjunto_numeros, "a", "c", conjunto_letras)

conjunto_mesclado.imprimir()

print(conjunto_mesclado.tamanho())
