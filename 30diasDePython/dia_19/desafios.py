#1
def retornarLinhasECaracteres(arquivo):
    numeroLinhas = len(arquivo.readlines())
    arquivo.seek(0) #assim que voce usa o read etc.., voce esta no final, precisa voltar no inicio do arquivo.
    quantidadeCaracteres = len(arquivo.read())
    return numeroLinhas,quantidadeCaracteres
# with open("./30diasDePython/dia_19/dados/obama.txt") as f:
#     print("Obama: Linhas:{} - Caracteres:{}".format(*retornarLinhasECaracteres(f)))
# with open("./30diasDePython/dia_19/dados/micheleObama.txt") as f:
#     print("Michele Obama: Linhas:{} - Caracteres:{}".format(*retornarLinhasECaracteres(f)))
# with open("./30diasDePython/dia_19/dados/trump.txt") as f:
#     print("Trump: Linhas:{} - Caracteres:{}".format(*retornarLinhasECaracteres(f)))
# with open("./30diasDePython/dia_19/dados/melinaTrump.txt") as f:
#     print("Melina Trump: Linhas:{} - Caracteres:{}".format(*retornarLinhasECaracteres(f)))


import json
#2 Pior forma possivel de fazer contagem, mas foi a que pensei no momento
#Jogar tudo numa lista só e depois contar.
def linguagens_mais_faladas(caminhoArquivo, quantidade):
    lista_linguagens = []
    with open(caminhoArquivo,encoding="utf8") as f:
        data = json.loads(f.read())
        data = data if quantidade == 0 else data[0:quantidade]
        for dicionado in data:
           lista_linguagens.extend(dicionado["languages"])
    return sorted(set([(lista_linguagens.count(i),i) for i in lista_linguagens]),reverse=True)

# print(linguagens_mais_faladas('./30diasDePython/dia_19/dados/countries_data.json',0))


#3
def cidades_mais_populosas(caminhoArquivo, quantidade):
    with open(caminhoArquivo,encoding="utf8") as f:
        data = json.loads(f.read())
        lista = list(map(lambda x: {'country':x["name"],'population':x["population"]},data))
        return sorted(lista[0:quantidade],key = lambda item: item['population'],reverse=True) if quantidade != 0 else sorted(lista,key = lambda item: item['population'],reverse=True)
print(cidades_mais_populosas('./30diasDePython/dia_19/dados/countries_data.json',0))


#Nivel 2
