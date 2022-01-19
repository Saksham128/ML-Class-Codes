d =  { 'A':'Java', 'C':'J2EE', 'B':'Android',
       'D':'Python', 'E':'Hadoop',  'Key':'Value',  12:'Delhi'}
del d['E']
print( "After deletion of 'E' " , d    )

print( "d['B'] = " , d['B']    )
print( "d[12]  = " , d[12]     )
#print( "d['Z'] = " , d['Z']    )
if 'Z' in d :
    print( "d['Z'] = " , d['Z']    )
else:
    print("Value not exist.")

print( "Value from dictionary = ", d.get('Z', "Value not found.") )
print( "len(d)=" , len(d)   )