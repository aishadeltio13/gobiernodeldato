import pandas as pd
import numpy as np
import random


df_crudo = pd.read_csv('teoxane_sales_dirty.csv', sep='\n', header=0, names=['raw_data'])
df = df_crudo['raw_data'].str.split(',', n=4, expand=True)