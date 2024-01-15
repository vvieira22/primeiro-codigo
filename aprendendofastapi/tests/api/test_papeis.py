from fastapi.testclient import TestClient
from tests.utils.papeis import create_papel_valido, create_papel_invalido
from models.papel import Papel
import asyncio
import pytest
import ormar

def test_cria_papel(client: TestClient) -> None:
    body = create_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]

def test_cria_papel_com_sigla_invalida(client: TestClient) -> None:
    body = create_papel_invalido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 422 #poderia ver no content a sigla se ta invalida pra validar o teste ou so ve se retornou 422
    
def test_obtem_papel_por_id(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
    response = client.get(f"/papeis/{papel.id}")
    content = response.json()
    assert response.status_code == 200
    assert content["sigla"] == papel.sigla

def test_obtem_papel_por_id_inexistente(client: TestClient) -> None:
    response = client.get(f"/papeis/0")
    content = response.json()
    assert response.status_code == 404
    assert content["mensagem"] == "Entidade nao encontrada."

#PATCH
def test_update_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    novo_nome = "Novo Nome"
    atributos_para_atualizar = {"nome": novo_nome}
    
    response = client.patch(f"/papeis/{papel.id}", json=atributos_para_atualizar)
    content = response.json()
    
    papel_atualizado = loop.run_until_complete(Papel.objects.get(id=papel.id))
    
    assert response.status_code == 200
    assert content["nome"] == novo_nome
    assert papel_atualizado.nome == novo_nome
    
def test_update_papel_inexistente(client: TestClient) -> None:
    novo_nome = "Novo Nome"
    atributos_para_atualizar = {"nome": novo_nome}
    
    #esse numero é ficticio que nao existe no banco justamente para forçar o erro.
    response = client.patch(f"/papeis/02020202020", json=atributos_para_atualizar)
    content = response.json()
    
    assert response.status_code == 404
    assert content["mensagem"] == "Entidade nao encontrada."
    
def test_delete_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
    response = client.delete(f"/papeis/{papel.id}")
    content = response.json()
    
    with pytest.raises(ormar.exceptions.NoMatch):
        loop.run_until_complete(Papel.objects.get(id=papel.id))
    
    assert response.status_code == 200
    
def test_delete_papel_existente(client: TestClient) -> None:
    response = client.delete(f"/papeis/02020202020")
    content = response.json()
    
    assert response.status_code == 404
    assert content["mensagem"] == "Entidade nao encontrada."