import pandas as pd
import numpy as np

#Convert this file into a pandas Data Frame. 
df = pd.read_csv('spotify.csv')

#Display basic informaƟon like memory and data types for this data frame.
print(df.info())

#Display basic staƟsƟcs like mean, std, quartiles, etc. for this data frame
print("Describe : ") 
print(df.describe(include='all'))

#Create a correlaƟon table for the data frame and comment about what kind of correlaƟon is there between danceability and energy
print("Correlation : ") 
print(df.corr())

#Display first five rows for this data frame
print(df.head())

#Display last five rows for this data frame
print(df.tail())

#Display the rows between 15 to 39 for this data frame
print(df[15:40])

#Display the data only for last five rows and last five columns for this data frame
print(df.tail(5).iloc[:, :5])