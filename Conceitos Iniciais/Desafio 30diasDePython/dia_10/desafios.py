#1
# for numero in range(11):
#     print(numero)

# numero = 0
# while numero < 11:
#     print(numero)
#     numero += 1

#2
# for numero in reversed(range(11)):
#     print(numero)
# for numero in range(10,-1,-1):
#     print(numero)
# numero = 10

# while numero < -1:
#     print(numero)
#     numero -= 1

#3
# for chamadas in range(8):
#     print("*"*chamadas)

#4
# for chamadas in range(8):
#     print("*"*8)

#5
# for numero in range(11):
#     print(f'{numero} x {numero} = {numero*numero}')

#6
# for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
#     print(item)

#7
# for item in range(101):
#     if item % 2 == 0:
#         print(item)

#8
# for item in range(101):
#     if item % 2 != 0:
#         print(item)

#Nivel 2
#1
# soma = 0
# for numero in range(101):
#     soma += numero
# print(soma)

# #2
# soma_par = 0
# soma_impar = 0
# for numero in range(101):
#     if(numero % 2 == 0):
#         soma_par += numero
#     else:
#         soma_impar += numero
# print(soma_par,soma_impar)


#Nivel 3
#1
import countries

# for cidades in countries.countries:
#     if "land" in cidades:
#         print(cidades)

#2
# lista = ['banana', 'orange', 'manga', 'lemon']
# for i in range(len(lista)-1, -1, -1):
#     print(lista[i])

#3
#-1
import countries_data

# lista_idiomas = []

# for paises in countries_data.ctdata:
#     for linguagem in paises["languages"]:
#         if linguagem not in lista_idiomas:
#             lista_idiomas.append(linguagem)
# print(len(lista_idiomas))

#-2
idiomas_mais_falados = {}

for paises in countries_data.ctdata:
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

#-3
populacao = {}

for pais in countries_data.ctdata:
    populacao[pais['name']] = pais['population']

populacao = sorted(populacao.items(), key=lambda x:x[1],reverse=True)
populacao = dict(populacao)
contador = 0
for chave in populacao:
    print(f'{chave}: {populacao[chave]} pessoas.')
    contador += 1
    if contador == 10:
        break