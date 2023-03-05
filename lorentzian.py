import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import pandas as pd
from scipy.stats import norm
import math

n_bins = 20

def twoLorentzian(x, amp1, cen1, wid1):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2))

#reading data from the csv
df = pd.read_csv("pendulumData.csv")
print(df['g (m/s2)'].mean())
print(df['g (m/s2)'].std())

# Creating distribution
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

#bins_labels(n_bins)

#creating the normal distribution
xmin, xmax = plt.xlim()
xdif = np.linspace(xmin, xmax, 233)
x = np.arange(xmin, xmax, 0.5)
p = norm.pdf(xdif, 9.817732353472108, .7338911413111793)
p = twoLorentzian(x=xdif, cen1=9.8177, amp1=121, wid1=0.45)
#(233)*norm.pdf(xdif, 9.817732353472108, .7338911413111793)
#plt.plot(xdif, norm.pdf(xdif, df['g (m/s2)'].mean(), df['g (m/s2)'].std()))
plt.plot(xdif, p)

plt.title('Distribution of g values of J-Lab students \n' + title)

# Show plot
plt.show()