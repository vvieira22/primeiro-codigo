#Loops
# 1- While loop
# 2 - For loop

#While
"""
while condition:
    do something
----------------------------
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
"""

# Break and Continue (1)
"""Podemos sair ou parar o loop na condição while quando quisermos
apenas utilizando a palavra reservada break, como exemplo:

while condition:
    code goes here
    if another_condition:
        break
"""

#Utilizando a palavra continue, pular a iteração atual e passa para proxima
#Exemplo abaixo, imprime 0,1,2, e 4, ele pula o (3)
""" 
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
"""


#For loop
# Loop usado para iterar sobre uma sequência 
# (lista, tupla, dict, conjunto, string)

#syntax
"""

for iterador in lst:
    do somtheting"
"""
#Exemplo iterando numeros na lista, printando primeiro ate ultimo elemento
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


# Break and Continue (2)
numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        break
#loop acima para de iterar quando chega a 3.

#Continue
#Continue: usamos continue quando gostamos de pular 
# algumas etapas da iteração do loop.

#Exemplo, quando for 3 ele ignora e passa pra proxima.
numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        continue
    print(number)
print('outside the loop')


#Função RANGE
"""
A função range() é usada para listar números. O intervalo (inicio,fim,passo)
leva 3 parametros, inicio, fim e incremento. Por padrao começa com 0 e
o incremento é 1. A sequencia de intervalo precisa de pelo menos 1 argumento, (fim)
Criando sequencias usando intervalo.
"""
lista = set(range(1, 11))
lista = list(range(1, 11))
print(lista)

# for iterator in range(start, end, step)

# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11


"""Loop For aninhado
# syntax
for x in y:
    for t in x:
        print(t)
"""
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#For - else
#Executar uma mensagem quando o loop for terminar, usamos else
for number in range(11):
    print(number)
else:
    print("loop acabou no numero",number)

#PASS
for numero in range(6):
    pass
"""
pass: é passar, ou seja, deixa passar, caso algum erro aconteça 
mas voce n quer que de problema, como no uso do exception.
Definição e uso
A passinstrução é usada como espaço reservado para código futuro.

Quando a passinstrução é executada, nada acontece, mas você evita um erro quando o código vazio não é permitido.

Código vazio não é permitido em loops, definições de função, definições de classe ou instruções if.
"""