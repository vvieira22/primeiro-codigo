# Uma função é um bloco reutilizável de código ou instruções 
# de programação projetadas para executar uma determinada tarefa. 
# Para definir ou declarar uma função,Python fornece a palavra-chave def 

#create function without param
def funcao_name():
    ... #do something
funcao_name() #call function

#function with return
def funcao_somar():
    return 1+1
soma = funcao_somar() #soma = 2

#function with params (int,list,string,bool, any)
def funcao_somar_2(numero1,numero2):
    return numero1+numero2
soma = funcao_somar_2(1,2) # soma = 3

#Passando argumento key e valor
def funcao_somar_2(numero1,numero2):
    return numero1+numero2
soma = funcao_somar_2(numero1 = 1, numero2 = 2) # soma = 3

#Função com parametro padrao
def saudacao(name="{not defined}"):
    return(f'Olá {name}')
print(saudacao())
print(saudacao("Vitor"))

#Numero indefinido de Argumentos.
# Se não sabemos o número de argumentos que passamos para nossa função, podemos criar uma função que pode receber um número arbitrário de argumentos 
# adicionando * antes do nome do parâmetro.
def funcao(*args):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    ...
funcao("haha","rs",10.1,100)

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

#Função Padrão e argumentos sem limite
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))


#Função com parâmetro de outra função.
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9