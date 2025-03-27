import pandas as pd
import numpy as np

df = pd.read_csv('mydata.csv')

#PB27
print(df.dropna(axis=1))
