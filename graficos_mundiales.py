import pandas as pd
import matplotlib.pyplot as plt

# Cargo datos desde archivos CSV
df_matches = pd.read_csv('fifa_worldcup_historical_data_clean.csv')
df_teams = pd.read_csv('fifa_worldcup_teams.csv')

# Ordeno los equipos por goles anotados y recibidos, y selecciono los primeros 50 equipos
df_teams = df_teams.sort_values(by='Goals', ascending=False).head(50)

# Preparo la figura y los ejes para los subgráficos
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# Gráfico 1: Goles anotados vs. Goles recibidos
axs[0, 0].bar(df_teams['Team'], df_teams['Goals'], label='Goles Anotados', color='green')
axs[0, 0].bar(df_teams['Team'], df_teams['RecivedGoals'], label='Goles Recibidos', color='red', bottom=df_teams['Goals'])
axs[0, 0].set_xticklabels(df_teams['Team'], rotation=90, fontsize=8)
axs[0, 0].set_ylabel('Número de Goles')
axs[0, 0].set_title('Goles Anotados y Recibidos por Equipo')
axs[0, 0].legend()

# Gráfico 2: Diferencia de goles por equipo (Top 25)
df_teams = df_teams.sort_values(by='GoalDifference', ascending=False)
df_top_teams = df_teams.head(25)
df_top_teams = df_top_teams.sort_values(by='GoalDifference', ascending=True)
axs[0, 1].barh(df_top_teams['Team'], df_top_teams['GoalDifference'], color='skyblue')
axs[0, 1].set_xlabel('Diferencia de Goles')
axs[0, 1].set_title(f'Diferencia de Goles por Equipo (Top {25})')
axs[0, 1].grid(axis='x', linestyle='--', alpha=0.7)

# Gráfico 3: Total de goles por año
goals_per_year = df_matches.groupby('Year')['TotalGoals'].sum()
year_with_max_goals = goals_per_year.idxmax()
max_goals = goals_per_year.max()
axs[1, 0].bar(goals_per_year.index, goals_per_year.values, color='skyblue')
axs[1, 0].set_xlabel('Año')
axs[1, 0].set_ylabel('Total de Goles')
axs[1, 0].set_title('Total de Goles por Año')
axs[1, 0].axhline(y=max_goals, color='r', linestyle='--', label=f'Año con Máximo de Goles: {year_with_max_goals}')
axs[1, 0].legend()

# Gráfico 4: Promedio de goles por partido por año
avg_goals_per_year = df_matches.groupby('Year')['TotalGoals'].mean()
axs[1, 1].plot(avg_goals_per_year.index, avg_goals_per_year.values, marker='o', color='green')
axs[1, 1].set_xlabel('Año')
axs[1, 1].set_ylabel('Promedio de Goles por Partido')
axs[1, 1].set_title('Promedio de Goles por Partido por Año')
axs[1, 1].grid(True)

# Ajusto el diseño para que no se solapen los elementos
plt.tight_layout()
plt.show()