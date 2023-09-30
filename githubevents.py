
import requests
from bs4 import BeautifulSoup


url = 'https://github.com/events' 
response = requests.get(url) #permite trabajar con los requerimientos y las respuestas que se le solicitan a
                                #un servidor web a partir de la API (mec.q permiten a dos componentes soft.comunicarse entre sí mediante un conjunto de definiciones y protocolos
                                # o del HTTP de la plataforma web

if response.status_code == 200: #Después de recibir e interpretar un mensaje de solicitud, un servidor responde con 
                                #un mensaje de respuesta HTTP. El mensaje de respuesta tiene un código de estado
    soup = BeautifulSoup(response.text, 'html.parser') #transforma el ht,l en objetos 
    repo= soup.find_all ("li", class_="py-3 py-lg-5 d-sm-flex")
    for noticia in repo: 
        t= noticia.find ("h3") 
        titulo= t.text.strip()
        print (titulo)
else:
    print('Error al hacer la solicitud HTTP.')

