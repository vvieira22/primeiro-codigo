from fastapi.testclient import TestClient

#ja vai pegar o cliente do conftest
def test_get_root(client: TestClient) -> None:
    resposta = client.get("/")
    body = resposta.json()
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "api de papeis"}
    