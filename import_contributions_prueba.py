import requests
from bs4 import BeautifulSoup

# Obtener datos y que reciba una url
def obtener_datos(url):
    try:
        pagina = requests.get(url)
        pagina.raise_for_status()  # Agregar paréntesis aquí
        bs = BeautifulSoup(pagina.content, "html.parser")
        titulos = bs.find_all("span", class_="text-normal")  # Cambiar "sr-only" a "text-normal"
        return titulos  # Cambiar el nombre de la variable a "titulos"
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

# Imprimir información básica de las contributions
def imprimir_info(titulos):  # Cambiar el nombre de la variable a "titulos"
    if titulos is not None and len(titulos) > 0:
        titulos = sorted(titulos, key=lambda x: x.text)  # Ordenando alfabéticamente
        print(f"Información de contributions en la página:")
        for i, titulo in enumerate(titulos, start=1):
            print(f"{i}. Titulo: {titulo.text}")  # Cambiar "Contribution" a "Titulo"
        print(f"Total de contributions encontradas: {len(titulos)}")
    else:
        print('No se encontraron contributions o hubo un error al obtener los datos.')

# Ejecutar el código
contributions = obtener_datos("https://github.com/lkuffo")
imprimir_info(contributions)