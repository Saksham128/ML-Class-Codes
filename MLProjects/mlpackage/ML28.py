d =  { 'A':'Java', 'C':'J2EE', 'B':'Android',
       'D':'Python', 'E':'Hadoop',  'Key':'Value'}
print( "'A' in d = " , 'A' in d    )
print( "a in d = " , 'a' in d    )
print(  "d.keys() = ", d.keys()    )
print("sorted( d.keys() ) = ", sorted(d.keys() )   )
print(  "d.values() = ", d.values()    )
print(  "d.items() = ", d.items()    )

keyList = d.keys()
for k in sorted(keyList):
    print( k , d[k]    )

print(  "d.items() = ", d.items() )
print( "Data type =", type(d.items()))

for key , value in d.items():  #[ ( ,) ,  (,) , (,) , (,) , (,)   ]
    print( key , " = " , value    )