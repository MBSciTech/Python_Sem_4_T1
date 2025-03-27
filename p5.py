#Conver auto-mpg.csv to dataframe in pandas 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("auto-mpg.csv")
print(df.head(10))
print(df.tail(10))
print(df.info()) # Return Meta Data
print(df.shape)
print(df.describe()) # Return Analysis of Data
print(df.describe(percentiles=[0.1,0.7,0.9]))
print(df.describe(include='all')) #Add 3 more rows in Analysis unique,top,freq
print(df.describe(include=[np.number]))
print(df.describe(exclude=[np.number]))
print(df[['mpg','cylinders']])
print(df.to_string())

df = (df[df['horsepower']!='?'])
print(df)
print(df[df['horsepower']=='?'])
print(df.corr())
print(pd.crosstab(df['cylinders'],df['model year']))
# Write in Jupiter
pd.plotting.scatter_matrix(df,figsize=[15,15])
plt.plot(pd.plotting.boxplot(df))
pd.plotting.parallel_coordinates(df,'cylinders',cols=['acceleration','mpg'])