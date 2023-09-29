import requests
import time
import urllib3
urllib3.disable_warnings()

def calcular_tempo(funcao):
    def wrapper():
        print("Pegando cotação")
        tempo_inicio = time.time()
        funcao()
        tempo_final = time.time()
        print(f"total de segundos para essa requisição: {tempo_final - tempo_inicio}")
    return wrapper

#Esse decorator me deu a funcionalidade de printar o tempo que levou para executar a minha funcao. pegar..()
@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link,verify=False)
    requisicao = requisicao.json()
    print(f"1 R$ = {requisicao['USDBRL']['bid']}$ dólar")

pegar_cotacao_dolar()
