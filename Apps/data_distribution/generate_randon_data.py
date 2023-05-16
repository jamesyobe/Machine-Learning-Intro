"""
Data Distribution
Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.

In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size

Create an array containing 250 random floats between 0 and 5:
"""
import numpy

import os

os.system('cls')
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
data = numpy.random.uniform(0.0, 5.0, 250)
print(f'250 random floats between 0 and 5:  {data }')
# Meaning that most of the values are within the range of 0.9 from the mean value, which is 89.769