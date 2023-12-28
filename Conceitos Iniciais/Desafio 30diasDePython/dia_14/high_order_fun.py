#High order functions.
'''
Toda função em python é de "primeira classe".
    -Uma função pode receber uma ou mais funções como parâmetros
    -Uma função pode ser retornada como resultado de outra função
    -Uma função pode ser modificada
    -Uma função pode ser atribuída a uma variável
'''

# Funcao como parametro
def somar_numeros(numeros):
    return sum(numeros) 

def high_order_fun(f,lst):
    somatorio = f(lst)
    return somatorio

resultado = high_order_fun(somar_numeros,[1,2,3])
print(resultado) #6


#Funcao como valor de retorno
def square(x):          # a square function
    return x ** 2
def cube(x):            # a cube function
    return x ** 3
def absolute(x):        # an absolute value function
    return x if x >= 0 else -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result) #square function.

print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


#Python Closures (fechamento)
#Em python funcao aninhada com a outra permite acessar conteudo da anterior.
def adicionar_10():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = adicionar_10()
print(closure_result(5))  # 15


#Python Decorators (decoradores python)
#É um padrão de design que permite ao usuário adicionar novas funcionalidades a um objeto sem modificar
#sua estrutura, sao geralmente chamados antes da definição de uma função que você deseja decorar.

#podemos dizer que eles são funções que modificam a funcionalidade de uma outra função, 
# eles nos ajudam a deixar o código menor e mais Pythônico

#modo classico, sem pythonismo
def func(f):
    def wrapper():
        print("Iniciada")
        f()
        print("Finalizada")
    return wrapper
def f1():
    print("Função f1() chamada!")
def f2():
    print("Função f2() chamada")

f1 = func(f1)
# f2 = func(f2)
# print(f1)
# f1()
# f2()

#like a python
#Decoramos a funcao f1 e f2 com @
#Abrir o arquivo exemplo_decorator para entender melhor.
def func(f):
    def wrapper(*args, **kwargs):
        print("Iniciada")
        f(*args, **kwargs)
        print("Finalizada")
    return wrapper
@func
def f1(x):
    print(f"O valor de x é = {x}")
@func
def f2():
    print("Função f2() chamada")
f1(2)
f2()

#Passando parametro na funcao que utiliza decorator
def dar_bom_dia(fun):
    def wrapper(para1):
        fun(para1)
        print(f"{para1}, bom dia")
    return wrapper
@dar_bom_dia
def saudar(nome):
    print(f"{nome} sua semana será maravilhosa")
# saudar("vitor")
# vitor sua semana será maravilhosa
# vitor, bom dia

#Passando parametro direto no decorator
#Ele é executado automaticamente.
def dar_bom_dia_usuario(*args, **kwargs):
    def wrapper(func):
        print(f"{kwargs['nome']}, bom dia")
        func()
    return wrapper

@dar_bom_dia_usuario(nome = "vitao")
def saudar():
    print("sua semana será maravilhosa")


#Funções integradas de ordem superior
# Algumas das funções integradas de ordem superior que abordamos nesta parte são map() , 
# filter e reduce . A função lambda pode ser passada como parâmetro e o melhor caso de uso de 
# funções lambda é em funções como mapear, filtrar e reduzir.

#Map function
'''
 O map vai aplicar uma função em cada item de uma lista de itens, ou seja, 
é um for com uma chamada da função para aplicá-la a cada item da sua lista.
 
 Ele é basicamente uma estrutura de repetição que vai aplicar uma função para cada 
 item dentro da sua lista
'''
#Exemplo pratico
#Quero adicionar imposto para cada elemento na minha lista
#modo "normal" de fazer:
precos = [1000, 1500, 1250, 2500]
precos_com_imposto = []

def adicionar_imposto(preco):
	return preco * 1.1
for preco in precos:
	precos_com_imposto.append(adicionar_imposto(preco))

#like a python, o map retorna objeto map, entao convertemos pra lst
precos_com_imposto2 = list(map(adicionar_imposto, precos))
print(precos_com_imposto2)

#outro exemplo
#adicionar +1 a cada elemento da lista
lista = [0,1,2,3,4,5,6,7,8,9]
print(list(map(lambda x : x + 1,lista)))

#converter todas string para int
lista = ["1","2","3"]
print(list(map(int,lista)))


#Filter function
# Seleciona elementos dentro de um iterável (lista,etc.) com base na saida de uma função
# especificada.
# A função vai ser aplicavel (igual map) se a função retornar true, para cada elemento.

#Em uma lista, pegar apenas os numeros pares
numeros = [1,2,3,5,6,2,6,7,2,7,9,3,2,3,6,8,9]
def numero_par(numero):
    return True if numero%2 == 0 else False
# print(list(filter(numero_par,numeros)))
#[2, 6, 2, 6, 2, 2, 6, 8]

#em uma lista de nomes, pegar apenas quem começa com a letra a
nomes = ["Pedro","Ancelma","ana clara","Maicon","Juliana","Matheus","Thiago","Ana","Anabele","Marcia",]
def nomes_com_a(nome):
    return True if nome[0].lower() == "a" else False
# print(list(filter(nomes_com_a,nomes)))
#['Ancelma', 'Ana clara', 'Ana', 'Anabele']


#Reduce function python only p3
# A reduce() aceita uma função e uma sequência, e retorna um único valor.
'''
Inicialmente, a função é chamada com os dois primeiros itens da sequência e o 
resultado é retornado.

A função é então chamada novamente com o resultado obtido na etapa 1 e o próximo 
valor da sequência.

Este processo continua se repetindo até que haja itens na sequência.
'''
#somar itens em uma lista
from  functools  import  reduce
lista = [0,1,2,3,4,5,6,7,8,9]

def somar(x1,x2): return x1+x2

print(reduce(somar,lista))
#45