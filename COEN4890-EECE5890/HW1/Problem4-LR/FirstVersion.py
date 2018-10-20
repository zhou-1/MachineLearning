
import time
import math
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from numpy import loadtxt, where
import matplotlib
# from pylab import scatter, show, legend, xlabel, ylabel


##get start time
start_time = time.time()
# scale larger positive and values to between -1,1 depending on the largest
# value in the data
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
data = pd.read_csv("data_breath_cancer.csv")

X = data.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]]
X = np.array(X)
X = min_max_scaler.fit_transform(X)
Y = data.iloc[:, [9]]
Y = np.array(Y)

# creating testing and training set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

## split training dataset as requested by this problem
total_size = 682
## set the fractions of the training data
fraction = 1
split = int(total_size * fraction)
X = X_train[:split, :]
Y = Y_train[:split, :]


##The sigmoid function
def Sigmoid(z):
    G = float(1.0 / float((1.0 + math.exp(-1.0 * z))))
    return G


##The hypothesis 
def Hypothesis(theta, x):
    z = 0
    for i in range(len(theta)):
        z += x[i] * theta[i]
    return Sigmoid(z)


##The cost function
def Cost_Function(X, Y, theta, m):
    sumOfErrors = 0
    for i in range(m):
        xi = X[i]
        hi = Hypothesis(theta, xi)
        if Y[i] == 1:
            error = Y[i] * math.log(hi)

        elif Y[i] == 0:
            error = (1 - Y[i]) * math.log(1 - hi)

        sumOfErrors += error
    const = -1 / m
    cost = const * sumOfErrors
    return cost


##The derivative of cost function
def Cost_Function_Derivative(X, Y, theta, j, m, alpha):
    sumErrors = 0
    for i in range(m):
        xi = X[i]
        xij = xi[j]
        hi = Hypothesis(theta, X[i])
        error = (hi - Y[i]) * xij
        sumErrors += error
    m = len(Y)
    constant = float(alpha) / float(m)
    cost = constant * sumErrors
    return cost


##The gradient decent
def Gradient_Descent(X, Y, theta, m, alpha):
    update_theta = []
    constant = alpha / m
    for j in range(len(theta)):
        CFDerivative = Cost_Function_Derivative(X, Y, theta, j, m, alpha)
        update_theta_value = theta[j] - CFDerivative
        update_theta.append(update_theta_value)
    return update_theta


##The logistic regression
def Logistic_Regression(X, Y, alpha, theta, num_iters):
    m = len(Y)
    for x in range(num_iters):
        update_theta = Gradient_Descent(X, Y, theta, m, alpha)
        theta = update_theta
        if x % 100 == 0:
            Cost_Function(X, Y, theta, m)
        print("The training time is %s seconds ---" % (time.time() - start_time))
    Accuracy(theta)


##Accurancy
def Accuracy(theta):
    count = 0
    length = len(X_test)
    for i in range(length):
        prediction = round(Hypothesis(X_test[i], theta))
        answer = Y_test[i]
        if prediction == answer:
            count += 1
    my_accurancy = float(count) / float(length)
    print('Accuracy is:', my_accurancy)


##Initialization
initial_theta = [0, 0, 0, 0, 0, 0, 0, 0, 0]
alpha = 0.1
iterations = 1000
Logistic_Regression(X, Y, alpha, initial_theta, iterations)
