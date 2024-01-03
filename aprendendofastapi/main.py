from fastapi import FastAPI

app = FastAPI()

#Get e post simples.
@app.get("/")
def root():
    return {"message": "Hello World"}
@app.post("/")
def root_post():
    return {"message": "Hello World"}

#Passando parâmetros na URL
#http://localhost:8000/root?parametro_obrigatorio=teste&parametro_opcional=123
@app.get("/root")
def root(parametro_obrigatorio: str, parametro_opcional: str = None):
    return {"parametro_obrigatorio": parametro_obrigatorio, "parametro_opcional": parametro_opcional}

#Como pegar conteudo do corpo da requisição, request body.
#importar pydantic
from pydantic import BaseModel

#Criar uma classe que herda de BaseModel
class Item(BaseModel):
    id: int
    descricao: str
    valor: float
    
@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]
""" 
        2 "objetos" distintos separados por virgula
        {
            "novo_item": {
                "id": 0,
                "descricao": "string",
                "valor": 0
            },
            "outro_item": {
                "id": 0,
                "descricao": "string",
                "valor": 0
            }
        }
"""


#HEADER - FASTAPI
"""
Os cabeçalhos HTTP são usados para passar informações adicionais entre o cliente e o servidor no pedido ou na resposta. 
Aqui estão alguns dos cabeçalhos HTTP mais comuns:
    Accept: Especifica os tipos de mídia que são aceitáveis para a resposta.

    Authorization: Contém as credenciais para autenticar um usuário-agente com um servidor.

    Cache-Control: Diretivas de controle de cache para a requisição ou resposta.

    Content-Type: Indica o tipo de mídia do recurso.

    Cookie: Armazena informações específicas do usuário.

    User-Agent: Contém uma string característica que permite o protocolo de rede do cliente identificar o tipo de aplicativo, 
    sistema operacional, fornecedor do software ou versão do software do agente do usuário do software solicitante.

    Host: Especifica o domínio do host e, opcionalmente, a porta número ao qual a requisição HTTP está sendo enviada.

    Referer: Contém o endereço da página da Web anterior da qual um link foi seguido.

    Content-Length: O tamanho, em bytes, do corpo da mensagem.

    Date: A data e hora em que a mensagem foi enviada.
"""
from fastapi import Header
from typing import Optional
from fastapi import Header

#: Optional[str] é opcional, eu poderia passar assim:
# user_agent = Header(None)
@app.get("/pegarHeader")
def get_header(user_agent : Optional[str] = Header(None)):
    return {"user_agent": user_agent}

#Pegar um header especifico/fora do padrao
#nome do header vai ser headerespecifico
@app.get("/pegarHeader2")
def get_header2(headerespecifico : Optional[str] = Header(default="valorpadrao")):
    #garantir que o headerespecifico vai ter um valor mesmo se enviar sem "nada"
    if not headerespecifico:
        headerespecifico = "valorpadrao"
    return {"headerespecifico": headerespecifico}


#COOKIES
"""
    Cookies são usados para armazenar informações específicas do usuário.
    Cookies são armazenados no lado do cliente.
    Cookies são enviados de volta para o servidor a cada solicitação.
    Cookies são usados para identificar usuários

    Cookies são pequenos arquivos de texto que são armazenados no navegador do usuário por sites que o usuário visita.
Eles são usados para manter o estado da sessão (como manter um usuário logado) e para rastrear as atividades do usuário no site.

    Podem ser configurados para curto ou longo prazo de tempo, recomendado curto periodo de tempo.
Os cookies são enviados de volta ao servidor a cada requisição HTTP subsequente ao mesmo domínio, permitindo que o servidor reconheça 
e lembre do usuário e de suas configurações. Isso é útil para manter os usuários logados,personalizar a experiência do usuário e 
rastrear o comportamento do usuário para análise.
"""

#Ele pode ter um chave e um valor

from fastapi import Response, Cookie

#setando um cookie
@app.get("/cookie")
def cookie(response : Response):
    response.set_cookie(key="meucookie", value="123456")
    return {"cookie": True}

@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"meucookie": meucookie}