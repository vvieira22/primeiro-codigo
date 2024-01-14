from models.papel import Papel
from fastapi import FastAPI, APIRouter, Response
import json
import ormar 

router =  APIRouter()

@router.post("/")
async def adicionar_papel(papel: Papel):
    await papel.save() 
    return papel

@router.get("/")
async def listar_papel():
    return await Papel.objects.all()

@router.get("/{id}")
async def pegar_papel(id: int, response: Response):
    try:
        return await Papel.objects.get(id=id)
    except ormar.exceptions.NoMatch:   #nao e bom botar qualquer execao pois pode dar 500, ou outro erro, importante mapear.
        response.status_code = 404
        return {"mensagem": "Entidade nao encontrada."}