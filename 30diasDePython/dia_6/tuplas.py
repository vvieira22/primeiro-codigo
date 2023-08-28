""" Uma tupla é uma coleção de dados ordenados e imutáveis.
São escritas com colchetes (). Depois de criada
o valor não pode ser alterado.
!!! Não podemos usar método add, insert e remove, pois ela não
é modificavel. 

Principais Métodos

> tuple()  Criar uma tupla vazia
> count()  Contar o numero d eitem especificado em uma tupla
> index()  Para encontrar o indice de um item especificado em uma tupla
    > operador: para juntar duas ou mais tuplas e criar uma nova.
"""

# Criando uma Tupla

##### Tupla vazia
empty_tuple = ()
#or using the tuple constructor
empty_tuple = tuple()

#### Tupla com valores iniciais
tpl = ('item1', 'item2', 'item3')

fruits = ('banana', 'maça', 'uva')


#Comprimento de uma tupla
print(len(fruits))  #output = 3


"""Acessando itens de uma tupla
Semelhante ao tipo de dado lista, usamos indexação positiva ou negativa
para acessar itens de uma tupla

                ('banana', 'maça', 'uva')
                    0        1       2
                            or
                ('banana', 'maça', 'uva')
                   -3        -2       -1
"""

#  Indexação positiva
fruits = ('banana', 'maça', 'uva')
first_item = fruits[0]
second_tem = fruits[1]

#ultimo indice/item
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

#  Indexação negativa
fruits = ('banana', 'maça', 'uva')
first_item = fruits[-3]
second_tem = fruits[-2]

#last item
last_fruit = fruits[-1]


#Fatiamento de Tuplas

#Podemos dividir uma subtupla setando intervalo de índices, onde começa
#e onde termina. O valor de retorno será uma tupla com itens especificados.

#Gama de índices positivos
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]          # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
#Se atente, ele sempre vai ser -1 no final, na o inclui o indice final

#Gama de índices negativos
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)



#Mudando tuplas para Listas.
#Podemos transformar tuplas em listas e vice-versa. Tupla é imutável
#se quisermos modifcar teremos que mudar para lista.

tpl  = ('item1', 'item2', 'item3')
lst = list(tpl)

fruits = ('banana', 'maça', 'uva')
fruits = list(fruits)
fruits[0] = 'morango'
print(fruits) #output (morango,maça,uva)

fruits = tuple(fruits)
print(fruits) #output (morango,maça, uva)


#Verificando um item em uma tupla
#Podemos verificar se existe item dentro de uma tupla com o operador in
#que retorna um booleano

fruits = ('banana','morango','uva')
print('melancia' in fruits) #output false


#Unindo tuplas
#Podemos juntar tuplas com operador +
fruits_1 = ('banana','morango','uva')
fruits_2 = ('pera', 'melancia')
fruits = fruits_1 + fruits_2 #output ('banana','morango','uva','pera','melancia')


#Excluindo tuplas
#Nao e possivel excluir um unico item dentro, somente a tupla inteira
#utilizando del
tpl = ('item1','item2')
del tpl