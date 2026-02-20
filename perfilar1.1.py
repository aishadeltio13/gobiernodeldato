# sweetviz

import pandas as pd
import sweetviz as sv

# Cargar el CSV
spotify = pd.read_csv("spotify-2023.csv", encoding="latin-1")

# Crear el reporte
reporte = sv.analyze(spotify)

# Generar el HTML
reporte.show_html("reporte_spotify.html")