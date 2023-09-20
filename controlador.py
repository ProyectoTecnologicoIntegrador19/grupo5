import tendencias

def listarTendenciasMensuales():
        url='https://github.com/trending?since=monthly&spoken_language_code=es' #link de pagina a scrapear
        cantidad = int(input("\nIngrese número de repositorios a extraer: "))
        #variable(listaRepositorios) donde llamamos al archivo(tendencias) donde tenemos la clase que necesitamos(TendenciasModelo) y le mandamos la url
        listaRepositorios = tendencias.TendenciasModelo(url) 
        #variable(lista) donde llamamos la variable anterior(listaRepositorios) y llamamos al metodo (obtenerTendencias) con la url
        lista = listaRepositorios.obtenerTendencias(url)
        #recorremos los resultados que nos trajo con un for
        for t in lista:
                print(f'\nRepositorio: {t["Repositorio"]}')
                print(f'Desarrollador: {t["Desarrollador"]}')
                print(f'Descripción: {t["Descripción"]}')
                print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
                print(f'Estrellas: {t["Estrellas"]}' + ' ' * 50 + f'Clonados: {t["Clonados"]}\n')
                print('-' * 100)
           

def listarTendenciasSemanales():
        url='https://github.com/trending?since=weekly&spoken_language_code=es'
        listaRepositorios = tendencias.TendenciasModelo(url)
        lista = listaRepositorios.obtenerTendencias(url)
        for t in lista:
            print(f'\nRepositorio: {t["Repositorio"]}')
            print(f'Desarrollador: {t["Desarrollador"]}')
            print(f'Descripción: {t["Descripción"]}')
            print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
            print(f'Estrellas: {t["Estrellas"]}' + ' ' * 50 + f'Clonados: {t["Clonados"]}\n')
            print('-' * 100)
            
def listarTendenciasDiarias():
        url='https://github.com/trending?since=daily&spoken_language_code=es'
        listaRepositorios = tendencias.TendenciasModelo(url)
        lista = listaRepositorios.obtenerTendencias(url)
        for t in lista:
            print(f'\nRepositorio: {t["Repositorio"]}')
            print(f'Desarrollador: {t["Desarrollador"]}')
            print(f'Descripción: {t["Descripción"]}')
            print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
            print(f'Estrellas: {t["Estrellas"]}' + ' ' * 50 + f'Clonados: {t["Clonados"]}\n')
            print('-' * 100)
            
            
            
            
