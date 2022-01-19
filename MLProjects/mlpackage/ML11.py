ar1 = [(0, 'Mary'), (1, 'had'), (2, 'a'), (3, 'little'), (4, 'lamb')]

print( list( enumerate(ar1) ) )

arr=['Mary', 'had', 'a', 'little', 'lamb']
#      0       1     2       3        4
print( enumerate(arr)   )

print( list( enumerate(arr) )  )
print( tuple( enumerate(arr) )  )

print("\n\n")

for i , j in enumerate(arr) :
    print( i , " === " , j   )

for a in enumerate(arr) :
    print( "a = ", a  )