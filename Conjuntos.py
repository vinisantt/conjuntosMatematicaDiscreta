# Criar listinha de conjuntos // classe que controla tudo que vai acontecer
# Ex: superClass para controlar quem faz o que, um gerente
# class superClass:
#   criarConjunto()
#   listaDeConjuntos = []
#   operacoesFeitas = {}

import itertools
from itertools import combinations

operacoes = {}  # Operações feitas são guardadas aqui, para motivos de otimização

# Deixar a classe conjunto como model, e as funções na classe Deus


class Conjunto:
    def __init__(self, nome, *elementos) -> object:
        self.nome = nome
        self.elementos = []
        for i in elementos:
            if i not in self.elementos:
                self.elementos.append(i)

    def imprimir(self, operacao=False) -> str:
        conjunto = self.nome + " = {"
        for elemento in self.elementos:
            if type(elemento) == str or type(elemento) == int:
                conjunto += str(elemento) + ","
            else:
                try:
                    conjunto += "{" + str(elemento.elementos) + "},"
                except AttributeError:
                    if len(elemento) > 0:
                        complementar = "{"
                        # necessario conversao de tipo
                        lista = list(elemento)
                        for ele in lista:
                            # caso n seja o ultimo
                            if ele != lista[-1]:
                                complementar += str(ele) + ","
                            else:
                                complementar += str(ele) + "},"
                        conjunto += complementar
                    else:
                        conjunto += "{},"

        if conjunto[-1] == ',':
            conjunto = conjunto[:-1]

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "") + "}"

        if operacao:
            return conjunto
        print(conjunto)

    def atualizaOperacoes(self, nome) -> None:
        remove = []
        for operacao in operacoes:
            if nome in operacao:
                remove.append(operacao)

        for i in remove:
            operacoes.pop(i)

    def inserir(self, elemento, operacao=False) -> None:
        if operacao == False:
            if elemento not in self.elementos:
                self.elementos.append(elemento)
                self.atualizaOperacoes(self.nome)
        else:
            if elemento not in self.elementos:
                self.elementos.append(elemento)

    def tamanho(self) -> int:
        return len(self.elementos)

    def pertence(self, elemento) -> bool:
        """
        Checa se o elemento passado pertence ao conjunto chamador.

        Parâmetros:
        - (String / int) elemento: Elemento que será verificado.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.pertence(2)

        Saída:

        - True

        """
        return elemento in self.elementos

    def contem(self, conjunto) -> bool:
        """
        Checa se o conjunto chamador contem tal conjunto.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado junto ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6)

        - A.contemProp(B)

        Saída:

        - False

        """
        if self.tamanho() < conjunto.tamanho():
            return False
        else:
            for elemento in conjunto.elementos:
                if elemento not in self.elementos:
                    return False
            return True

    def contemProp(self, conjunto) -> bool:
        """
        Checa se o conjunto chamador contem propriamente tal conjunto.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado junto ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6)

        - A.contemProp(B)

        Saída:

        - False

        """
        if self.contem(conjunto):
            return self.tamanho() > conjunto.tamanho()
        return False

    def imprimirLatex(self) -> None:
        """
        Imprime em tela o conjunto em Latex.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.imprimirLatex()

        Saída:

        - $A = \\\{1,2,3\\\}$

        """
        conjunto = self.imprimir(True)
        expressoes = {'{': '\\{', '}': '\\}'}
        formulaLatex = ''
        for i in conjunto:
            if i in expressoes:
                formulaLatex += expressoes[i]
            else:
                formulaLatex += i
        print(f"${formulaLatex}$")
        return formulaLatex

    def estaVazio(self) -> bool:
        """
        Checa se o conjunto está vazio.

        Exemplo:

        - A = Conjunto("A")

        - A.estaVazio()

        Saída:

        - True

        """
        return self.tamanho() == 0

    def igual(self, conjunto) -> bool:
        """
        Checa se um conjunto é igual ao outro.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será comparado ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6) 

        - A.igual(B)

        Saída:

        - False

        """
        if self.tamanho() == conjunto.tamanho():
            return self.contem(conjunto)
        return False

    def uniao(self, conjunto) -> object:
        """
        Une dois conjuntos, retornando um novo conjunto contendo os elementos de ambos.

        Parâmetros:
        - (Conjunto) conjunto: Os elementos deste conjunto serão unidos ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6) 

        - A.uniao(B)

        Saída:

        - Conjunto("A U B", 1, 2, 3, 4, 5, 6)

        """
        uniao = Conjunto(f"{self.nome} ∪ {conjunto.nome}")

        if self.igual(conjunto):
            uniao.elementos = self.elementos
            operacoes[f"{self.nome} ∪ {conjunto.nome}"] = uniao

        elif uniao.nome not in operacoes and uniao.nome[::-1] not in operacoes:
            if not conjunto.estaVazio() and not self.estaVazio():
                if conjunto.tamanho() > self.tamanho():
                    uniao.elementos = conjunto.elementos
                    for elemento in self.elementos:
                        uniao.inserir(elemento, True)
                else:
                    uniao.elementos = self.elementos
                    for elemento in conjunto.elementos:
                        uniao.inserir(elemento, True)
            else:
                if conjunto.estaVazio() and not self.estaVazio():
                    uniao.elementos = self.elementos
                else:
                    uniao.elementos = conjunto.elementos

            operacoes[f"{self.nome} ∪ {conjunto.nome}"] = uniao

        try:
            return operacoes[uniao.nome]
        except KeyError:
            return operacoes[uniao.nome[::-1]]

    def intersecao(self, conjunto) -> object:
        intersecao = Conjunto(f"{self.nome} ∩ {conjunto.nome}")

        if self.igual(conjunto):
            intersecao.elementos = self.elementos
            operacoes[f"{self.nome} ∩ {conjunto.nome}"] = intersecao

        elif intersecao.nome not in operacoes and intersecao.nome[::-1] not in operacoes:
            if not conjunto.estaVazio() and not self.estaVazio():
                for elemento in conjunto.elementos:
                    if self.pertence(elemento):
                        intersecao.inserir(elemento)
                operacoes[f"{self.nome} ∩ {conjunto.nome}"] = intersecao
        try:
            return operacoes[intersecao.nome]
        except KeyError:
            return operacoes[intersecao.nome[::-1]]
    
    def diferenca(self, conjunto) -> object:
        """
        Realiza a diferença entre dois conjuntos, retornando um novo conjunto com os elementos resultantes da diferença.

        Exemplo:

        - X = Conjunto("X", 4, 5)
        - Y = Conjunto("Y", 5, 6)

        - X.diferenca(Y)

        Saída:

        - Conjunto("X - Y", 4)

        """

        diferenca = Conjunto(f"{self.nome} - {conjunto.nome}")
        if(self.tamanho() > 0 and conjunto.tamanho() > 0):
            for elemento in self.elementos:
                if elemento not in conjunto.elementos:
                    diferenca.inserir(elemento, True)
        return diferenca

    def complementar(self, conjunto) -> object:
        
        if conjunto.contem(self):
            comp = self.diferenca(conjunto)
            comp.nome = f"{self.nome}^{conjunto.nome}"
            return comp
        else:
            return Conjunto(f"{self.nome}^{conjunto.nome}")

    def conjuntoDasPartes(self) -> None:
        """
        Retorna as combinações possíveis dos elementos de um conjunto.

        Exemplo:

        - X = Conjunto("X", 5, 4)

        - X.conjuntoDasPartes()

        - Saída:
        - - {}
        - - {5}
        - - {4}
        - - {5, 4}


        """

        elementos = self.elementos

        for i in range(0, len(elementos)+1):
            linha = list(itertools.combinations(elementos, i))
            for x in linha:
                try:
                    ultimo = str(x)[-2]
                    if ultimo == ',':
                        if "{" not in str(x) or "}" not in str(x):
                            print(str(x).replace(",", "").replace(
                                "(", "{").replace(")", "}"))
                        else:
                            print((str(x)[:-2] + str(x)[-1:]
                                   ).replace("(", "{").replace(")", "}"))
                    else:
                        print(str(x).replace("(", "{").replace(")", "}"))
                except IndexError:
                    pass
