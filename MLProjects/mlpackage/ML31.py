print( "range(11,21)=" , list( range(11,21) )    )

from operator import itemgetter
print( "itemgetter(2)=", itemgetter(2)( range(11,21) )  )

tu = ('Python' , 'Java' ,'J2EE', 'Android', 'Hadoop'  )
print( "itemgetter(2)=", itemgetter(2)(tu)  )