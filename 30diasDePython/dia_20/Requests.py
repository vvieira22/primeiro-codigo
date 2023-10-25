'''
Lendo do URL
Agora você já sabe como ler ou escrever em um arquivo localizado em sua máquina local. Às vezes, gostaríamos de ler um site usando url ou uma API. 
API significa Interface de Programa de Aplicativo. É um meio de trocar dados estruturados entre servidores principalmente como dados JSON. 
Para abrir uma conexão de rede, precisamos de um pacote chamado requests - ele permite abrir uma conexão de rede e implementar operações 
CRUD (criar, ler, atualizar e excluir). 
'''

# import requests

'''
Veremos os métodos get , status_code , headers , text e json no módulo requests :
    get() : para abrir uma rede e buscar dados da url - ele retorna um objeto de resposta
    status_code : Depois de buscarmos os dados, podemos verificar o status da operação (sucesso, erro, etc)
    headers : Para verificar os tipos de cabeçalho
    text : para extrair o texto do objeto de resposta buscado
    json : para extrair dados json Vamos ler um arquivo txt deste site, https://www.w3.org/TR/PNG/iso_8859-1.txt .
'''

import requests # importing the request module

# url = 'https://github.com/itsfoss/text-files/blob/master/sample_log_file.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page


import requests
import json
url = 'https://restcountries.com/v2/all'  # countries api
response = requests.get(url,verify=False)  # opening a network and fetching a data
# print(response) # response object
print(response.status_code)  # status code, success:200
print(response.headers)  # headers information
countries = response.json()
json_str  = json.dumps(countries[:1][0],indent=4)
print(json_str)  # we sliced only the first country, remove the slicing to see all countries|