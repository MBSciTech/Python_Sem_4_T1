import pandas as pd
import numpy as np

#PB28
df = pd.DataFrame([[1000],[2000],[3000],[4000],
                   [5000],[6000],[7000],[8000],
                   [9000],[20000]
                   ],columns=['salary'])
def outlier(datacolumn) :
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn,[25,75])
    IQR = Q3 - Q1
    lr = Q1 - 1.5*IQR
    ur = Q3 + 1.5*IQR
    return lr,ur

lr,ur = outlier(df['salary'])
print(df.drop(df[(df.salary>ur) | (df.salary < lr)].index))
