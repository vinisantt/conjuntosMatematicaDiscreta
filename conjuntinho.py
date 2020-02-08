class Conjunto:
    def __init__(self, nome, *elementos):
        self.nome = nome
        self.elementos = []
        for i in elementos:
            if i not in self.elementos:
                self.elementos.append(i)

    def imprimir(self):
        conjunto = self.nome + " = {" + f"{self.elementos}" + \
            "}"
        # verificar se é do tipo objeto, se for chamar o metodo imprimir
        conjunto = conjunto.replace("[", "").replace("]", "").replace("'", "")

        print(conjunto)

    def inserir(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def tamanho(self):
        return len(self.elementos)
