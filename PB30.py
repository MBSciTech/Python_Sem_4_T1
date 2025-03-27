import pandas as pd
import numpy as np

#PB30
df = pd.read_csv('auto-mpg.csv')
print(df.drop(['mpg','cylinders'],axis=1))