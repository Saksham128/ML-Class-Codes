import numpy as np
n1 = np.array([4,5,6])
n2 = np.array([1,2,3])
print(  "\n\n"  )
print( "n1   =   " ,n1     )   #[4,5,6]
print( "n2   =   " ,n2     )   #[1,2,3]
print( "n1 + n2 = ", n1 + n2  )
print( "n1 - n2 = ", n1 - n2  )
n3 = np.array([4,5,6,7])
#print( n1 + n3 )

import numpy as np
n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])
print("Before : ", n4 )
print( sorted(n4)  )     #External Sorting
print("After : ", n4 )
n4.sort( )   #In-place sorting  or Internal Sorting
print( "After n4.sort() = ", n4  )