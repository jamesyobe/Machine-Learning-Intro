import matplotlib.pyplot as plt
from scipy import stats
import numpy
import os
import math
os.system('cls')
"""
In this example I will use random generated data
x = age of car
y =  speed of car
"""
# generate 20 numbers betweeen 0 and 20 for age of car
x = numpy.random.uniform(0, 5, 20)
print(f'Age of cars 0 to 20 {x}')
# generate 20 numbers betweeen 60 and 140 for speed of car
y = numpy.random.uniform(60, 140, 20)
print(f'Speed  of cars 60 to 140 {y}')

slope, intercept, r, p, std_err = stats.linregress(x, y)

rAbs = abs(r) 
rRoundedPercentage = round(rAbs * 100)

print(f'the coefficient of correlation -  called r :  {rRoundedPercentage}%')

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

ageOfCar = input("Enter age of a car: ")

# Redict future speed
speed = myfunc(int(ageOfCar))

print(f'The prdicted speed for {ageOfCar } year old car  is {speed}')


#Plot
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


