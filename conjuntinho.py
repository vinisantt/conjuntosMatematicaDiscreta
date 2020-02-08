class Conjunto:
    def __init__(self, nome, *elementos):
        self.nome = nome
        self.elementos = []
        for i in elementos:
            if i not in self.elementos:
                self.elementos.append(i)

    def imprimir(self):
        conjunto = self.nome + " = {"
        for elemento in self.elementos:
            if type(elemento) != Conjunto:
                conjunto += str(elemento) + ","
            else:
                conjunto += "{" + str(elemento.elementos) + "},"

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "")[0:-1] + "}"

        print(conjunto)

    def inserir(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def tamanho(self):
        return len(self.elementos)
