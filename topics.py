import json 
import requests 
from bs4 import BeautifulSoup

def obtener_datos(url): 
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.content, "html.parser") 
    nombres = bs.find_all("p", class_="f3 lh-condensed mb-0 mt-1 Link--primary") 
    descripcion = bs.find_all("p", class_="f5 color-fg-muted text-center mb-0 mt-1")
    #p class="f5 color-fg-muted text-center mb-0 mt-1"
    topics = [nombre.text.strip() for nombre in nombres] 
    resultado = [desc.text.strip() for desc in descripcion]
    return (resultado, topics)

resultado, topics = obtener_datos("https://github.com/topics/")
eleccion = int(input("1, 2"))
if eleccion == 1: 
    for topic in topics: print(topic)
if eleccion == 2:
    for desc in resultado: print(desc)
else: print("error")

