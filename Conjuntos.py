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
            if type(elemento) == str:
                conjunto += str(elemento) + ","
            else:
                conjunto += "{" + str(elemento.elementos) + "},"

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "")[0:-1] + "}"

        print(conjunto)

    def inserir(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def tamanho(self) -> int:
        return len(self.elementos)

    def pertence(self, elemento):
        return elemento in self.elementos
    
    def contem(self, *cg):
        if tamanho() < len(cg):
            return False
        else:
            for elemento in self.elementos:
                if elemento not in cg:
                    return False 
            return True

    # n sei como é pra ta no arquivo, mas fui baseado em que os conjuntos sejam
    # separados por ";"
    '''def separa_arq(self, arquivo) -> list:
        conjuntos = arquivo.split(";")
        return conjuntos

    def le_arq(self, arquivo) -> str:
        with open(arquivo, 'r') as arq:
            arq = self.separa_arq(arq.read())

        return arq
    '''
