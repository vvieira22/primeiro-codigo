"""
O que é Web Scrapping
A Internet está repleta de uma enorme quantidade de 
dados que podem ser usados ​​para diversos fins. Para coletar esses dados, 
precisamos saber como extrair dados de um site.

Web scraping é o processo de extrair e coletar dados de sites e armazená-los 
em uma máquina local ou em um banco de dados.

Nesta seção, usaremos o pacote beautifulsoup e requests para extrair dados.
 A versão do pacote que estamos usando é beautifulsoup 4.

Para começar a raspar sites, você precisa de solicitações , beautifoulSoup4 
e um site .

pip install requests
pip install beautifulsoup4

"""

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
# the content from the website
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website

#get all 'img' tag 
tables = soup.find_all('img')
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc

table = tables[0:2] # the result is a list, we are taking out data from it
print(table)

