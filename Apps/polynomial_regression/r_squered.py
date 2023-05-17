"""
R-Squared
It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.

The relationship is measured with a value called the r-squared.

The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
"""

import numpy
from sklearn.metrics import r2_score
import math

x = [ 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))


print(f'{round(r2_score(y, mymodel(x)) * 100) }%')
"""
Note: The result 0.94 = 94% shows that there is a very good relationship, and we can use polynomial regression in future predictions.

Predict Future Values
Now we can use the information we have gathered to predict future values.

Example: Let us try to predict the speed of a car that passes the tollbooth at around the time 17:00:

To do so, we need the same mymodel array from the example above:
"""
hourOfDay = input("Enter hour of day(24 hour clock): ")
speed = mymodel(int(hourOfDay))
print(f'The prdicted speed for car passing at {hourOfDay}:00  is {round(speed)} miles/hour')