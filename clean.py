import pandas as pd
import unicodedata
 
spotify = pd.read_csv('spotify-2023.csv', encoding='latin-1')
print(spotify.info())

# ¿ CUÁNTAS CANCIONES DIFERENTES HAY ?
cantidad = spotify["track_name"].nunique()
print(cantidad)

# ¿ CUÁL ES EL ARTISTA QUE MÁS CANCIONES EN SOLITARIO TIENE ?

