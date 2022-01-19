import numpy as np
arr = np.array( [11, 22, 33, 0. ,44, 55] )
print( "arr.sum() = " , arr.sum()  )
print( np.sum(arr) )
print( "arr.std() = " , arr.std()  )
print( "arr.mean() = ", arr.mean() )
print( np.mean(arr) )
print( "arr.max() = " , arr.max()  )
print( "arr.min() = " , arr.min()  )
print( "arr.size = "  , arr.size   )
print( "arr.shape ="  , arr.shape  )


# following line will print( index of nonzero values
print( "arr.nonzero() = ", arr.nonzero() )

print( "arr.dtype= " , arr.dtype  )
#Are all elements greater than zero
print( np.all( [1,2,3,4] )    )     #True
print( np.all( [1,2,0,3,4] )  )     #False
#Is any elements greater than zero
print( np.any( [1,2,3,4] )     )       #True
print( np.any( [1,2,0,3,4] )    )      #True
print( np.any( [0,0,0,0.,0] )    )     #False
print( np.any( [0,0,0,0.,0,1] )   )  #True

