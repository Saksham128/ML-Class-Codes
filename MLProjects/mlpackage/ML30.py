list1 = [ 20, 10, 30, 100, 90, 70 ]
print(   sorted(list1 )    )
print(   list1    )
list1.sort()
print(   list1    )


tx = ( 20, 10, 30, 100, 90, 70 )
ty = sorted(tx)   #In-place Sorting is not allowed in tuple
print( "tx = " ,  tx    )
print( "ty = " , ty    )
tx = ( 20, 10, 30, 100, 90, 70 )
ty = sorted(tx, reverse=True)
print( "tx = " ,  tx    )
print( "ty = " ,  ty    )
#tx.sort() # Error because tuple cant be modified.
print( tx )

