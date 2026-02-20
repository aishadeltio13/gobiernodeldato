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
top_mes = spotify['released_month'].value_counts().head(1)
print(top_mes)

# ¿ CUAL ES EL AÑO DE LA SEGUNDA CANCION MAS ANTIGUA ?
resultado = spotify['released_year'].sort_values(ascending=True).head(2)
print(resultado)

# ¿ CUAL ES LA MEDIANA DEL BMP ?
mediana_total = spotify['bpm'].median()
print(mediana_total)

# ¿ CUAL ES EL VALOR MAS FRECUENTE DE danceability_% Y SU % ?
valor = spotify['danceability_%'].value_counts().head(1)
print(valor)
porcentaje = (valor / len(spotify)) * 100
print(porcentaje)

# ¿ EN QUE POSICIÓN ESTÁ ED SHERAN EN RELACION A NÚMERO DE CANCIONES ?
ranking = spotify['artist(s)_name'].value_counts()
posicion = ranking.index.get_loc('Ed Sheeran') + 1
print(posicion)

# ¿ EN QUE AÑO HUBO 18 CANCIONES ?
canciones_por_año = spotify['released_year'].value_counts()
años_con_18 = canciones_por_año[canciones_por_año == 18]
print(años_con_18)

# ¿ CUANTAS CANCIONES HAY EN APPLE PLAYLIST ?
total = spotify['in_apple_playlists'].sum()
print(total)