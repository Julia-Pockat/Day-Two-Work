import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

df = pd.read_csv("pendulumData.csv")

#one piece of data was a large outlier, likely because of 
#difference in units. Can throw it out by uncommenting the code below:

df = df[df['g (m/s2)'] < 100]
display(df)

display(df['g (m/s2)'])
display(df['stat uncert'])
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.scatter(x = df['g (m/s2)'], y = 'stat uncert')

print(df['g (m/s2)'].std())

plt.plot

plt.show()
  