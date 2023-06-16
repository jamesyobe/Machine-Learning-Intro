import pandas as pd
import os
# We will use some methods from the sklearn module, so we will have to import that module as well:
from sklearn import linear_model
"""
Multiple Regression
Multiple regression is like linear regression, but with more than one independent value, 
meaning that we try to predict a value based on two or more variables.

"""
os.system('cls')

# Read in the data from the "population_counts.csv" file into a Pandas DataFrame
df = pd.read_csv(
    r'C:/Users/james.yobe\Documents/Git-Repo/Machine-Learning-Intro/Apps/multiple_regression/data/data.csv')
print(df)

# Review the first five rows of the DataFrame

# Then make a list of the independent values and call this variable X.

# Put the dependent values in a variable called y
X = df[['Weight', 'Volume']]
y = df['CO2']

"""
From the sklearn module we will use the LinearRegression() method 
to create a linear regression object.

This object has a method called fit() that takes the independent and dependent
 values as parameters and fills the regression object with data that describes the relationship:
"""
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

# Now we have a regression object that are ready to predict CO2 values
# based on a car's weight and volume:
# predict the CO2 emission of a car where the weight is 2300kg,
# and the volume is 1300cm3:
carWeight = input('Enter weight of a car: ')
carVol = input('Enter volume of a car: ')
predictedCO2 = regr.predict([[float(carWeight), float(carVol)]])
print(f'For a car that weighs {carWeight} kgs  and has a volume of {carVol} cm3, its predicted CO2 emmission is {round(predictedCO2[0])} grams of CO2 for every kilometer it drives.')
