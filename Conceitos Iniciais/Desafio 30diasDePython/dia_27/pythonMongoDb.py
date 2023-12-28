# Python com MongoDB
# Python é uma tecnologia backend e pode ser conectada a diferentes aplicativos de banco de dados. 
# Ele pode ser conectado a bancos de dados SQL e noSQL. Nesta seção,
# conectamos Python ao banco de dados MongoDB, que é um banco de dados noSQL.


# MongoDB
# MongoDB é um banco de dados NoSQL. O MongoDB 
# armazena dados em um documento semelhante a JSON, o que torna o MongoDB muito flexível e escalável. 
# Vejamos as diferentes terminologias dos bancos de dados SQL e NoSQL. A tabela a seguir fará a diferença 
# entre bancos de dados SQL e NoSQL.

# SQL versus NoSQL ( olhar imagem .png)


# Nesta seção, focaremos em um banco de dados NoSQL MongoDB. 
# Vamos nos inscrever no mongoDB clicando no botão entrar e depois clicar em registrar na próxima página.


# let's import the flask
# from flask import Flask, render_template
# import pymongo
# import os # importing operating system module
# MONGODB_URI = 'mongodb+srv://admin:admin@30diaspython.a9qhzfg.mongodb.net/'
# client = pymongo.MongoClient(MONGODB_URI)
# print(client.list_database_names())

# app = Flask(__name__)
# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# Criando um banco de dados e uma coleção
# Vamos criar um banco de dados, banco de dados e coleção no mongoDB serão criados caso não exista. 
# Vamos criar um banco de dados com o 
# nome trinta_dias_de_python e uma coleção de alunos . Para criar um banco de dados

# db = client.name_of_databse # we can create a database like this or the second way
# db = client['name_of_database']


# let's import the flask
from flask import Flask, render_template
import pymongo
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
