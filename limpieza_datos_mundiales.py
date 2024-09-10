import pandas as pd

# Cargo los datos desde el archivo CSV
df_matches = pd.read_csv('fifa_worldcup_historical_data.csv')

# Elimino filas duplicadas y ordeno por año
df_matches.drop_duplicates(inplace=True)
df_matches.sort_values('Year', inplace=True)

# Identifico los índices de las filas que quiero eliminar
index_eliminar = df_matches[(df_matches['Home'].str.contains('Sweden')) & (df_matches['Away'].str.contains('Austria'))].index

# Elimino las filas identificadas
df_matches.drop(index_eliminar, inplace=True)

# Limpio los datos de la columna 'Score' eliminando caracteres no deseados
df_matches['Score'] = df_matches['Score'].str.replace(r'[^\d–-]', '', regex=True)

# Elimino espacios en blanco de las columnas 'Home' y 'Away'
df_matches['Home'] = df_matches['Home'].str.strip()
df_matches['Away'] = df_matches['Away'].str.strip()

# Separar la columna 'Score' en 'HomeGoals' y 'AwayGoals'
df_matches[['HomeGoals', 'AwayGoals']] = df_matches['Score'].str.split('–', expand=True)
df_matches.drop('Score', axis=1, inplace=True)

# Renombro las columnas para mayor claridad
df_matches.rename(columns={'Home': 'HomeTeam', 'Away': 'AwayTeam'}, inplace=True)

# Convierto 'HomeGoals' y 'AwayGoals' a enteros
df_matches = df_matches.astype({'HomeGoals': 'int', 'AwayGoals': 'int'})

# Calculo el total de goles
df_matches['TotalGoals'] = df_matches['HomeGoals'] + df_matches['AwayGoals']

# Guardo el DataFrame limpio en un nuevo archivo CSV
df_matches.to_csv('fifa_worldcup_historical_data_clean.csv', index=False)

# Obtengo la lista de equipos únicos
df = df_matches
team_list = teams_home = df['HomeTeam'].unique()

# Defino una función para obtener los goles por equipo
def get_goals_per_team(team):
    # Selecciono las filas donde el equipo es el equipo local o visitante
    df_team = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].copy()
    # Establezco los goles usando .loc para evitar advertencias
    df_team.loc[:, 'Goals'] = df_team.apply(lambda x: x['HomeGoals'] if x['HomeTeam'] == team else x['AwayGoals'], axis=1)
    # Establezco los goles recibidos usando .loc para evitar advertencias
    df_team.loc[:, 'RecivedGoals'] = df_team.apply(lambda x: x['HomeGoals'] if x['HomeTeam'] != team else x['AwayGoals'], axis=1)
    list_goals = [{'Team': team, 'Goals': df_team['Goals'].sum().item(), 'RecivedGoals': df_team['RecivedGoals'].sum().item()}]
    return list_goals

# Obtengo los datos de todos los equipos
all_teams = [get_goals_per_team(team) for team in team_list]
df_all_teams = pd.DataFrame([team for sublist in all_teams for team in sublist])

# Calculo la diferencia de goles
df_all_teams['GoalDifference'] = df_all_teams['Goals'] - df_all_teams['RecivedGoals']

# Guardo el DataFrame de equipos en un archivo CSV
df_all_teams.to_csv('fifa_worldcup_teams.csv', index=False)
