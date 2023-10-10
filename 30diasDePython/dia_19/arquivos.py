#Manipulação de arquivos
#Como trabalhar com diferentes formatos de arquivo (.txt, .json, .xml, .csv, .tsv, .excel) 
#Primeiro vamos familiarizar com formato .txt

#Para começar vamos ler um arquivo.
#Temos a funcao integrada para ler chamada open()
'''
open('filename', mode) 
mode (r,a, w, x, t,b) could be to read, write, update..

    "r" - Leitura - Valor padrão. Abre um arquivo para leitura, retorna um erro se o arquivo não existir
    "a" - Anexar - Abre um arquivo para anexar, cria o arquivo se ele não existir
    "w" - Write - Abre um arquivo para escrita, cria o arquivo se ele não existir
    "x" - Create - Cria o arquivo especificado, retorna um erro se o arquivo existir
    "t" - Texto - Valor padrão. Modo texto
    "b" - Binário - Modo binário (por exemplo, imagens)
'''


#Abrindo arquivos no modo leitura
#por padrao sem colocar mode, ele já abre no modo leitura.
f = open("./30diasDePython/dia_19/exemplos.txt")
txt = f.read() 
    #readline() so le a primeira linha.
    #readlines() le todo o texto por linha e retorna uma lista de linhas.
    #splitlines() vai ler cada linha como lista, sem \n
print(txt)
f.close()

#Sempre que abrirmos um arquivo devemos fechar, para nao esquecer de fechamos
#existe uma nova maneira de abrir utilizando with - fecha os arquivos sozinhos.
#Vamos reescrever o conteudo anterior utilizando with:

with open('./30diasDePython/dia_19/exemplos.txt') as f:
    lines = f.read().splitlines()
    print(lines)


#Abrindo arquivos para gravar e atualizar.
# devemos atribuir como parametro na funcao open a ou w:

# "a" - anexar - será anexado ao final do arquivo; 
# se o arquivo não for criado, um novo arquivo será criado.

# "w" - write - irá sobrescrever qualquer conteúdo existente, 
# se o arquivo não existir ele cria.

#exemplo, escrever essa msg na ultima linha do arquivo
with open('./30diasDePython/dia_19/exemplos.txt','a') as f:
    f.write("linha adicionada no final do arquivo")


#Arquivos .json
# Json significa notação para objeto JavaScript, em python significa
# que trabalharemos com  um dicionário.

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

#ALTERNANDO ENTRE JSON E DICT
import json
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['skills'])

#ALTERNANDO ENTRE DICT PARA JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

#SALVANDO COMO ARQUIVO JSON
# Também podemos salvar nossos dados como um arquivo json. 
# Vamos salvá-lo como um arquivo json usando as etapas a seguir. 
# Para escrever um arquivo json, usamos o método json.dump(), 
# que pode levar dicionário, arquivo de saída, garantir_ascii e recuo.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./30diasDePython/dia_19/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
#No código acima, usamos codificação e recuo. O recuo torna o arquivo json fácil de ler.


#Arquivo com extensão .csv
# CSV significa valores separados por vírgula. CSV é um formato de arquivo 
# simples usado para armazenar dados tabulares, como planilhas ou bancos de 
# dados. CSV é um formato de dados muito comum na ciência de dados.

# "name","country","city","skills"
# "Asabeneh","Finland","Helsinki","JavaScript"

#exp:
import csv
with open('./30diasDePython/dia_19/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')


#ARQUIVO .XLSX
# Para ler arquivos Excel, precisamos instalar o pacote xlrd . 
# utilizando o pip.
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


#ARQUIVO .XML
# XML é outro formato de dados estruturados que se parece com HTML. 
# Em XML as tags não são predefinidas. A primeira linha é uma declaração XML.
# A tag person é a raiz do XML. A pessoa tem um atributo de gênero. 
# Exemplo: XML:

# <?xml version="1.0"?>
# <person gender="female">
#   <name>Asabeneh</name>
#   <country>Finland</country>
#   <city>Helsinki</city>
#   <skills>
#     <skill>JavaScrip</skill>
#     <skill>React</skill>
#     <skill>Python</skill>
#   </skills>
# </person>
#Para saber como melhor utilizar xml, consultar doc: https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
tree = ET.parse('./30diasDePython/dia_19/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)