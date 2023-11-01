import requests
from bs4 import BeautifulSoup

# Obtener datos y que reciba una URL
def obtener_datos(usuario):
    try:
        url = f"https://github.com/{usuario}"
        pagina = requests.get(url)
        pagina.raise_for_status()
        bs = BeautifulSoup(pagina.content, "html.parser")
        titulo = bs.find_all("span", class_="sr-only")
        return titulo
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

# Mostrando info de contributions
def imprimir_info(contributions):
    if contributions is not None and len(contributions) > 0:
        # Ordenando alfabéticamente
        contributions = sorted(contributions, key=lambda x: x.text)
        print(f"Información de contributions en la página:")
        for i, contribution in enumerate(contributions, start=1):
            print(f"{i}. Contribution: {contribution.text}")
        print(f"Total de contributions encontradas: {len(contributions)}")
    else:
        print("No se encontraron contributions en la página.")

# Ejecutar el código para un usuario específico
usuario = "usuario"  # Se puede cambiar al nombre de usuario deseado
contributions = obtener_datos(usuario)
if contributions:
    imprimir_info(contributions)