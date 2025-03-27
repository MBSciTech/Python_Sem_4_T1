import pandas as pd
import numpy as np

a = 'hello'
b = [1,2,3]
c = (1,2,3)
d = {'a':1,'b':2}
e = np.arange(3)

ser1 = pd.Series(a)
ser2 = pd.Series(b)
ser3 = pd.Series(c)
ser4 = pd.Series(d)
ser5 = pd.Series(e)

print(ser1)
print(ser2)
print(ser3)
print(ser4)
print(ser5)