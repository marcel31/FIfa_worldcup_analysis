import pandas as pd
from bs4 import BeautifulSoup
import requests

# Defino los años de los torneos de la Copa Mundial de la FIFA
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

# Defino la función para obtener los partidos de un año específico
def get_matches(year):
    
    # Creo una variable para la URL del año pasado por parametro
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    
    # Realizo una solicitud HTTP para obtener el contenido de la página
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    # Busco todos los divs que contienen los datos de los partidos
    matches = soup.find_all('div', class_='footballbox')

    # Inicializo listas para almacenar los datos de los partidos
    home = []
    score = []
    away = []

    # Recorro cada partido y extraigo los datos
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())
        
    # Creo un DataFrame con los datos extraídos
    dict_football = {'Home': home, 'Score': score, 'Away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['Year'] = year
    return df_football

# Obtengo los partidos para todos los años definidos
matches = [get_matches(year) for year in years]

# Combino los DataFrames de todos los años en uno solo
df_matches = pd.concat(matches, ignore_index=True)

# Guardo el DataFrame en un archivo CSV
df_matches.to_csv('fifa_worldcup_historical_data.csv', index=False)
