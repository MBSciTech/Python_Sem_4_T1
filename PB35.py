import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Outliner as out

#1.Load the dataset into a pandas DataFrame (data_result.csv)  and answer the following questions.
df = pd.read_csv('data_result.csv')

#2. View the first few rows of the dataset 
print(df.head())

#3. Check the shape of the dataset 
print(df.shape)

#4. View the first last rows of the dataset
print(df.tail())

#5. Get summary statistics of numerical columns 
print(df.describe())

#6.  Get summary statistics of numerical columns with 0.58 and 0.87 percentiles
print(df.describe(percentiles=[0.58, 0.87]))

#7. Get summary statistics of all types of  columns 
print(df.describe(include='all'))

#8. Information of all columns 
print(df.info())

#9. Check for missing values 
print(df.isnull().sum())

#10.Removing duplicates if duplicates
df = df.drop_duplicates()

#11.  List out female students who have greater than 7 spi in all  semesters. 
df_female_spi = df[(df['Gender'] == 'Female') & (df['1st']>7) & (df['2nd']>7) & (df['3rd']>7) & (df['4th']>7) & (df['5th']>7)].shape[0]
print(df_female_spi)

#12.  Find number of  students those who have greater than 8 spi in all 5 semesters.
df_spi = df[(df['1st']>8) & (df['2nd']>8) & (df['3rd']>8) & (df['4th']>8) & (df['5th']>8)].shape[0]
print(df_spi)

#13. Find outliers of sem 4 result. Also represent statistical  analysis with visualization.(boxplot)
print(out.outlier(df['4th']))
plt.figure(figsize=(6,4))
plt.boxplot(df['4th'])
plt.show()
