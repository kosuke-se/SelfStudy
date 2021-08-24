import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.google.com')
data = BeautifulSoup(site.text, 'html.parser')

print(data.title)
print(data.title.text)
print(data.find_all('a'))
print(data.find(id='id_name'))
print(data.find(text='Google'))