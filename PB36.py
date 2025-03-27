import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Outliner as out

# Use the file movies.csv which contains 1629 rows and 18 columns. Read this csv file and display the basic information like 
#memory and data types for this data frame. 
df = pd.read_csv('movies.csv')
print(df.info())

#1. List out Movies Released in Year 2019.
print(df[(df['year_of_release']==2019)].shape[0])

#2.How Many Movies are having IMDB Rating > 7 (Display Number of Movies).
print(df[(df['imdb_rating']> 7)].shape[0])

#3.List out the Movies with ‘title’ and ‘story’ whose IMDB Votes > 20000.
print(df[(df['imdb_votes'] > 20000)][['title_x','story']].shape[0])

#4.List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies.
print(df[(df['year_of_release']==2018)][['title_x','release_date']].shape[0])

#5.Display only Movie Title with its Wikipedia Link.
print(df[['title_x','wiki_link']].shape[0])
