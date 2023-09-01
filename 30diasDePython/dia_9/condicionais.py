#Condicionais

# Por padrão, as instruções no script Python são executadas sequencialmente de cima para baixo.

#Execucao condicional: um bloco de instrucoes ou expressao for verdadeira.
#Repetitiva: execucao repetidamente até um fim com expressao de saida.

#IF CONDITION
'''syntax
if condition:
    this part of code runs for truthy conditions
'''
if 2>1:
    print("sim")


#ELSE CONDITION
#se a condicao do primeiro bloco for falsa ele executara o else
if 1>2:
    print("sim")
else:
    print("nao")

#Elif (elsif)    
#Multiplas condicoes
"""
# syntax
if condition:
    code
elif condition:
    code
else:
    code
"""

#Short Hand - ternary operator
#   code if condition else code

print("é par") if 11%2==0 else print("é impar")


#Nested Conditions
#Condicao dentro da outra
# syntax
"""
    if condition:
        code
        if condition:
            code
"""

"""If com operadores Lógicos
&& = and
|| = or
"""
if(1+1==2) and (2-1==1):
    print("correto")

if(1+1==2) or (2-1=="1"):
    print("correto")