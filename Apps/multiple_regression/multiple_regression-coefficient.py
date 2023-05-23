"""
Coefficient
The coefficient is a factor that describes the relationship with an unknown variable.

Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.

In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. 
The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.
"""

# Example:Print the coefficient values of the regression object:
import os
import pandas as pd
from sklearn import linear_model
os.system('cls')
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(r'C:/Users/james.yobe\Documents/Git-Repo/Machine-Learning-Intro/Apps/multiple_regression/data/data.csv')
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

"""
Result Explained
The result array represents the coefficient values of weight and volume.

Weight: 0.00755095
Volume: 0.00780526

These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.

I think that is a fair guess, but let test it!

We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.

What if we increase the weight with 1000kg?
"""

regr = linear_model.LinearRegression()
regr.fit(X.values, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

"""
We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.

Which shows that the coefficient of 0.00755095 is correct:

107.2087328 + (1000 * 0.00755095) = 114.75968





It can be difficult to compare the volume 1.0 with the weight 790, but if we scale them both into comparable values, we can easily see how much one value is compared to the other.

There are different methods for scaling data, in this tutorial we will use a method called standardization.

The standardization method uses this formula:

z = (x - u) / s

Where z is the new value, x is the original value, u is the mean and s is the standard deviation.

If you take the weight column from the data set above, the first value is 790, and the scaled value will be:

(790 - 1292.23) / 238.74 = -2.1
If you take the volume column from the data set above, the first value is 1.0, and the scaled value will be:

(1.0 - 1.61) / 0.38 = -1.59

Now you can compare -2.1 with -1.59 instead of comparing 790 with 1.0.

You do not have to do this manually, the Python sklearn module has a method called StandardScaler() which returns a Scaler object with methods for transforming data sets.
"""

# ExampleGet your own Python Server Scale all values in the Weight and Volume columns:


scale = StandardScaler()
scaledX = scale.fit_transform(X)

print(scaledX)

#Result:Note that the first two values are -2.1 and -1.59, which corresponds to our calculations: