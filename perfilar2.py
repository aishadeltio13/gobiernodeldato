import pandas as pd
import numpy as np
import random


# Load the dataset
df = pd.read_csv('teoxane_sales_dirty.csv')

# Explore the dataset
print(df.head())
print(df.info())