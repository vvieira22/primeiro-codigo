#1
import requests
url = "https://www.gutenberg.org/files/1112/1112.txt"

def ler_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Erro ao ler texto"

def palavras_mais_comuns(texto):
    texto = texto.lower()
    for caracter in ",.;:-?!()[]'/":
        texto = texto.replace(caracter, ' ')
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    palavras_ordenadas = sorted(contagem, key=contagem.get, reverse=True)
    return palavras_ordenadas[:10]
# print(palavras_mais_comuns(ler_texto(url)))

#2
#Assumindo que metric está em kgs!
import json
url = "https://api.thecatapi.com/v1/breeds"

def ler_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        return  response.json()
    else:
        return "Erro ao ler texto"

thecatapi = ler_texto(url)

#i
import re
#GATO MAIS LEVE
#nao sei como ele consegui achar o menor pq o valor é "2 - 4" nao um numero inteiro direto.
gato_mais_leve = min(thecatapi, key=lambda x: sum(int(elemento) for elemento in re.findall(r'\d+', x['weight']['metric'])))
# print(gato_mais_leve)

#GATO MAIS PESADO
gato_mais_pesado = max(thecatapi, key=lambda x: sum(int(elemento) for elemento in re.findall(r'\d+', x['weight']['metric'])))
# print(gato_mais_pesado)

#MEDIA PESO
# Cria uma lista de valores numéricos a partir de cada valor de intervalo
valores = [[float(valor) for valor in elemento['weight']['metric'].split('-')] for elemento in thecatapi]
# Calcula a média de cada valor
medias = [sum(valor) / 2 for valor in valores]
# Calcula a média geral
media_geral = sum(medias) / len(medias)
# print(media_geral)

#MEDIANA
import statistics
# print(statistics.median(medias))

#Desvio padrao
import numpy as np
# print(np.std(valores))


#2
#LISTA DOS PAISES
paises = [elemento['origin'] for elemento in thecatapi]
frequencia = {}
for elemento in thecatapi:
    valor = elemento['origin']
    frequencia[valor] = frequencia.get(valor, 0) + 1

ordenado = sorted(frequencia.items(),key = lambda x: x[1],reverse=True)
ordenado_dict = {k: v for k, v in ordenado}
print(ordenado_dict)
