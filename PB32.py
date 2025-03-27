import pandas as pd
import numpy as np


# Use the file ipl-matches.csv which contains data of all the IPL matches from year 2008 to 2022. Read this csv file and display the
# basic information like memory and data types for this data frame. Write python code for the following cases:

df = pd.read_csv('ipl-matches.csv')

#List out all matches gone in superover.
superovers = df[df['SuperOver']=='Y']
print(superovers)

#How Many Matches won by Chennai Super Kings at Kolkata
cskWin = df[(df['WinningTeam']=='Chennai Super Kings') & (df['City']=='Kolkata')]
print(len(cskWin))

#In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians.
thalaWins = df[(df['Player_of_Match']=='MS Dhoni') & (df['Team1']=='Mumbai Indians') | (df['Team2']=='Mumbai Indians')]
print(len((thalaWins)))

#Display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match
gtWins = df[(df['TossWinner']=='Gujarat Titans') & (df['TossDecision']=='bat') & (df['WinningTeam']=='Gujarat Titans')]
print(len(gtWins))

#Display list of all matches won by Gujarat Titans
gtWins = df[(df['WinningTeam']=='Gujarat Titans')]
print(len(gtWins))