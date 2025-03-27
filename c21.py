import pandas as pd
df = pd.read_csv('auto-mpg.csv')
import matplotlib.pyplot as plt

plt.figure(figsize = (8,6))
df.set_index('horsepower')[['mpg']].plot(kind='area',alpha=0.5)
plt.xlabel('Hp')
plt.ylabel('MPG')
plt.title('Areaplot of HP vs MPG')
plt.xticks(rotation=45)
plt.show()