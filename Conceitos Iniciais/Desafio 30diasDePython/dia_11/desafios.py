#1
def add_two_numbers(n1,n2):
    return n1+n2

#2
def area_circulo(raio):
    return 3.14 * raio * raio

#3
def add_all_nums(*args):
    soma = 0
    for num in args:
        try:
            if(int(num)):
                soma += num
        except:
                print("argumento nao numerico, passando ao proximo")
    return soma
print(add_all_nums(10.0,"rs",30))

#4
def c_to_f(cTemp):
     return ((cTemp * 9/5) + 32)

#5
def check_season(mes):
     if(mes==""):
          return "Outono"
     elif(mes==""):
        return "Inverno"
     elif(mes==""):
          return "Primavera"
     return "Verao"

#6
def calcular_slope(m,x,b):
     return m*x + b

#7
import math
def equationroots(a, b, c): 

    discri = b * b - 4 * a * c 

    sqrtval = math.sqrt(abs(discri)) 

    if discri > 0: 
        print("real and different roots") 
        print((-b + sqrtval)/(2 * a)) 
        print((-b - sqrtval)/(2 * a)) 

    elif discri == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 

    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrtval) 
        print(- b / (2 * a), " - i", sqrtval) 

#8
def print_list(list):
    for element in list:
        print(element)

#9
def print_reversed(list):
    for element in range(len(list),0,-1):
        print(element)
print_reversed([1,2,3,4])

#10
def capitalize_list_items(list):
    nova_lista = []
    for elemento in list:
        nova_lista.append(elemento.upper())

#11
def add_item(list,item):
    return list.append(item)

#12
def add_item(list,item):
    return list.remove(item)

#13
def sum_of_numbers(number):
    sum = 0
    for numero in range(number+1):
        sum += numero
    return sum


#Nivel 2

#1
def evens_and_odds(numero):
    numeros_pares = 0
    numeros_impares = 0

    if numero %2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    
    return numeros_pares,numeros_impares

#2
def fact(numero):
    fact = 1
    for i in range(1, numero+1):
        fact = fact * i
    return fact

#3
def is_empty(parm):
    return "vazio" if parm == "" else "nao vazio"

#4
from statistics import median,mode,pvariance,pstdev
from math import isnan
from itertools import filterfalse

def calcula_lista(lista):
    return sum(lista) / len(lista), median(lista), mode(lista), pvariance(lista),pstdev(lista)


#Nivel 3

#1
def is_primo(numero):
   if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, 'não é primo')
            break
    else:
        print(numero, 'é primo')

#2
def is_unique(list):
    if (len(list) == len(set(list))):
        return "nao tem elementos iguais"
    return "tem elementos iguais"

#3
def is_same_type(list):
    first_type = type(list[0])
    for elemento in list:
        if type(elemento) != first_type:
            return "diferente"

#4
from keyword import iskeyword
def is_valid(parm):
    return parm.isidentifier() and not iskeyword(parm)

#5 -1
from countries_data import ctdata

def most_spoken_languages(data):
    idiomas_mais_falados = {}

    for paises in data:
        for linguagens in paises["languages"]:
            if linguagens in idiomas_mais_falados:
                idiomas_mais_falados[linguagens] += 1
            #Primeira execucao
            else:
                idiomas_mais_falados[linguagens] = 1

    idiomas_mais_falados = sorted(idiomas_mais_falados.items(), key=lambda x:x[1],reverse=True)
    idiomas_mais_falados = dict(idiomas_mais_falados)

    contador = 0
    for chave in idiomas_mais_falados:
        print(f'{chave}: {idiomas_mais_falados[chave]} ocorrências')
        contador += 1
        if contador == 10:
            break
most_spoken_languages(ctdata)

#5 -2
def most_populated_countries(data):
    populacao = {}

    for pais in data:
        populacao[pais['name']] = pais['population']

    populacao = sorted(populacao.items(), key=lambda x:x[1],reverse=True)
    populacao = dict(populacao)
    
    contador = 0
    for chave in populacao:
        print(f'{chave}: {populacao[chave]} pessoas.')
        contador += 1
        if contador == 10:
            break
most_populated_countries(ctdata)