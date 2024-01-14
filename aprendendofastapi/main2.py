from fastapi import FastAPI

from rotas import router
app = FastAPI()

@app.get("/")
def get_root():
    return {"mensagem": "api de papeis"}

app.include_router(router, prefix="")
# isso aqui era um teste para items de supermercado, ignorar papel e sim trocar por Item
# @app.get("/papel/valor_total")
# def pegar_valor_total():
    
#     # forma fraca burra, nao usar
#     total = 0
#     for papel in banco_dados_fake:
#         total += papel.valor * papel.quantidade
    
#     # modo pythonico
#     total = sum([papel.valor * papel.quantidade for papel in banco_dados_fake])
        
#     return {"valor_total": total}