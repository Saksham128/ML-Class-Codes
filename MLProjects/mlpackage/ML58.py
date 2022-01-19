import numpy as np
import matplotlib.pyplot as plt
import math
#Implementation of linear regression
#------------------------------------------------
def estimate_coef(x,y):
    #numbers of observations/points/training data
    n = np.size(x)
    #n = len(x)

    #mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    SS_xy = np.sum(x *y)-n * m_x * m_y
    SS_xx = np.sum(x * x) - n * m_x * m_x

    #Calculating regression coefficients
    m = SS_xy /  SS_xx
    c = m_y - m * m_x  # c = y-mx
    return (m,c)

def plot_regression_line(x,y,b):
    #plotting the actual points as scatter plot
    plt.scatter(x,y,color="r",marker="o",s=30)
    y_pred = b[0] + b[1] * x

    plt.scatter(x,y_pred ,color="g",marker="o",s=60)
    plt.plot(x,y_pred,color="b")
    #putting labels
    plt.xlabel("--------------x----------->")
    plt.ylabel("--------------y----------->")
    #funtion of show plot
    plt.show()

def startAIAlgorithm():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])
    #estimating coefficients
    m,c = estimate_coef(x,y)      #sender values
    print("Estimated coefficients:\n")
    print("slope m =",m)
    print("y-Intercept c=",c)
    print("Model : y=",m,"* x +",c)

    plot_regression_line(x,y,[c,m])
if __name__ == "__main__":             #This is main function
    startAIAlgorithm()



#  Drawback of this ML algorithm
#  1)Historic Data & ML logic in same code file
#  2)All calculations done mannually
#  3)Model not applied for future predictions