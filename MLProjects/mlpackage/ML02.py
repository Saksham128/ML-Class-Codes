import math
#Return the ceiling of x as a float,
# the smallest integer value greater than
# or equal to x.
print( math.ceil(4.1)  )   #5
print( math.ceil(4.4)  )   #5
print( math.ceil(4.5)  )   #5
print( math.ceil(4.9)  )   #5
#Return the floor of x as a float,
# the largest integer value less than
#  or equal to x.
print( math.floor(4.1)  )  #4
print( math.floor(4.4)  )  #4
print( math.floor(4.5)  )  #4
print( math.floor(4.9)  )  #4

#math.copysign(x, y) : Return x with the sign of y
print( "math.copysign(2, -4) =", math.copysign(2, -4) )       #-2
#math.pow(x, y) : Return x raised to the power y.
print( "math.pow(2, 4) =" , math.pow(2, 4) )             #16.0

#math.fabs(x) : Return the absolute value of x.
print( "math.fabs(-5.1) = " , math.fabs(-5.1)  )          #5.1

#math.factorial(x) : Return x factorial. Raises ValueError
#  if x is not integral or is negative.
print( "math.factorial(5) = ", math.factorial(5))     #120

#math.fsum(iterable) : Return an accurate floating point sum of values in the iterable.
                     #Avoids loss of precision by tracking multiple intermediate partial sums
print( "math.fsum([.4, .6, .2])=", math.fsum(  [.4, .6, .2]  )    )   #1.2

#math.pi :The mathematical constant pi = 3.141592..., to available precision
print("Constant value of math.pi=", math.pi  )

#math.degrees(x)Convert angle x from radians to degrees.
print("math.degrees(2.0) = " , math.degrees(2.0)  )      #114.591559026
#math.radians(x) : Convert angle x from degrees to radians.
print("math.radians(114.591559026)=", math.radians(114.591559026) )     #2

print("math.log(8,2)=", math.log(8,2) )         #2**3 = 8  = log(8, 2) = log 8 to thebase 2
print("math.sqrt(25)=" , math.sqrt(25) )