# Criar listinha de conjuntos // classe que controla tudo que vai acontecer
# Deixar a classe conjunto como model, e as funções na classe Deus
# Ex: superClass para controlar quem faz o que, um gerente

import Conjunto

class ClasseDeus:

    listaDeConjuntos = []
    operacoesFeitas = {}

    def criarConjunto(self, nome, *elementos):
        conjunto = Conjunto.Conjunto(nome,elementos)
        return conjunto 

    def imprimir(self,conj) -> str:
        conjunto = conj.nome + " = {"
        for elemento in conj.elementos:
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
        for operacao in self.operacoesFeitas:
            if nome in operacao:
                remove.append(operacao)

        for i in remove:
            self.operacoesFeitas.pop(i)
        print(self.operacoesFeitas)

    def inserir(self, conjunto ,elemento, o=False):
        if o == False:
            if elemento not in conjunto.elementos:
                conjunto.elementos.append(elemento)
                self.atualizaoperacoesFeitas(conjunto.nome)
        else:
            if elemento not in conjunto.elementos:
                conjunto.elementos.append(elemento)

    def tamanho(self,conjunto) -> int:
        return len(conjunto.elementos)

    def pertence(self, conjunto,elemento):
        return elemento in conjunto.elementos

    def contem(self, conjunto, cg) -> bool:
        if conjunto.tamanho() < cg.tamanho():
            return False
        else:
            for elemento in cg.elementos:
                if elemento not in conjunto.elementos:
                    return False
            return True

    def contemProp(self, conjunto ,cg) -> bool:
        if conjunto.contem(cg):
            return conjunto.tamanho() > cg.tamanho()
        return False

    def imprimirLatex(self,conjunto):
        formula = conjunto.imprimir()
        expressoes = {'{': '\\{', '}': '\\}'}
        formulaLatex = ''
        for i in formula:
            if i in expressoes:
                formulaLatex += expressoes[i]
            else:
                formulaLatex += i
        print(f"${formulaLatex}$")
        return formulaLatex

    def estaVazio(self,conjunto):
        return conjunto.tamanho() == 0

    def igual(self, conjunto1 ,conjunto2):
        if conjunto1.tamanho() == conjunto2.tamanho():
            return conjunto1.contem(conjunto2)
        return False

    def uniao(self, conjunto1, conjunto2):
        unido = self.criarConjunto(f"{conjunto1.nome} U {conjunto2.nome}")

        if self.igual(conjunto1, conjunto2):
            unido.elementos = conjunto1.elementos
            self.operacoesFeitas[f"{conjunto1.nome} U {conjunto2.nome}"] = unido

        elif unido.nome not in self.operacoesFeitas and unido.nome[::-1] not in self.operacoesFeitas:
            if not conjunto2.estaVazio() and not conjunto1.estaVazio():
                if conjunto2.tamanho() > conjunto1.tamanho():
                    unido.elementos = conjunto2.elementos
                    for elemento in conjunto1.elementos:
                        self.inserir(unido, elemento, True)
                else:
                    unido.elementos = conjunto1.elementos
                    for elemento in conjunto2.elementos:
                        self.inserir(unido, elemento, True)
            self.operacoesFeitas[f"{conjunto1.nome} U {conjunto2.nome}"] = unido

        try:
            return self.operacoesFeitas[unido.nome]
        except KeyError:
            return self.operacoesFeitas[unido.nome[::-1]]
