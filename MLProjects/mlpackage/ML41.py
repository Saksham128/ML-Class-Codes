import numpy as np
print("--Element wise Comparisons:--")
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print( "a == b : ", a == b )       #array([False,  True, False,  True], dtype=bool)
print( "a > b : ", a > b )         #array([False, False,  True, False], dtype=bool)


print( "---Array - wise comparisons:---")
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
print( "np.array_equal(a,b):" ,
       np.array_equal(a,b) )   #False

print( "np.array_equal(a,c):" ,
       np.array_equal(a,c) )   #True
