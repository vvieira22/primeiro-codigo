#Compreensão de lista
""" A compreensão de lista em Python é uma maneira 
compacta de criar uma lista a partir de uma sequência.

IMPORTANTE!!!!
A compreensão da lista é consideravelmente mais rápida do que processar 
uma lista usando o loop for . """

#Syntax
#     [i for i in iterable if expression]

#Por exemplo, splitar uma string em lista
from random import randint

string_exp = "python"
lista = [i for i in string_exp]
print(lista)

#Exemplo 2, gerar uma lista de numeros
lista = [i for i in range(11)]

#E possivel ainda realizar calculos matematicos ainda dentro do listc.
lista_multiplicada = [i*2 for i in range(11)]

#E ainda e possivel fazer uma lista de tuplas.
lista_tupla_numero_e_seu_dobro = [(i,i*2) for i in range(11)]

#A compreenção de lista pode ser combinada com a expressao if
lista_pares_de_0_a_100 = [i for i in range(100) if i%2==0]


#FUNÇÃO LAMBDA
""" Lambda function é uma função anonima, que o usuario nao precisa definir como funcao
nao vai escrever a funcao depois de utilizar. Pode receber multiplos argumentos mas
so pode ter uma expressao. """

# Criando lambda
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(1, 2, 3))

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

#Se auto chamando a funcao lambda
# Self invoking lambda function
print((lambda a, b: a + b)(2,3)) #==5

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

#Função lambda dentro de outra função
def power(x):
    return lambda n : x ** n
cube = power(2)(3) #function power now need 2 arguments to run, in separate rounded brackets