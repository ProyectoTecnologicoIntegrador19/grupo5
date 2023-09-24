
import requests
from bs4 import BeautifulSoup


url = 'https://github.com/event' 
response = requests.get(url) #permite trabajar con los requerimientos y las respuestas que se le solicitan a
                                #un servidor web a partir de la API (mec.q permiten a dos componentes soft.comunicarse entre sí mediante un conjunto de definiciones y protocolos
                                # o del HTTP de la plataforma web

if response.status_code == 200: #Después de recibir e interpretar un mensaje de solicitud, un servidor responde con 
                                #un mensaje de respuesta HTTP. El mensaje de respuesta tiene un código de estado
    soup = BeautifulSoup(response.text, 'html.parser') #transforma el ht,l en objetos 
    
    div= soup.find_all('div', class_='col-md-8 col-lg-12') #(nombre elemento,atributos o clases )
    titulo = div.find_all('h3').text.strip() #El método strip() eliminar los espacios en blanco
    fecha = div.find_all('p', class_='color-fg-muted f5').text.strip()
    descripcion= div.find_all('p class="mb-3"').text.strip()
   
    print (("Título:  ", titulo),("Fecha:   ", fecha), ("Descripción:  ", descripcion))
else:
    print('Error al hacer la solicitud HTTP.')

