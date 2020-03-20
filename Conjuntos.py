# Criar listinha de conjuntos // classe que controla tudo que vai acontecer
# Ex: superClass para controlar quem faz o que, um gerente
# class superClass:
#   criarConjunto()
#   listaDeConjuntos = []
#   operacoesFeitas = {}

operacoes = {}  # Operações feitas são guardadas aqui, para motivos de otimização

# Deixar a classe conjunto como model, e as funções na classe Deus


class Conjunto:
    def __init__(self, nome, *elementos):
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
                conjunto += "{" + str(elemento.elementos) + "},"

        if conjunto[-1] == ',':
            conjunto = conjunto[:-1]

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "") + "}"

        if operacao:
            return conjunto
        print(conjunto)

    def atualizaOperacoes(self, nome):
        remove = []
        for operacao in operacoes:
            if nome in operacao:
                remove.append(operacao)

        for i in remove:
            operacoes.pop(i)

    def inserir(self, elemento, o=False):
        if o == False:
            if elemento not in self.elementos:
                self.elementos.append(elemento)
                self.atualizaOperacoes(self.nome)
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

    def estaVazio(self):
        return self.tamanho() == 0

    def igual(self, conjunto):
        if self.tamanho() == conjunto.tamanho():
            return self.contem(conjunto)
        return False

    def uniao(self, conjunto):
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

    def intersecao(self,conjunto):
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

                
