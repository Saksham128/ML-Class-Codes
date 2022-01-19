
from operator import itemgetter
products=[ ('Mouse',   400),
           ('Keyboard',300),
           ('Monitor', 400),
           ('CPU',     800),
           ('UPS',     200)
         ]
#Sorting on the basis of index 1 values
print( sorted( products, key=itemgetter(1), reverse=True)  )
#Sorting on the basis of index 0 values
print( sorted(products, key=itemgetter(0), reverse=True )  )

#Sorting on the basis of index 1 first and then 0 values
print( sorted(products, key=itemgetter(1,0)              )  )

