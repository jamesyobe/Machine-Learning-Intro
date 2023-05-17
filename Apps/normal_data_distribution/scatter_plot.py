"""
Scatter Plot
A scatter plot is a diagram where each value in the data set is represented by a dot.

The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length,
 one for the values of the x-axis, and one for the values of the y-axis:

 The x array represents the age of each car.

The y array represents the speed of each car.
"""


import os
import matplotlib.pyplot as plt
os.system('cls')


x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()
"""
Scatter Plot Explained
The x-axis represents ages, and the y-axis represents speeds.

What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.

"""