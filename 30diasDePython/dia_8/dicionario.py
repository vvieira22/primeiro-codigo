#Dicionario é uma coleção sem ordem, modificável
# e alinhada como (chave : valor).


#Criando um dicionário
dici = {}
dicionario = {'key1':'value1','key2':2,"key3":1.9}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':25,
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}


#Comprimento dicionário, numero de pares chave:valor.
print(len(person))


#Acessando itens em um dicionário, consultando seu nome de chave:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])
"""
Acessar um item pelo nome da chave gera um erro se a chave não existir. 
Para evitar este erro primeiro temos que verificar se existe uma chave ou 
podemos usar o método get . O método get retorna None, que é um tipo de 
dados de objeto NoneType, se a chave não existir.
"""
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('city'))       # None


#Adicionando um novo registro no dicionário
dct['key99'] = 'value99'
#Modificando itens no dicionário funciona da mesma forma
#a chave ja deve existir


#Verificando chaves em um dicionário
print('key99' in dct) #true


# Removendo pares de chave e valor de um dicionário
# pop(key) : remove o item com o nome de chave especificado:
# popitem() : remove o último item
# del : remove um item com nome de chave especificado
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

#Dicionário para Lista
# O método items() altera o dicionário para uma lista de tuplas.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Limpar dicionario
#metodo .clear()
# dct.clear()

#Excluindo totalmente
# del dct   

"""Copie um dicionário
Podemos copiar um dicionário usando um método copy() . 
Usando copy podemos evitar a mutação do dicionário original.
"""
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


# Obtendo chaves do dicionário como uma lista
# O método keys() nos fornece todas as chaves 
# de um dicionário como uma lista.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


# Obtendo valores de dicionário como uma lista
# O método de valores nos dá todos os valores de 
# um dicionário como uma lista.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])