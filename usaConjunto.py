import conjuntinho

Conjunto = conjuntinho.Conjunto

conjunto_toper = Conjunto("B", 1, 2, 3)
conjunto_de_inteiros = Conjunto("A", "a", "c", conjunto_toper)

conjunto_de_inteiros.imprimir()

print(conjunto_de_inteiros.tamanho())
