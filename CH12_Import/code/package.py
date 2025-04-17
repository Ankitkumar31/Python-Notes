# # Basic Syntax of Package
# syntax 1: 
import maths.calculator as calc
a = calc.add(1,2)
print(a)

i = calc.sub(3,2)
print(i)

# syntax 2 : 
from maths import calculator as calc
b = calc.add(1,2)
print(b)

x = calc.sub(5,2)
print(x)

# syntax 3 : 
from maths.calculator import add,sub,multiply
c = add(1,2)
print(c)

d = multiply(2,5)
print(d)


# Commonly used library modules : 
