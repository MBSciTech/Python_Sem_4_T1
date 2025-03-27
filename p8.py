import pandas as pd
import numpy as np

sd = pd.DataFrame({
    'name':[np.nan,'cde',np.nan,'xyz','mno','cde'],
    'region' : [np.nan,'b','c','d','e','b'],
    'sales' : [np.nan,20,39,np.nan,50,20],
    'expense' : [np.nan,200,300,np.nan,np.nan,200]
})

print(sd)
print(sd.isna())
print(sd.isna().sum())
print(sd.dropna())
print(sd.dropna(how='any'))

#'thresh' peramiter will keep only the raws with atleast given non nan values.
print(sd.dropna(thresh=2))
print(sd.dropna(subset=['sales','expense']))
print(sd.dropna(axis='columns'))
print(sd.fillna("python"))
print(sd.drop(4,axis=0))
print(sd.drop_duplicates())