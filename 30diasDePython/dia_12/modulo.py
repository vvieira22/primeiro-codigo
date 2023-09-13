""" O que é um módulo
Um módulo é um arquivo que contém um conjunto de códigos ou um conjunto de funções que podem ser
incluídas em uma aplicação.
Um módulo pode ser um arquivo contendo uma única variável, uma função ou uma grande base de código. """


#Importando modulo
import mymodule
print(mymodule.generate_full_name("vitor","silva"))

#Podemos importar chamando especificamente o que queremos
from mymodule import generate_full_name
generate_full_name("vitor", "silva")

#Podemos renomear a funcao importada com palavra reservada as
from mymodule import generate_full_name as genName
genName("vitor", "silva")


#Importar modulos Integrados
""" Como outras linguagens de programação, também podemos importar módulos importando o arquivo/função 
usando a palavra-chaveimport . Vamos importar o módulo comum que usaremos na maior parte do tempo. 
Alguns dos módulos integrados comuns: 
math , datetime , os , sys , random , stats , collections , json , re """
import math


#Modulo SO
""" Esse modulo é importante pois com ele podemos exectar diversas funcoes do sistema operacional
Criar, remover, alterar pastas, diretorios e manipular programas. """
import os
# Creating a directory
# os.mkdir('directory_name')


#Modulo Sistema
""" O módulo sys fornece funções e variáveis
​usadas para manipular diferentes partes do ambiente de execução Python
 """
#Se chamar o arquivo python com argumentos, podemos pegar facilmente usando esse exemplo abaixo

#O INDICE 0 É SEMPRE O PROPRIO SCRIPT, POR ISSO TA USANDO 1,2,3.....
# python meuscript.py arg1 arg2
import sys
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# Alguns comandos sys úteis:
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version


#Módulo de Estatísticas
""" O módulo de estatísticas fornece funções para estatísticas matemáticas de dados numéricos.
As funções estatísticas populares definidas neste módulo: média , mediana , modo , stdev etc. """
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# Módulo Matemático
# Módulo contendo muitas operações matemáticas e constantes.
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function

""" Agora importamos o módulo matemático que contém muitas funções que podem nos ajudar a realizar cálculos matemáticos. 
Para verificar quais funções o módulo possui, podemos usar help(math) ou dir(math) . 
Isso exibirá as funções disponíveis no módulo. Se quisermos importar apenas uma função específica do módulo, 
importamo-la da seguinte forma: """
from math import pi
print(pi)

#Importar todo modulo de matematica
from math import *


# Módulo de cordas
# Um módulo string é um módulo útil para muitos propósitos. O exemplo abaixo mostra algum uso do módulo string.
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


#Modulo Aleatorio
""" Agora você está familiarizado com a importação de módulos. Vamos fazer mais uma importação para nos 
familiarizarmos com ele. Vamos importar o módulo random que nos dá um número aleatório entre 0 e 0,9999.... 
O módulo random tem muitas funções, mas nesta seção usaremos apenas random e randint . """

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive