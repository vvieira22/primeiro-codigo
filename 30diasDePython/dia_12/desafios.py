#1
import string
import random

def random_user_id(len):
    return "".join(random.choice(string.ascii_letters) for i in range(len))

#2
def user_id_gen_by_user():
    numero_caraceteres = int(input("caracteres: "))
    repeticao = int(input("quantidade geradas: "))

    for repeticao in range(repeticao):
        print(random_user_id(numero_caraceteres))

#3 modo inteligente, eu tinha feito com uma flag = vazio e adicionada (xxx) e um espaco
def gen_rgb():
    numbers = ["".join(random.choices(string.digits, k=3)) for _ in range(3)]
    rgb = " ".join(numbers)
    return rgb

#Nivel 2

#1
def gen_hexa_colors():
    letras = string.ascii_letters
    letras = letras[0:6]
    numeros = string.digits

    return ("#" + "".join(random.choice(letras + numeros) for _ in range(6)))

#2
from random import randint
def random_list_rgb(quantidade):
    lista = []
    for numero in range(quantidade):
        lista.append("rgb" + gen_rgb())
    return lista

#3
def generate_colors(type, quantidade):
    lista = []
    for numero in range(quantidade):
        if(type == "rgb"):
            lista.append(type + "(" + gen_rgb() + ")")
        else:
            lista.append(type + "(" + gen_hexa_colors() + ")")
    return lista

#Nivel 3

#1
def shuffle_list(lista):
    lista_nova = []
    
    while (len(lista)!= len(lista_nova)):
        elemento = random.choice(lista)
        if(elemento not in lista_nova):
            lista_nova.append(elemento)
    return lista_nova

#anternativamente return random.choices(lista, k=len(lista))
print(shuffle_list([1,2,3,4,5,6]))

#2
def nove_aleatorios_sem_repeticao():
    return random.sample(range(0, 9), 7)
print(nove_aleatorios_sem_repeticao())