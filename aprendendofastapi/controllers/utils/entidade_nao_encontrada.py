import ormar
from fastapi import HTTPException
from functools import wraps
#esse decorator wraps vai pegar as propriedade da funcao que eu estou recebendo como parametro
# e atribuir para essa funcao interna que eu to criando. Isso faz com que o fastapi consiga pegar as informacoes da funcao interna e registrar ela como endpoint

def entidade_nao_encontrada(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=404, detail="Entidade nao encontrada.") #fastapi ja tem um tratamento para 404. ele precisa das inf da funcao apra registrar ela. quando passamos assim ela n tem a funcao interna do endpoint para realizar a validacao
    return inner