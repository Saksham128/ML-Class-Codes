#-----------------------------------------------------------------8-------------
#The range() Function
print( "range(10) = ", list(range(10) ) ) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print( "range(5 , 10) = ",
       list( range(5,10) )   )                # [5, 6, 7, 8, 9]

print( "range(0 , 10 , 3) = ",
       list( range(0,10,3) )    )              # [0, 3, 6, 9]

print(  sorted( range(1, 11), reverse=True)  )

print(  sorted( range(2, 101,2), reverse=True)  )

print( "range(10 , 10 , 3) = ", list(range(10,10,3) )    )   # [ ]
print( "range(-10, -100, -30) = ", list(range(-10, -100, -30))     )    #[-10, -40, -70]