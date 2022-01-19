num=int(input("Enter any number"))
if(num%2 == 0):
    print("Even number")
else:
    print("Odd number")
print("\n----------------------------------------\n")
print("Even number") if(num%2 == 0) else print("Odd number")

arr = [ a  for a in range(1,101)  if a%5==0   ]
print(arr)