import warnings
warnings.filterwarnings(action="ignore")

import numpy as np
from sklearn.preprocessing import StandardScaler
data = [[0, 0],
        [0, 0],
        [1, 1],
        [1, 1]]
a = np.array(data)
#a = a.T
print("Original Data =\n", a)
scaler = StandardScaler()
print(scaler.fit(a))
print("scaler.mean_ = ", scaler.mean_)
data2 = scaler.transform(a)
print("After transformation \n" ,data2)
print("Mean = \n", np.mean(data2, axis=0)  )
print("Std = \n",  np.std(data2,  axis=0)  )