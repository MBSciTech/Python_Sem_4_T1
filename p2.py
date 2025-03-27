import pandas as pd
import numpy as np

ser = pd.Series([1,2,None],index = ['a','b','c'],name='python')
print(ser.index)
print(ser.values)
print(ser.dtypes)
print(ser.shape)
print(ser.size)
print(ser.hasnans)
print(ser.ndim)
print(ser.name)
print(len(ser))
print(ser.empty)
print(ser.count())