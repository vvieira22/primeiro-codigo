# Interface de programação de aplicativos (API)
"""
No contexto do desenvolvimento web, uma API é definida como um conjunto de 
especificações, como mensagens de solicitação do Hypertext Transfer Protocol (HTTP), 
juntamente com uma definição da estrutura das mensagens de resposta, geralmente em XML 
ou(JSON).
"""

#Por exemplo utilizar api Rest do twitter para obter informacoes do site
#tendencias de pesquisas, etc..

#API RESTful é uma interface de programa de aplicativo (API) que usa solicitações 
# HTTP para dados GET, PUT, POST e DELETE

# get - obter dados de um recurso (ou coleção de recursos)
# post - criar um novo recurso
# put - atualizar um recurso
# delete - remover um recurso

#Iremos criar a aplicacao que execute operação CRUD (Criar, Ler, Atualizar, Excluir)  que possui uma API para criar dados, obter dados, 
# atualizar dados ou excluir dados de um banco de dados.


#HTTP (protocolo de transferência de hipertexto)
"""
HTTP é um protocolo de comunicação estabelecido entre um cliente e um 
servidor. Um cliente, neste caso, é um navegador e um servidor é o local
onde você acessa os dados. HTTP é um protocolo de rede usado para entregar 
recursos que podem ser arquivos na World Wide Web, sejam eles arquivos HTML,
arquivos de imagem, resultados de consultas, scripts ou outros tipos de arquivos.
"""

#Estrutura do HTTP

"""
HTTP usa o modelo cliente-servidor. Um cliente HTTP abre uma conexão e 
envia uma mensagem de solicitação para um servidor HTTP e o servidor HTTP 
retorna uma mensagem de resposta que representa os recursos solicitados. 
Quando o ciclo de resposta da solicitação é concluído, o servidor 
fecha a conexão.
"""


# Linha de solicitação inicial (linha de status)
# A linha de solicitação inicial é diferente da resposta.
# Uma linha de solicitação possui três partes, separadas por espaços:

# nome do método (GET, POST, HEAD)
# caminho do recurso solicitado,
# a versão do HTTP que está sendo usada. por exemplo, GET/HTTP/1.1


# Initial Response Line(Status Line)
# The initial response line, called the status line, also has three parts separated by spaces:

# HTTP version
# Response status code that gives the result of the request, 
# and a reason which describes the status code. Example of status lines are: 
#     HTTP/1.0 200 OK or HTTP/1.0 404 Not Found Notes:
# The most common status codes are: 200 OK: The request succeeded, 
# and the resulting resource (e.g. file or script output) is returned in the message body. 
# 500 Server Error A complete list of HTTP status code can be found https://http.cat/


#Header Fields (CAMPOS DO HEADERS)
# as linhas de cabeçalho fornecem informações sobre a solicitação ou resposta, 
# ou sobre o objeto enviado no corpo da mensagem.

#Header fields
"""
Os campos de cabeçalho fornecem informações adicionais sobre a solicitação ou resposta HTTP. 
Eles são compostos por um nome e um valor, separados por dois pontos (:). 
Existem vários campos de cabeçalho disponíveis, cada um com uma finalidade específica. 
Alguns exemplos comuns de campos de cabeçalho incluem:

- Content-Type: especifica o tipo de mídia do corpo da mensagem (por exemplo, text/html, application/json).
- Content-Length: especifica o tamanho do corpo da mensagem em bytes.
- Authorization: fornece credenciais de autenticação para acessar recursos protegidos.
- User-Agent: identifica o software do cliente que está fazendo a solicitação.
- Accept: especifica os tipos de mídia que o cliente aceita na resposta.
- Cookie: contém informações de estado do cliente que são enviadas de volta ao servidor.
"""

#Exemplo de uso de campos de cabeçalho em uma solicitação HTTP:

import requests

url = "https://api.example.com/users"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <access_token>"
}

response = requests.get(url, headers=headers)
"""

Neste exemplo, estamos fazendo uma solicitação GET para a URL "https://api.example.com/users" 
e incluindo dois campos de cabeçalho: "Content-Type" e "Authorization". 
O campo "Content-Type" especifica que o corpo da mensagem é um JSON, 
enquanto o campo "Authorization" contém um token de acesso para autenticação.

É importante fornecer os campos de cabeçalho corretos em uma solicitação HTTP, 
pois eles podem afetar o comportamento do servidor e a forma como a resposta é processada.
"""

#Exemplo de uso de campos de cabeçalho em uma resposta HTTP:

import json
import requests

response_data = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}

response_headers = {
    "Content-Type": "application/json",
    "Content-Length": str(len(json.dumps(response_data)))
}

response = {
    "status_code": 200,
    "headers": response_headers,
    "data": response_data
}

"""

Neste exemplo, estamos simulando uma resposta HTTP com um status de 200 (OK) 
e incluindo dois campos de cabeçalho: "Content-Type" e "Content-Length". 
O campo "Content-Type" especifica que o corpo da mensagem é um JSON, 
enquanto o campo "Content-Length" especifica o tamanho do corpo da mensagem em bytes.

Os campos de cabeçalho em uma resposta HTTP fornecem informações adicionais 
sobre a resposta, como o tipo de mídia do corpo da mensagem e o tamanho do corpo da mensagem. 
Essas informações podem ser úteis para o cliente ao processar a resposta recebida.
"""

#Body , O corpo da mensagem
# O corpo de uma requisição HTTP é uma parte 
# importante para enviar dados para um servidor. 
# Ele é usado principalmente em requisições POST,
# PUT e PATCH, onde você deseja enviar informações 
# para serem processadas pelo servidor.

# No código que você compartilhou, o corpo 
# da requisição é definido na variável data

url = "https://api.example.com/users"
headers = {
    "Content-Type": "application/json"
}
data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

