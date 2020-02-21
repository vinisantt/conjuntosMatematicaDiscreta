class Conjunto:
    def __init__(self, nome, *elementos):
        self.nome = nome
        self.elementos = []
        for i in elementos:
            if i not in self.elementos:
                self.elementos.append(i)
 
    def imprimir(self) -> str:
        conjunto = self.nome + " = {"
        for elemento in self.elementos:
            if type(elemento) == str:
                conjunto += str(elemento) + ","
            else:
                conjunto += "{" + str(elemento.elementos) + "},"

        if conjunto[-1] == ',':
            conjunto = conjunto[:-1]

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "") + "}"

        print(conjunto)
        return conjunto

    def inserir(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def tamanho(self) -> int:
        return len(self.elementos)

    def pertence(self, elemento):
        return elemento in self.elementos
    
    def contem(self, cg) -> bool:
        if self.tamanho() < cg.tamanho():
            return False
        else:
            for elemento in cg.elementos:
                if elemento not in self.elementos:
                    return False
            return True

    def contemProp(self, cg) -> bool:
        if self.contem(cg):
            return self.tamanho() > cg.tamanho()            
        return False
    
    def imprimirLatex(self):
        conjunto = self.imprimir()
        expressoes = {'{':'\\{','}':'\\}'}
        formulaLatex = ''
        for i in conjunto:
            if i in expressoes:
                formulaLatex += expressoes[i]
            else:
                formulaLatex += i
        print(f"${formulaLatex}$")
        return formulaLatex


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
