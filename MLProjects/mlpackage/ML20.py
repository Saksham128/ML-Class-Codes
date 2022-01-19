import  math
str1 = "(4 * 2) - 1"
print(str1)
print( eval(str1) )



# variable used in expression
x = int( input("Enter the value of x:")  )
y = int( input("Enter the value of y:")  )
str1 = input( "Enter the expression(in terms of x and y):")
#str1 = "2 * x * y"
# evaluating expression
z = eval(str1)
# printing evaluated result
print(  "z = ", z   )