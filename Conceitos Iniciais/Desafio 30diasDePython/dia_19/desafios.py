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

print(linguagens_mais_faladas('./30diasDePython/dia_19/dados/countries_data.json',0))


#3
def cidades_mais_populosas(caminhoArquivo, quantidade):
    with open(caminhoArquivo,encoding="utf8") as f:
        data = json.loads(f.read())
        lista = list(map(lambda x: {'country':x["name"],'population':x["population"]},data))
        return sorted(lista[0:quantidade],key = lambda item: item['population'],reverse=True) if quantidade != 0 else sorted(lista,key = lambda item: item['population'],reverse=True)
# print(cidades_mais_populosas('./30diasDePython/dia_19/dados/countries_data.json',0))


#Nivel 2
#4
with open("./30diasDePython/dia_19/dados/email_exchanges.txt") as f:
    arquivo = f.read()
    import re
    pattern = r'[\w.]+@[\w]+\.[\w.]+' #(qualquer letra ou .) + @ + qualquer coisa + . + qualquer coisa
    lista = list(set(re.findall(pattern,arquivo)))
    # print(lista)

#5
def palavra_mais_comum(caminho,quantidade):
    with open(caminho) as f:
        arquivo = f.read()
        lista_palavras = []
        pattern = r'\w+'
        lista = re.findall(pattern,arquivo)
        lista = sorted(set([(lista.count(i),i) for i in set(lista)]),reverse=True)
        return (lista[0:quantidade] if quantidade !=0 else lista)
# print(palavra_mais_comum("./30diasDePython/dia_19/dados/email_exchanges.txt",4))

#6
# print("Obama: ")
# print(palavra_mais_comum("./30diasDePython/dia_19/dados/obama.txt",10))
# print("Michele: ")
# print(palavra_mais_comum("./30diasDePython/dia_19/dados/micheleObama.txt",10))

# print("Trump: ")
# print(palavra_mais_comum("./30diasDePython/dia_19/dados/trump.txt",10))
# print("Melina: ")
# print(palavra_mais_comum("./30diasDePython/dia_19/dados/melinaTrump.txt",10))


#7
stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def removerPalavrasSuporte(texto):
    return ' '.join(palavra for palavra in texto.split() if palavra.lower() not in stop_words)

def removerPontuacao(texto):
    lista_palavras = []
    pattern = r'\w+'
    lista = re.findall(pattern,texto)
    return " ".join(lista)

from difflib import SequenceMatcher
def verificarSimilaridade(caminhoTexto1,caminhoTexto2):
    with open(caminhoTexto1) as f:
        texto1 = f.read()
    with open(caminhoTexto2) as f:
        texto2 = f.read()
    texto1 = removerPalavrasSuporte(texto1)
    texto2 = removerPalavrasSuporte(texto2)
    texto1 = removerPontuacao(texto1)
    texto2 = removerPontuacao(texto2)
    porcentagem =  SequenceMatcher(None,texto1,texto2).ratio()
    return str('%.1f'%(porcentagem * 100)) + "%" + " de similaridade entre os textos"
# print(verificarSimilaridade("./30diasDePython/dia_19/dados/obama.txt","./30diasDePython/dia_19/dados/trump.txt"))


#8
def mostcommonwordintext(texto):
    pattern = r'1595(.|\n)*?THE.END'
    stringLimpa = re.search(pattern,texto).group(0)
    stringLimpa = stringLimpa.replace("\n"," ")
    stringLimpa = stringLimpa.split()
    return sorted(set([(stringLimpa.count(i),i) for i in stringLimpa]),reverse=True)[0:10]

# with open("./30diasDePython/dia_19/dados/romeo_juliet.txt",'r') as f:
#     texto = f.read()
#     print(mostcommonwordintext(texto))


#9
#a
import csv
contador_py = 0
with open('./30diasDePython/dia_19/dados/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    contador_py = sum(1 for linha in csv_reader for elemento in linha if "python" in elemento.lower())
# print(contador_py)

#b
import csv
contador_js = 0
with open('./30diasDePython/dia_19/dados/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    contador_js = sum(1 for linha in csv_reader for elemento in linha if "javascript" in elemento.lower())
# print(contador_js)

#c
pattern = r'\bjava\b'
contador_java = 0
with open('./30diasDePython/dia_19/dados/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    #re.IGNORECASE lower ou upper case
    contador_java = sum(1 for linha in csv_reader for elemento in linha if re.search(pattern, elemento, re.IGNORECASE))
# print(contador_java)