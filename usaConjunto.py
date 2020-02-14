import Conjuntos

c = Conjuntos.Conjunto('teste')
d = Conjuntos.Conjunto('in')

conjunto_numeros1 = Conjunto("B", 1, 2, 3)
conjunto_numeros = Conjunto("B", 1, 2, 3)
conjunto_letras = Conjunto("C", 'd', "e", "g")
conjunto_mesclado = Conjunto(
    "A", conjunto_numeros, "a", "c", conjunto_letras)

conjunto_mesclado.imprimir()
#print(conjunto_mesclado.pertence(2))
print(conjunto_numeros1.contem(conjunto_numeros))
