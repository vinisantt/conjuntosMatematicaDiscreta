# A API Conjunto foi desenvolvida para resolver as operações da Teoria de Conjuntos

## Funcionalidades:
- Inserir um Conjunto
- Inserir um Elemento em um Conjunto
- Imprimir um Conjunto
- Obter o tamanho de um Conjunto
- Identificar se um conjunto contém um Elemento
- Identificar se um Conjunto é Subconjunto de outro
- Identificar se um Conjunto é Subconjunto próprio de outro
- União de Conjuntos
- Interseção de Conjuntos
- Encontrar o complemento de um Conjunto
- Obter a diferença entre dois Conjuntos
- Encontrar o Conjunto das partes de um Conjunto

## Baixando a API e dependências.
- Fazer o clone do repositório:
```
git clone
```
- Instalar a biblioteca pylatex:
```
pip install pylatex
```

# Exemplos de utilização:
Para usar a API, abra o arquivo `usaConjunto.py` em um editor de código de sua preferencia.
Como descrito acima a API disponibiliza alguma funcionalidades que resolvem algumas operações da Teoria de Conjuntos.

Um Conjunto é uma estrutura que agrupa objetos e constitui uma base para construir estruturas mais complexas.
Segue uma definição mais formal: Um conjunto é uma coleção de zero ou mais objetos distintos, chamados elementos do conjunto, os quais não possuem qualquer ordem associada. Dessa forma, os elementos (que podem ser qualquer coisa: números, pessoas, frutas) são indicados por letra minúscula e definidos como um dos componentes do conjunto.
Um Conjunto também tem como componente um nome e tamanho. Os elementos de um Conjunto são separados por vírgula e normalmente dentro de chaves, como por exemplo: `A = {a, e, i o ,u}`.

## Inserir um Conjunto:
Para inserir um novo Conjunto deve-se adicionar uma variável que vai receber a instância de um novo objeto do tipo Conjunto, como parâmetro do objeto deve ser passado o Nome seguido dos Elementos do Conjunto.
### Exemplo:
```
A = Conjunto("A", 5, 3, 1)
```
*Os Elementos de um Conjunto não se repetem, então essa funcionalidade além de adicionar um novo Conjunto, ela também verifica se o próximo Elemento Contém no Conjunto que está sendo criado.*

## Inserir um Elemento em um Conjunto:
Antes de inserir um Elemento em um Conjunto, primeiro deve ter sido criado um elemento antes, como é demonstrado em Inserir um Conjunto. Com o conjunto criado vamos chamar a função inserir() na variável que o Conjunto foi instanciado e passar como parâmetro os elementos que deseja adicionar
### Exemplo:
```
A.inserir(4)
```
*Os Elementos de um Conjunto não se repetem, então essa funcionalidade além de adicionar os novos Elementos no Conjunto, ela também verifica se o Elemento Contém no conjunto.*

## Imprimir um Conjunto:
Para visualizar o Conjunto basta chamar a função imprimir(), ela não requer nenhum parâmetro e retorna a impressão do Conjunto.
### Exemplo:
```
A = Conjunto("A", 5, 3, 1)
A.imprimir()
```
#### Retorno:
```
A = {5, 3, 1}
```

## Obter tamanho de um Conjunto: 
Para obtermos o tamanho de conjunto basta chamar a função tamanho, ela não requer nenhum parâmetro e retorna a quantidade de elementos que o Conjunto que está chamando possui.
### Exemplo: 
```
A = Conjunto(“A”, 3, 4, 5)
A.tamanho()
```
#### Retorno:
`3`

## Identificar se um Conjunto contém um elemento:
Para verificarmos se um elemento pertence à outro precisamos utilizar a função pertence, passando como parâmetro o elemento no qual deseja verificar, ao fazer isso, esta funcionalidade percorre sua lista de elementos à procura de um que seja igual ao elemento passado como parâmetro, caso encontre, retorna True (verdadeiro), caso não, retorna False (falso).
### Exemplo:
```
A = Conjunto(“A”, 3, 4, 5)
A.pertence(5)
```
#### Retorno:
`True`

## Identificar se um Conjunto é Subconjunto de outro
Para verificar se um Conjunto é Subconjunto de outro Conjunto, deve chamar a função contem(), e passar como parâmetro um Conjunto ao qual deseja verificar se é um Subconjunto do Conjunto instanciado. Essa função retorna um boolean, se o Conjunto passado no parâmetro for Subconjunto do Conjunto instanciado, retornar true, caso contrário retorna false.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, {2, 9})
B = Conjunto("B", {2, 9})
A.contem(B)
```
#### Retorno:
`True`
*Para definir se um Conjunto é Subconjunto de um outro Conjunto deve verificar Se todos os elementos de um conjunto 𝐴 também são elementos de um conjunto 𝐵, então 𝐴 está contido em 𝐵, o que é representado por: 𝐴 ⊆ 𝐵. Isso também é lido como 𝐴 é subconjunto de 𝐵.*

## Identificar se um Conjunto é Subconjunto próprio de outro:
Para verificar se um Conjunto  é Subconjunto próprio de outro, utilizamos a função contemProp, que recebe como parâmetro um Conjunto, que ao ser chamada verifica primeiramente se o Conjunto passado é um subconjunto do elemento que chamou a função utilizando a função contem(Conjunto), caso não seja já retorna False (falso), caso não verifica se o tamanho dos dois conjuntos são iguais, caso seja, retorna False (falso), caso não retorna True (verdadeiro, é um subconjunto próprio).
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, {2, 9})
B = Conjunto("B", {2, 9})
A.contemProp(B)
B.contemProp(A)
```
#### Retorno: 
```
True
False
```
*Um subconjunto próprio é quando um Conjunto é subconjunto de outro e há alguma diferença entre a quantidade de elementos do Conjunto que chama a função com o Conjunto passado como parâmetro.*
