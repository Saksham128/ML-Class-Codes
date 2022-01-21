import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('insurance_data2.csv')
print( df )

X = df.iloc[:,0:1].values
Y = df.iloc[:, 1].values
print(Y)

plt.title("Insurance data")
plt.xlabel("Age")
plt.ylabel("Insured or not")
plt.scatter(X,Y)
plt.show()


n = len(Y)

m_x = np.mean(X)
m_y = np.mean(Y)

SS_xy = np.sum(X*Y) - n * m_x * m_y
SS_xx = np.sum(X*X) - n * m_x * m_x

m = SS_xy / SS_xx
print("Value of m = ", m)

c = m_y - m * m_x
print("Value of c = ", c)

y_predicted = m * X +  c
print(y_predicted)

plt.title("Insurance data")
plt.xlabel("Age")
plt.ylabel("Insured or not")
plt.scatter(X,Y)
plt.plot(X, y_predicted,  "ro-")
plt.show()


import math
def get_sigmoid(z):
    return 1 / ( 1 + np.power(math.e,-z))

plt.title("Insurance data")
plt.xlabel("Age")
plt.ylabel("Insured or not")
plt.scatter(X,Y,color='b',s=100)
plt.plot(X, get_sigmoid(y_predicted),'ro-')
plt.show()