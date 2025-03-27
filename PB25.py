import pandas as pd
import numpy as np

#PB25
df = pd.read_csv('mydata.csv')
print(df.dropna())

#PB26
print(df.dropna(how='all'))

#PB27
print(df.dropna(axis=1))

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

#PB29
data = {
"A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
"B": [50, 40, 40, 30, 50],
"C": [True, False, False, False, True]
}
data = pd.DataFrame(data)
data = data.drop_duplicates()
print(data.reset_index())

#PB30
df = pd.read_csv('auto-mpg.csv')
print(df.drop(['mpg','cylinders'],axis=1))

#PB31
