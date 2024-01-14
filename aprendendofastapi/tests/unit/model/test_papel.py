from tests.utils.papeis import create_papel_invalido, create_papel_valido
from models.papel import Papel
import pytest

def test_cria_papel_valido() -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)  #atributos vai retornar um dicionario, usar o ** transforma cada elemento em um parametro
    
def test_cria_papel_com_sigla_invalida() -> None:
    with pytest.raises(ValueError):
        atributos = create_papel_invalido(['sigla'])
        papel = Papel(**atributos)  #atributos vai retornar um dicionario, usar o ** transforma cada elemento em um parametro
    