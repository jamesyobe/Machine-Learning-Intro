import numpy
from scipy import stats
import os

os.system('cls')
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

meanSpead = numpy.mean(speed)

print(f'Mean =  {meanSpead}')


medianSpeed = numpy.median(speed)

print(f'Median =  {medianSpeed}')

modeSpeed = stats.mode(speed, keepdims=False)

print(f'Mode =  {modeSpeed}')


