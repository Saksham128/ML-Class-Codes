num=int(input("Enter number for prime number testing : "))    #7
for a in range(2, num):   #[2,3,4,5,6]
   if num%a == 0 :
       print( num , " is not a prime number."  )
       break
else:
    print( num, " is a prime number."  )