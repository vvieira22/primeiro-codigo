from models.papel import Papel
from fastapi import FastAPI, APIRouter
import json

router =  APIRouter()

@router.post("/")
async def adicionar_papel(papel: Papel):
    await papel.save() 
    return papel

@router.get("/")
async def listar_papel():
    return await Papel.objects.all()