from models.papel import Papel
from fastapi import FastAPI, APIRouter
import json

banco_dados_fake = []

papel1 = Papel(id=1, nome="PETR4", sigla="PETR4", cnpj="123456789")
papel2 = Papel(id=2, nome="VALE3", sigla="VALE3", cnpj="987654321")
papel3 = Papel(id=3, nome="ITUB4", sigla="ITUB4", cnpj="456789123")
papel4 = Papel(id=4, nome="BBDC4", sigla="BBDC4", cnpj="321654987")
papel5 = Papel(id=5, nome="ABEV3", sigla="ABEV3", cnpj="789123456")
banco_dados_fake.extend([papel1, papel2, papel3, papel4, papel5])

router =  APIRouter()

@router.post("/")
def adicionar_papel(papel: Papel):
    try:
        for existing_papel in banco_dados_fake:
            if existing_papel.id == papel.id or existing_papel.nome == papel.nome:
                raise Exception("Papel já existe na lista!")
        banco_dados_fake.append(papel)
        return f"Inserido com sucesso!"
    except Exception as e:
        return f"Erro ao inserir papel: {e}"

@router.get("/")
def listar_papel():
    return banco_dados_fake