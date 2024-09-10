# Análisis de Datos de la Copa Mundial de la FIFA

Este repositorio contiene scripts en Python para extraer, limpiar y analizar datos históricos de los torneos de la Copa Mundial de la FIFA. Los datos se obtienen de Wikipedia, se procesan para eliminar inconsistencias y se visualizan a través de gráficos para proporcionar información útil sobre el rendimiento de los equipos y las estadísticas de los torneos.

## Archivos

### `Extraccion_datos_mundiales.py`:
- **Propósito**: Extrae datos de partidos de la Copa Mundial de la FIFA desde Wikipedia para cada torneo desde 1930 hasta 2022.
- **Cómo funciona**:
  - Define los años de los torneos.
  - Utiliza `requests` y `BeautifulSoup` para extraer los partidos de cada año.
  - Guarda los datos en un archivo CSV llamado `fifa_worldcup_historical_data.csv`.

### `limpieza_datos_mundiales.py`:
- **Propósito**: Limpia y transforma los datos extraídos para un análisis más detallado.
- **Cómo funciona**:
  - Carga los datos del archivo CSV generado por `Extraccion_datos_mundiales.py`.
  - Elimina duplicados, filas innecesarias y limpia las columnas.
  - Separa la columna de resultados en goles anotados y recibidos.
  - Calcula el total de goles y guarda los datos limpios en `fifa_worldcup_historical_data_clean.csv`.
  - Calcula estadísticas de goles por equipo y guarda los resultados en `fifa_worldcup_teams.csv`.

### `graficos_mundiales.py`:
- **Propósito**: Genera gráficos para visualizar los datos procesados.
- **Cómo funciona**:
  - Carga los datos limpios y los de los equipos.
  - Genera gráficos sobre goles anotados y recibidos, diferencia de goles, total de goles por año y promedio de goles por partido por año.
  - Los gráficos se muestran en una ventana utilizando `matplotlib`.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar los scripts:

- `pandas`
- `beautifulsoup4`
- `requests`
- `lxml`
- `matplotlib`

Puedes instalarlas usando pip:

```bash
pip install pandas beautifulsoup4 requests lxml matplotlib
