#RULE-2:Tuple is immutable
#----------------------------
tu = ('Python', 'Java','J2ee', 'Android', 'Hadoop' )
print( type(tu) , tu  )
#tu[3] = "RDBMS"    #This line is error
print("tu.index('android')= ", tu.index('Android') )  #3
print(" 'Hadoop' in tu = " ,  'Hadoop' in tu  )
print(" 'Crysta' in tu = " ,  'Crysta' in tu  )


#RULE-1: Lists are mutable
#----------------------------
a = ["Noida", "Delhi", "Lucknow", "Goa", "Kanpur"]                  # This is list
#     0         1          2        3        4
a[3] = "UK"
print( a  )
a.append("Patna")
print( a  )

del a[1]
print( a )

a.insert(0, "Varanasi")
print( a )