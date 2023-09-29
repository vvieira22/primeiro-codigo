countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
# Mapear é simplesmente termos um iteravel e para cada elemento dele executar a função definida para esse elemento.
# Filtar é termos um iterável e caso a função correspondida para elemento do iteravel retornar true selecionar ele.
# Reduce é para um iterável, realizar operações com todos os elementos afim de ter apenas um unico resultado

#2
# Funções de ordem superior sao funcoes que tem outras funcoes dentro dela, se passam como parametro ou se retornam outra funcao.
# Fechamento, se funcao está aninhada com a outra, permite acessar conteudo da anterior.
# Decorador, é uma extensão da função, ele vai executar coisas a mais antes de executar a função "principal"

#3
#Como o enunciado esta horrivel, o 3 vou deixar queto.

#4-5-6
# for cidade in countries:
#     print(cidade)
# for nome in names:
#     print(cidade)
# for number in numbers:
#     print(number)


#LEVEL 2
#1
lista_maiscula = list(map(lambda x : x.upper(),countries))

#2
lista_quadrado = list(map(lambda x : x**2,numbers))

#3
lista_maiscula = list(map(lambda x : x.upper(),names))

#4
#modo fraco.
def land(nome):
    return True if "land" in nome else False
#modo god of war:
nomes_com_land = list(filter(lambda x: "land" in x,countries))

#5
cidade_maior_6 = list(filter(lambda x: len(x)==6,countries))

#6
cidade_maior_6 = list(filter(lambda x: len(x)>=6,countries))

#7
cidade_comeca_e = list(filter(lambda x : x[0].upper() == "E",countries))
# print(cidade_comeca_e)

#8
# A SOMA DE TODOS OS NUMEROS PARES.
from  functools  import  reduce
soma_pares = reduce(lambda x,y : x+y, filter(lambda x: x%2 == 0,numbers))
#30

#9
def get_string_lists(parametro):
    return list(filter(lambda x : isinstance(x,str),parametro))

#10
soma = reduce(lambda x,y : x+y, numbers)

#11
paises = reduce(lambda x,y : x+", "+y, countries)
# print(f"{paises} sao paises do norte da europa")

#12
from countriesdata import countries as ct
def chamadacategoria_países():
    return list(filter(lambda x : "land" or "ia" or "stand" or "ria" in x,ct))
# print(chamadacategoria_países())

#13
#Fiquei horas pensando nisso e só cheguei nessa conclusao
#parece ser bem ruim e nada pythonica, mas é o que funcionou.
def adicionar_dicionario(valor):
    if(valor[0][0].lower() in chaves):
        chave = valor[0]
        if(chave not in dicionario.keys()):
            dicionario[chave] = []
            dicionario[chave].append(valor)
        else:
            if(valor not in dicionario[chave]):
                dicionario[chave].append(valor)
dicionario = {}
chaves = list(set(map(lambda x: x[1].lower(),ct)))
list(map(adicionar_dicionario,ct))
# print(dicionario)

#14
def get_first_ten_countries():
    return ct[0:10]

#15
def get_last_ten_countries():
    return ct[-10:]

#Nivel 3
#1
import pprint
from countriesdata import data
#Classificar os paises por nome, capital e populacao
#muito tempo que perdi pra entender essa brincadeira mas foi!
filtro = list(map(lambda x: {k: v for k, v in x.items() if k == "name" or k=="capital" or k =="population"},data))

#2
filtro = list(map(lambda x: {k: v for k, v in x.items() if k == "currency"},data[0:10]))

#3
#Exercicio doido!, chato, demorei muito
from operator import itemgetter

filtro = list(map(lambda x: {k: v for k, v in x.items() if k =="population" or k =='name'},data))

sorted_list = sorted(filtro, key=itemgetter('population','name'),reverse=True)[0:10]
print(sorted_list)
