"""
Big Data Distributions
An array containing 250 values is not considered very big, but now you know how to create a random set of values, 
and by changing the parameters, you can create the data set as big as you want.
Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
"""
import numpy

import os
import matplotlib.pyplot as plt
os.system('cls')
data = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(data, 100)
plt.show()