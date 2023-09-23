
import requests
from bs4 import BeautifulSoup


url = 'https://github.com/event' 
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    primerParrafo = soup.find_all('p', align='center', dir='auto')[1]
    contenido = primerParrafo.get_text().strip()

    print(contenido)
else:
    print('Error al hacer la solicitud HTTP.')

