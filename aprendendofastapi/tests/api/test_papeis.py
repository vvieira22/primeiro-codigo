from fastapi.testclient import TestClient
from tests.utils.papeis import create_papel_papel_valido

def test_cria_papel(client: TestClient) -> None:
    body = create_papel_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]