import pandas as pd
import unicodedata
 
df = pd.read_csv('spotify-2023.csv', encoding='latin-1')
print(df.info())

