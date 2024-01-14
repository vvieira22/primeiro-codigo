def create_papel_valido():
    return {
        "id":0,
        "nome": "string",
        "sigla": "PETR4", #precisa ser valido la pelo teste que fizemos dentro da classe papel
        "cnpj": "string",
    }

def create_papel_invalido(campos_invalidos=['sigla']):
    papel_invalido = {
        "id":0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string",
    }
    
    if 'sigla' in campos_invalidos:
        papel_invalido['sigla'] = '22AAAAAAAAAAAAAAAA' 
    
    return papel_invalido