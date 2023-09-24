import requests
from bs4 import BeautifulSoup

class TendenciasModelo:
    #metodo constructor
    def __init__(self,url,) -> None:   
        self.url = url 
       
             
       
    def obtenerTendencias(self,url):   
        respuesta = requests.get(url) #realiza una solicitud HTTP GET a la url
        if respuesta.status_code == 200: # comprueba si la solicitud fue exitosa (código de estado 200=OK)
            # parsea el contenido HTML con BeautifulSoup(se analiza para identificar las etiquetas, atributos y contenido dentro del documento)
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            #lista vacia para guardar los resultados
            repositorios = []
            # buscar el atributo y la clase que contiene toda la información que queremos extraer 
            repositorio = soup.find_all('article', class_='Box-row')

            for articulo in repositorio:
                # nombre y desarrollador con etiqueta h2 clase: 'h3 lh-condensed' 
                repo = articulo.find('h2', class_='h3 lh-condensed')#find= buscar 
                #guardo en la variable lo q contiene repo, lo paso a texto y elimino espacios en blanco  con strip
                repo_nombre_completo = repo.text.strip()
                # guardo del repo solo el desarrollador con la etiqueta span
                desarrollador = repo.span.text.strip()
                # creo una variable donde elimino el nombre del desarrollador y queda solo el titulo
                titulo_repo = repo_nombre_completo.replace(desarrollador, '').strip()


                #descripción con p clase:'col-9 color-fg-muted my-1 pr-4'
                descripcion_repo = articulo.find('p', class_='col-9 color-fg-muted my-1 pr-4')
                descripcion = descripcion_repo.text.strip() if descripcion_repo else 'Sin descripción'

                #lenguaje de programación con span clase:'d-inline-block ml-0 mr-3'
                lenguaje_repo = articulo.find('span', class_='d-inline-block ml-0 mr-3')
                lenguaje = lenguaje_repo.text.strip() if lenguaje_repo else ''

                # estrellas con a clase:'Link Link--muted d-inline-block mr-3'
                estrellas_repo=articulo.find('a', class_='Link Link--muted d-inline-block mr-3')
                estrellas= estrellas_repo.text.strip() if estrellas_repo else ''
                
                # forks con a (filtro para encontrar el elemento <a> con la funcion lambda): href que termina con /forks 
                forks_repo=articulo.find('a', href=lambda href: href.endswith("/forks"))
                forks= forks_repo.text.strip() if forks_repo else ''
                #forks = articulo.find('a', href=lambda href: href and href.endswith("/forks"), class_='Link Link--muted d-inline-block mr-3')
                
                # encode= evitar errores al imprimir, codifica los caracteres en "utf-8"
                titulo_repo=titulo_repo.encode("utf-8", "ignore").decode("utf-8")
                desarrollador=desarrollador.encode("utf-8", "ignore").decode("utf-8")
                descripcion=descripcion.encode("utf-8", "ignore").decode("utf-8")
                lenguaje=lenguaje.encode("utf-8", "ignore").decode("utf-8")
                estrellas=estrellas.encode("utf-8", "ignore").decode("utf-8")
                forks=forks.encode("utf-8", "ignore").decode("utf-8")
                
                # método append para agregar los diccionarios en la lista repositorio. 
                # Cada elemento de la lista repositorios es un diccionario que contiene información sobre un repositorio
                repositorios.append({
                    'Repositorio': titulo_repo,
                    'Desarrollador': desarrollador,
                    'Descripción': descripcion,
                    'Lenguaje de Programación': lenguaje,
                    'Estrellas': estrellas,
                    'Clonados': forks
                })
            #devuelve la lista completa de diccionarios
            return repositorios
        else:
            print('Error al hacer la solicitud HTTP.')
            
    