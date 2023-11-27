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
json_data = json.dumps(data)

# Print the JSON data
print(json_data)