import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#BOXPLOT
df = pd.read_csv("auto-mpg.csv")
sns.boxplot(x = df['cylinders'],y = df['mpg'],data = df)

#SCATTER
plt.figure(figsize=(8,6))
sns.scatterplot(x = 'mpg', y = 'weight', data= df)
plt.xlabel('mpg')
plt.ylabel('weight')
plt.title("ScatterPlot")
plt.xticks(rotation = 90)

#STACKPLOT
year = [950,1950,1970,1980,1990,2000,2010,2018]
region = ['Africa','America']
population = [[0.22,0.28,0.36,0.47,0.63,0.81,1.8,1.27],
              [0.34,0.42,0.52,0.61,0.72,0.84,0.94,1.80]
             ]
fig,ax = plt.subplots()
ax.stackplot(year,population,labels = region)
ax.set_xlabel('Year')
ax.set_ylabel('Population')
plt.xticks(rotation=90)
ax.legend()

#FILL BETWEEN
x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(8,6))
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)')
plt.fill_between(x,y1,y2,where=(y1 > y2),color='lightblue',alpha=0.5,label='sin > cos')
plt.fill_between(x,y1,y2,where=(y1<=y2),color='lightcoral',alpha=0.5,label='cos>sin')
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.title('File example')
plt.legend()

#WAFFLE PLOT
value = [12,22,16,38,12]
from pywaffle import Waffle
plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=value,
    columns=10,
)

cylinder_count = df['cylinders'].value_counts()
fig = plt.figure(
    FigureClass=Waffle,
    rows = 10,
    values= cylinder_count,
    labels= [f'{key}({value})' for key,value in cylinder_count.items()],
    legend={'loc':'upper left',
            'bbox_to_anchor':(1,1)},
    figsize=(8,6)
)

#REGPLOT
plt.figure(figsize=(8,6))
ax = sns.regplot(x = 'mpg', y='weight',data = df,color='green',marker='+')
ax.set(xlabel = 'mpg', ylabel = 'weight')
ax.set_title('mpg vs weight')
plt.show()


