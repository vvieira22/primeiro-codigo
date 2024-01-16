from models.papel import Papel
from fastapi import APIRouter
from models.requests.papel_update import PapelUpdate
from fastapi import APIRouter
from models.papel import Papel
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.delete_controller import delete_controller

router = APIRouter()

@router.post("/")
async def adicionar_papel(papel: Papel):
    await papel.save() 
    return papel

@router.get("/")
async def listar_papel():
    return await Papel.objects.all()

@router.get("/{id}")
@entidade_nao_encontrada
async def pegar_papel(id: int):
    return await Papel.objects.get(id=id)
    
@router.patch("/{papel_id}")
@entidade_nao_encontrada
async def patch_papel(propriedades_atualizacao: PapelUpdate, papel_id: int):    
    papel_salvo = await Papel.objects.get(id=papel_id)
    propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
    await papel_salvo.update(**propriedades_atualizadas)
    return papel_salvo
    
#Generalizando o delete, só fiz o delete a titulo de curiosidade.
@router.delete("/{id}")
@delete_controller(Papel)
@entidade_nao_encontrada
async def delete_papel(id: int):
   pass 