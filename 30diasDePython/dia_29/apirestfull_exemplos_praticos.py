from pickle import PUT
from flask import Flask, request, jsonify
import os

#PATCH VS PUT
"""
PUT e PATCH são dois métodos HTTP usados para atualizar recursos em um servidor.

A principal diferença entre eles é como eles lidam com a atualização do recurso:

- PUT: Este método substitui todo o recurso atual com os novos dados enviados na requisição. 
Se alguns atributos não forem incluídos na nova versão, eles serão removidos. Em outras palavras, um PUT é uma atualização completa do 
recurso.
- PATCH: Este método atualiza apenas os atributos que foram incluídos na requisição. Todos os outros atributos permanecem inalterados. 
Portanto, um PATCH é uma atualização parcial do recurso.
Por exemplo, se você tem um recurso com os atributos `nome`, `email` e `telefone`, e você envia uma requisição PUT com apenas 
`nome` e `email`, o atributo `telefone` será removido. Mas se você enviar uma requisição PATCH com apenas `nome` e `email`, 
o atributo `telefone` permanecerá inalterado.
"""

# PASSAR OBJETO OU IDENTIFICADOR NA URL
"""
A escolha entre passar o objeto que você precisa alterar ou excluir via JSON pelo corpo da requisição 
ou incorporar algum identificador na URL depende do método HTTP que você está usando e das práticas recomendadas 
para APIs RESTful.

Para métodos HTTP como PUT, PATCH e DELETE, é comum passar o identificador do recurso que você deseja 
alterar ou excluir na URL. Por exemplo, você pode ter uma URL como /api/recursos/{id} onde {id} é o identificador 
do recurso. O corpo da requisição então contém os dados que você deseja atualizar.

Para o método POST, que é geralmente usado para criar novos recursos, 
é comum passar os dados do novo recurso no corpo da requisição, e não na URL.
"""

app = Flask(__name__)

# Dicionário pré-existente
data_dict = {'chave1': 'valor1', 'chave2': 'valor2'}

@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    data = request.get_json()  # Obtém os dados enviados na requisição POST

    # Adiciona o elemento ao dicionário pré-existente
    for chave,valor in data.items():
        data_dict[chave] = valor
    # data_dict[data['chave']] = data['valor']

    # Retorna uma resposta em formato JSON
    return jsonify({'mensagem': 'Elemento adicionado com sucesso'})

@app.route('/api/exemplo', methods=['PATCH'])
def exemplo_patch():
    data = request.get_json()
    
    chave, valor = list(data.items())[0]
    if chave not in data_dict:
        return jsonify({'mensagem': 'Elemento não encontrado'})
    
    data_dict[chave] = valor
    
    # Retorna uma resposta em formato JSON
    return jsonify({'mensagem': 'Elemento ATUALIZADO com sucesso'})

@app.route('/api/exemplo', methods=['DELETE'])
def exemplo_delete():
    data = request.get_json()
    
    chave, valor = list(data.items())[0]
    if chave not in data_dict:
        return jsonify({'mensagem': 'Elemento não encontrado'})
    
    del data_dict[chave]
    
    # Retorna uma resposta em formato JSON
    return jsonify({'mensagem': 'Elemento DELETADO com sucesso'})



#Retornar a lista de elementos do dicionário
@app.route('/api/exemplo', methods=['GET'])
def exemplo_get():
    return jsonify(data_dict)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
