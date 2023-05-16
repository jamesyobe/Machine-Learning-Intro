"""
Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

"""
import numpy

import os

os.system('cls')
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
speedStd = numpy.std(speed)
print(f'Standard Deviation = {speedStd }')
# Meaning that most of the values are within the range of 0.9 from the mean value, which is 89.769