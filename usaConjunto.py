import conjuntinho

Conjunto = conjuntinho.Conjunto

conjunto_toper = Conjunto("B", 1, 2, 3)
conjunto_de_inteiros = Conjunto("A", "a", conjunto_toper, "c")


# conjunto_de_inteiros.imprimir()

# conjunto_de_inteiros.inserir(2)
# conjunto_de_inteiros.inserir(2)
conjunto_de_inteiros.imprimir()

print(conjunto_de_inteiros.tamanho())
