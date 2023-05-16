"""
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

Or the other way around, if you multiply the standard deviation by itself, you get the variance!



"""
import numpy

import os

os.system('cls')
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
speedVariance = numpy.var(speed)
print(f'Variance = {speedVariance}')
# Meaning that most of the values are within the range of 0.9 from the mean value, which is 89.769