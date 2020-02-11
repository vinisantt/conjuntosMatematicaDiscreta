import Conjuntos

Conjunto = Conjuntos.Conjunto

conjunto_numeros = Conjunto("B", 1, 2, 3)
conjunto_letras = Conjunto("C", 'd', "e", "g")
conjunto_mesclado = Conjunto(
    "A", conjunto_numeros, "a", "c", conjunto_letras)

a = conjunto_mesclado.le_arq('teste.csv')

print(a)
