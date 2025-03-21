# plottask.py
# program to plot a histogram
# Author: Daniel Finnerty

import numpy as np
import matplotlib.pyplot as plt

# set criteria
mean = 5
std_dev = 2
qty_values = 1000

# generate values based off above criteria
np.random.seed(1)
norm_dist = np.random.normal(mean, std_dev, qty_values) # source: https://www.w3schools.com/python/numpy/numpy_random_normal.asp

# calculating function values assuming 'x' values from above
norm_dist.sort() # sort numbers into ascending order. Source: https://www.geeksforgeeks.org/python-list-sort-method/
funct_values = (norm_dist) **3

plt.hist(norm_dist, bins= 20, label = ["Hist Values"], color = "lightblue", edgecolor = "grey") # added label to resolve legend error. Source: https://github.com/matplotlib/matplotlib/issues/9728
plt.plot(norm_dist, funct_values, label = ["h(x) = x^3"], color = "orange")
plt.title("Histogram and Plot", fontweight = "bold", fontsize = 14) # Bold font source: https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.xlim(0, 12) # limit size of plot given range of funct_values
plt.ylim(0,175)
plt.show()

'''
plt.savefig("plottask.png")
'''
