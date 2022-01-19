

#Module02.py
import Module01
Module01.show(4)
Module01.sum(2, 3)
print( Module01.count )
from Module01 import *
show(4)
sum(2, 3)
print( count )

import Module01
Module01.show(7)
Module01.sum(3, 5)
print( "Module01.count=" , Module01.count)


# Connecting with math library
import math
print( math.sqrt(25) )
print( math.pi )

#Adding all features of math library
# in the program
from math import *
print( sqrt(16) )
print( pi )
#Adding selective features of math
# library in the program
from math import sqrt, pi
print( sqrt(16) )
print( pi )
#Nick name to the Linked Library
import math as chintu
print( chintu.sqrt(25) )
print( chintu.pi )

import Module01
Module01.show(4)
Module01.sum(2, 3)
print( Module01.count )
from Module01 import *
show(4)
sum(2, 3)
print( count )
