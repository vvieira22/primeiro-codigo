#Tipos de erro em python:

'''
-Erro de nome - NameError
chamar ou printar uma variavel que nao existe, exemplo de retorno de erro:
print(age)
NameError: name 'age' is not defined


-Erro de índice - IndexError
lista = [1,2,3]
print(lista[8])
IndexError: list index out of range


-Modulo nao encontrado - ModuleNotFoundError
import algumodulodoido
ModuleNotFoundError: No module named 'algumodulodoido'


-Erro de Atributo - AtributoError
import math
print(math.PIS)
AttributeError: module 'math' has no attribute 'PIS'


-Erro de chave - KeyError
usuario = {name:vitor,idade:28}
usuario["profissao"]
KeyError: 'profissao'


-Erro de tipo - TypeError
print("4" + 1)
TypeError: unsupported operand type(s) for +: 'int' and 'str'


-Erro de importação - ImportError
from math import something
ImportError: cannot import name 'something' from 'math'


-Erro de valor - ValueError
int("123a")
ValueError: invalid literal for int() with base 10: '123a'


-Erro Divisao por Zero - ZeroDivisionError
1/0
ZeroDivisionError: division by zero
'''