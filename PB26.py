import pandas as pd
import numpy as np

#PB25
df = pd.read_csv('mydata.csv')

#PB26
print(df.dropna(how='all'))
