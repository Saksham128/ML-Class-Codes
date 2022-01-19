# Pie Charts
import matplotlib.pyplot as plt

myLabels = ['S1', 'S2', 'S3']
sections = [60, 90, 50]
myColors = ['c', 'g', 'r']
plt.pie(sections, labels=myLabels, colors=myColors,
        startangle=45,
        explode=(0, 0.1, 0),
        autopct='%1.2f%%')

plt.title('Pie Chart Example')
plt.show()
