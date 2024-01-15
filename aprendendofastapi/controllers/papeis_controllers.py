from models.papel import Papel
from fastapi import FastAPI, APIRouter, Response
import json
import ormar 
from models.requests.papel_update import PapelUpdate

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
    
@router.patch("/{papel_id}")
async def patch_papel(propriedades_atualizacao: PapelUpdate, papel_id: int, response: Response):
    try:
        papel_salvo = await Papel.objects.get(id=papel_id)
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await papel_salvo.update(**propriedades_atualizadas)
        return papel_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade nao encontrada."}
    
@router.delete("/{papel_id}")
async def delete_papel(papel_id: int, response: Response):
    try:
        papel_salvo = await Papel.objects.get(id=papel_id)
        return await papel_salvo.delete()
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade nao encontrada."}