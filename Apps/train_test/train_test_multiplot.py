"""
Evaluate Your Model
In Machine Learning we create models to predict the outcome of certain events, like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.

To measure if the model is good enough, we can use a method called Train/Test.


What is Train/Test
Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the data set into two sets: a training set and a testing set.

80% for training, and 20% for testing.

You train the model using the training set.

You test the model using the testing set.

Train the model means create the model.

Test the model means test the accuracy of the mode

Start With a Data Set
Start with a data set you want to test.

Our data set illustrates 100 customers in a shop, and their shopping habits.
"""
import os
os.system('cls')

# Example
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
from sklearn.metrics import r2_score

x = numpy.random.normal(3, 1, 100) # mean, std, size
y = numpy.random.normal(150, 40, 100) / x
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 14))


 
plt.subplot(2,2,1) # set a 2 by 2 matrix and set plot 1 in first box
plt.title("100 customers in a shop, and their shopping habits")
plt.xlabel("Number of minutes")
plt.ylabel("Amount of money spent")

plt.scatter(x, y)

"""
Split Into Train/Test
The training set should be a random selection of 80% of the original data.

The testing set should be the remaining 20%.
"""
train_x = x[:80] # 0 - 79
train_y = y[:80] # 0 - 79

test_x = x[80:]  # 80 - 100
test_y = y[80:]  # 8 - 100

"""
Display the Training Set
Display the same scatter plot with the training set:

Example
"""
plt.subplot(2,2,2) # set a 2 by 2 matrix and set plot 1 in second box
plt.title("Training Data Set")
plt.xlabel("Number of minutes")
plt.ylabel("Amount of money spent")
plt.scatter(train_x, train_y)



"""
Result:
It looks like the original data set, so it seems to be a fair selection:
"""

plt.subplot(2,2,3) # set a 2 by 2 matrix and set plot 1 in 3rdbox
plt.title("Testing  Data Set")
plt.xlabel("Number of minutes")
plt.ylabel("Amount of money spent")
plt.scatter(test_x, test_y)


"""
Result:
The testing set also looks like the original data set:



Fit the Data Set
What does the data set look like? In my opinion I think the best fit would be a polynomial regression, 
so let us draw a line of polynomial regression.

To draw a line through the data points, we use the plot() method of the matplotlib module:
"""

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100) 
plt.subplot(2,2,4) # set a 2 by 2 matrix and set plot 1 in fourth box
plt.title("Customers in a shop, and their shopping habits Model")
plt.xlabel("Number of minutes")
plt.ylabel("Amount of money spent")
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))

"""
The result can back my suggestion of the data set fitting a polynomial regression, 
even though it would give us some weird results if we try to predict values outside of the data set.
 Example: the line indicates that a customer spending 6 minutes in the shop would make a purchase worth 200. That is probably a sign of overfitting.

But what about the R-squared score? The R-squared score is a good indicator of how well my data set is fitting the model.

R2
Remember R2, also known as R-squared?

It measures the relationship between the x axis and the y axis, and the value ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.

The sklearn module has a method called r2_score() that will help us find this relationship.

In this case we would like to measure the relationship between the minutes a customer stays in the shop and how much money they spend.
"""

# Example - How well does my training data fit in a polynomial regression?

r2_train = r2_score(train_y, mymodel(train_x))

print(f'\n R-Squared for training mode: {round(r2_train,2) }')
# Note: The result 0.799 shows that there is a OK relationship.

"""
Bring in the Testing Set
Now we have made a model that is OK, at least when it comes to training data.

Now we want to test the model with the testing data as well, to see if gives us the same result.

Example
Let us find the R2 score when using testing data:
"""

r2_test = r2_score(test_y, mymodel(test_x))

print(f'\n R-Squared for test model: {round(r2_test,2)}')

# Note: The result 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict future values.


fig.suptitle(f'Time vs Amount spent in a shop. (R2 training = {round(r2_train *100) }%, R2 test = {round(r2_test * 100)}%)', fontsize=20)
plt.show()


"""
Predict Values
Now that we have established that our model is OK, we can start predicting new values.

Example
How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?
"""
numberOfMinites = float(input("\nEnter number of minutes: "))
print(f'\nA customer in the shop for  {numberOfMinites} minutes will spend ${round(mymodel(numberOfMinites),2)}')