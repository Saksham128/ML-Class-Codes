#Scatter Plots
import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 2, 3, 4]
x2 = [2, 3, 4]
y2 = [5, 5, 5]
x3 = [1, 2, 3, 4, 5]
y3 = [6, 8, 7, 8, 7]
plt.scatter(x1, y1)
plt.scatter(x2, y2, marker='v', color='r')
plt.scatter(x3, y3, marker='^', color='m')
plt.title('Scatter Plot Example')
plt.show()