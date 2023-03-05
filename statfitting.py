
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import pandas as pd
from scipy.stats import norm
from scipy.stats import chisquare

n_bins = 20
#reading data from the csv
df = pd.read_csv("pendulumData.csv")
print(df['g (m/s2)'].mean())
print(df['g (m/s2)'].std())

# Creating x and y for histogram, filtering out the outlier
df = df[df['g (m/s2)'] < 900]
print(df['g (m/s2)'].mean())
print(df['g (m/s2)'].std())
x = df['g (m/s2)']
y = .75 ** x + np.random.randn(233) + 25
 
# Creating histogram
title = "Fit results: mean = %.3f,  standard deviation = %.4f, # of counts = 233" % (df['g (m/s2)'].mean(), df['g (m/s2)'].std())
plt.xlabel('g value (m/s^2)')
plt.ylabel('# of counts')
plt.hist(x, bins = n_bins, color='black')

dof = 232

#creating the normal distribution
xmin, xmax = plt.xlim()
xdif = np.linspace(xmin, xmax, 233)
x = np.arange(xmin, xmax, 0.5)
p = 233*norm.pdf(xdif, 9.817732353472108, .7338911413111793)
plt.plot(xdif, p)
x_chi, y_chi, obj = plt.hist(x, bins = n_bins, color='black')

rv = chisquare(f_obs=x_chi, f_exp=y_chi) #f_exp from normal values 
print(rv)
plt.title('Distribution of g values of J-Lab students \n' + title)
plt.show()