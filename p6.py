#Write a program to read the CSV height and weight 
#Task 1 : Extract the information of CSV
#Task 2 : Write the statestical summery
#Task 3 : create a correlation table
#Task 4 : create a BoxPlot of height and weight

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('heights_weights.csv')
print(df.info())

print(df.describe())

print(df.corr())

print(pd.plotting.boxplot(df))