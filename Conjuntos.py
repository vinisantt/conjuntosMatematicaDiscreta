operacoes = {}


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
            if type(elemento) == str or type(elemento) == int:
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
        expressoes = {'{': '\\{', '}': '\\}'}
        formulaLatex = ''
        for i in conjunto:
            if i in expressoes:
                formulaLatex += expressoes[i]
            else:
                formulaLatex += i
        print(f"${formulaLatex}$")
        return formulaLatex

    def estaVazio(self):
        return self.tamanho() == 0

    def uniao(self, conjunto):
        unido = Conjunto(f"{self.nome} U {conjunto.nome}")

        if unido.nome not in operacoes and unido.nome[::-1] not in operacoes:
            if not conjunto.estaVazio() and not self.estaVazio():
                if conjunto.tamanho() > self.tamanho():
                    unido.elementos = conjunto.elementos
                    for element in self.elementos:
                        unido.inserir(element)

                else:
                    unido.elementos = self.elementos
                    for element in conjunto.elementos:
                        unido.inserir(element)

            operacoes[f"{self.nome} U {conjunto.nome}"] = unido
            print("teste")
        print(operacoes)
        try:
            return operacoes[unido.nome]
        except KeyError:
            return operacoes[unido.nome[::-1]]

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
