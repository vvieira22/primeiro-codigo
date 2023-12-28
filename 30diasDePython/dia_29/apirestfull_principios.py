# Nesta seção, abordaremos uma API RESTful que usa métodos de solicitação HTTP para dados GET, PUT, POST e DELETE.

# Cada aplicação que possui operação CRUD (Criar, Ler, Atualizar, Excluir) 
# possui uma API para criar dados, obter dados, atualizar dados ou excluir dados do banco de dados.
# O navegador pode lidar apenas com solicitações get. Portanto, precisamos de uma ferramenta que nos 
# ajude a lidar com todos os métodos de solicitação (GET, POST, PUT, DELETE).
#O postman é um dos mais populares quando se trata de desenvolvimento de api.


#Estrutura de uma API
# Um ponto final da API é um URL que pode ajudar a recuperar, criar, atualizar ou excluir um recurso. 
# A estrutura é semelhante a esta: Exemplo: https://api.twitter.com/1.1/lists/members.json
# GET        Used for object retrieval
# POST       Used for object creation and object actions
# PUT        Used for object update
# DELETE     Used for object deletion


# AQUI VAMOS USAR DADOS MARRETADOS, PODEMOS FACILMENTE CONECTAR AO BANCO DE DADOS E BUSCAR ESSAS INFORMACOES
# MAS COMO O USO DO MONGODB TA COMPLICADO, OPTEI POR SETAR ESSES DADOS MANUALMENTE.

# let's import the flask
from flask import Flask,  Response
import os
import json

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')

#Aqui vai detornar um estudante especifico pelo nome
@app.route('/api/v1.0/students/<name>', methods=['GET'])
def get_student(name):
    student_list = [
        {
            'name': 'Asabeneh',
            'country': 'Finland',
            'city': 'Helsinki',
            'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
        },
        {
            'name': 'David',
            'country': 'UK',
            'city': 'London',
            'skills': ['Python', 'MongoDB']
        },
        {
            'name': 'John',
            'country': 'Sweden',
            'city': 'Stockholm',
            'skills': ['Java', 'C#']
        }
    ]
    
    for student in student_list:
        if student['name'] == name:
            return Response(json.dumps(student), mimetype='application/json')
    
    return Response(json.dumps({'error': 'Student not found'}), status=404, mimetype='application/json')

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)