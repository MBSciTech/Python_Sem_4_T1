import pandas as pd
import numpy as np

#PB31

#Convert this file into a pandas Data Frame. (0.5 marks)
df = pd.read_csv('mydata.csv')

#Display basic information like memory and data types for this data frame. 
print(df.info())

#Display basic statistics like mean, std, quartiles, etc. for this data frame. 
print(df.describe())

#Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight.
print(df.corr())

#Do Height and Weight contain any outliers? 
#???