

"""
[eod] [code]import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.preprocessing import PolynomialFeatures

x_train = pd.read_csv("D:\\ML\\data\\x_train.csv")
y_train = pd.read_csv("D:\\ML\\data\\y_train.csv")
y_train = y_train.loc[:,:]

x = np.array(x_train)
y = np.array(y_train)

def loss(x,y,theta):
    x = np.array(x)
    y = np.array(y)
    n = x.shape[0]
    
    theta = np.array(theta).reshape(2,1)
    h = x.dot(theta)
    cost = 1/(2*n) * np.sum((h - y)**2)
    
    return cost

# x = np.array(x_train)
# y = np.array(y_train)

# x = np.array(x_train).reshape(-1,1)

x = np.array(x_train).reshape(-1,1)
y = np.array(y_train).reshape(-1,1)

x = np.insert(x, 0, values=1, axis=1)

print(x.shape)
print(x[:2])
print(y.shape)


x = np.array(x_train)
y = np.array(y_train)

x = np.insert(x, 0, values=1, axis=1)

def predict(x, theta):
    x = np.array(x)
    n = x.shape[0]
    
    theta = np.array(theta).reshape(2,1)
    h = x.dot(theta)
    
    predict = np.vectorize(lambda i: 1 if i >= 0.5 else 0)(h)
    
    return predict

initial_theta = np.zeros(2)
result = optimize.minimize(loss, x0=initial_theta, args=(x,y), method='L-BFGS-B', jac=None, hess=None, hessp=None, bounds=None, constraints=(), tol=None, callback=None,  options={'disp': True, 'maxiter': 500})
print(