import requests
from bs4 import BeautifulSoup

class insightsmodelo: 
    def __init__(self) -> None:
        pass
    def get_insights_data(username):
        # Obtener la URL de la página de Insights
        url = "https://github.com/{username}/insights"

        # Hacer una solicitud HTTP a la URL
        response = requests.get(url)

        # Parsear la respuesta HTTP
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraer la información deseada
        stars = soup.find("span", class_="Counter").text
        forks = soup.find("span", class_="Counter").text
        watchers = soup.find("span", class_="Counter").text

        # Obtener la información sobre los Contributors
        contributors_table = soup.find("table", class_="table table-hover").find("tbody")
        contributors = []
        for tr in contributors_table.find_all("tr"):
            contributor = {
                "name": tr.find("td", class_="col-6").text,
                "contributions": tr.find("td", class_="col-6").find("span").text,
            }
            contributors.append(contributor)

        return {
            "stars": stars,
            "forks": forks,
            "watchers": watchers,
            "contributors": contributors,
        }

