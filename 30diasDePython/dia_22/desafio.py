#1
import requests
from bs4 import BeautifulSoup
import json

# URL to fetch
url = "https://www.bu.edu/president/boston-university-facts-stats/"

# Fetch the content from url
response = requests.get(url)
content = response.content

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all li elements with class 'list-item'
list_items = soup.find_all('li', class_='list-item')

# Extract the text from eachs li element and store it in a dictionary
data = {item.find('p', class_='text').get_text(): item.find('span', class_='value').get_text() for item in list_items}

# Convert the dictionary to JSON
json_data = json.dumps(data, indent=4)

# Print the JSON data
# print(json_data)


#2
# URL to fetch
url = "https://archive.ics.uci.edu/datasets"

# Fetch the content from url
response = requests.get(url)
content = response.content

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
soup = soup.find('div', class_='flex flex-col gap-1')
soup = soup.find_all('div', class_='rounded-box bg-base-100')   

# Find all li elements with class 'link-hover link text-xl font-semibold'
# name = soup.find_all('a', class_='link-hover link text-xl font-semibold')
data = {item.find('a', class_='link-hover link text-xl font-semibold').get_text(): item.find('p', class_='truncate').get_text() for item in soup}
json_data = json.dumps(data, indent=3)
# print(json_data)

#3
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"	

# Fetch the content from url
response = requests.get(url)
content = response.content

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

td_elements = soup.find_all('td', {'data-sort-value': True})
nome_presidentes = [] #ordem cronologica.
for presidentes in td_elements:
    nome_presidentes.append(presidentes.find('a')['title'])
print(nome_presidentes)