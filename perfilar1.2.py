import pandas as pd
 
spotify = pd.read_csv('spotify-2023.csv', encoding='latin-1')
print(spotify.info())

# ¿ CUÁNTAS CANCIONES DIFERENTES HAY ?
cantidad = spotify["track_name"].nunique()
print(cantidad)

# ¿ CUÁL ES EL ARTISTA QUE MÁS CANCIONES EN SOLITARIO TIENE ?
grupos1 = spotify[spotify['artist_count'] == 1]
resultado = grupos1.groupby('artist(s)_name').size()
resultado = resultado.sort_values(ascending=False).head(3).reset_index()
print(resultado)

# ¿ CUAL ES EL DIA DEL MES EN EL QUE MÁS CANCIONES SE PUBLICAN ?