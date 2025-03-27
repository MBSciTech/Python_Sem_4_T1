# DATAFRAME UNDERSTANDING

import pandas as pd
import numpy as np

#CREATION OF DATAFRAME
data = {'name':['AA','IBM','GOOGLE'],'date':['1-1-2025','2-2-2025','3-3-2025'],
        'shares' : [100,30,90],
        'price' : [12.3,10.3,32.2]
        }

df = pd.DataFrame(data)
print(df)

#ACCESS OF DATAFRAME

print(df['shares'])
print(df.loc[0][1])

#ADD COLUMN

df['A new colum'] = 100
print(df)

#READ CSV

'''
Three Methods 
(1) Using the Excelsheet
(2) Using .txt file
(3) Using Jupiter Note book

'''