import requests
from bs4 import BeautifulSoup


class CodigoModelo:
    def __init__(self, url) -> None:
        self.url = url
       
           
    def obtenerInfoCode(self, url):  
        gitStart='https://github.com/search?q='
        gitEnd='&type=code'        
        urlCompleta=gitStart+url+gitEnd
        #Se divide el link en 3 bloques, el texto buscado va en el bloque de medio
        respuesta = requests.get(urlCompleta)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            repositorio=[]
            file = []
            lang = []
            codigo = []
