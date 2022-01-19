#First Method
alpha=input("Enter alphabet to search : ")   #Z
searchStatus = False
for ch in "ABCDE" :
    if (ch == alpha):     #alpha = 'D'
        searchStatus = True
        break

if searchStatus == True:
        print( alpha , " found is the given word")
else:
    print( alpha , " not found is the given word")


#Second Method
alpha=input("Enter alphabet to search : ")   #Z
for ch in "ABCDE" :
    if (ch == alpha):     #alpha = 'B'
        print( alpha , "found is the given word")
        break
else:
    print( alpha , "not found is the given word")