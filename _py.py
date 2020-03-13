# Criar listinha de conjuntos // classe que controla tudo que vai acontecer
# Deixar a classe conjunto como model, e as funções na classe Deus


# Ex: superClass para controlar quem faz o que, um gerente
class managerClass:

    listaDeConjuntos = []
    operacoesFeitas = {}

    def criarConjunto(self, nome, *elementos)

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

    def atualizaoperacoesFeitas(self, nome):
        remove = []
        for operacao in operacoesFeitas:
            if nome in operacao:
                remove.append(operacao)

        for i in remove:
            operacoesFeitas.pop(i)
        print(operacoesFeitas)

    def inserir(self, elemento, o=False):
        if o == False:
            if elemento not in self.elementos:
                self.elementos.append(elemento)
                self.atualizaoperacoesFeitas(self.nome)
        else:
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

    def igual(self, conjunto):
        if self.tamanho() == conjunto.tamanho():
            return self.contem(conjunto)
        return False

    def uniao(self, conjunto):
        unido = Conjunto(f"{self.nome} U {conjunto.nome}")

        if self.igual(conjunto):
            unido.elementos = self.elementos
            operacoesFeitas[f"{self.nome} U {conjunto.nome}"] = unido

        elif unido.nome not in operacoesFeitas and unido.nome[::-1] not in operacoesFeitas:
            if not conjunto.estaVazio() and not self.estaVazio():
                if conjunto.tamanho() > self.tamanho():
                    unido.elementos = conjunto.elementos
                    for elemento in self.elementos:
                        unido.inserir(elemento, True)
                else:
                    unido.elementos = self.elementos
                    for elemento in conjunto.elementos:
                        unido.inserir(elemento, True)
            operacoesFeitas[f"{self.nome} U {conjunto.nome}"] = unido

        try:
            return operacoesFeitas[unido.nome]
        except KeyError:
            return operacoesFeitas[unido.nome[::-1]]

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
