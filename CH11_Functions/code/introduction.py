# Function definition : 
'''
def colors ():
    print('black')
    print('white')

def fruits ():
    print('apple')
    print('mango')

# function calling : 

fruits()
colors()
fruits()
'''


# errors in python : 
# colors() # throws an error after definition only we can call function.
'''
def colors ():
    print('black')
    print('white')

def fruits ():
    print('apple')
    print('mango')

# function calling : 

fruits()
colors()
fruits()
'''

# if same function is defined multiple times then only latest definition is executed.
'''
def color():
    print('black')
    print('white')

color()

def color():
    print('red')
    print('green')

color()
'''

# According to scope there are 2 type : 
#1. Local varaible 
#2. Global variable


# Local Variable in python : 
'''
def multiple():
    a = 2       # Local variable
    b = 3       # Local variable
    print(a*b)

def add():
    a=2   # local variable
    b=3   # local variable
    print(a+b)

multiple()
add()
'''
# Global variable in python : 
'''
a = 12      # Global variable
b = 13      # Global variable

def multiple():
    print(a*b)

def add():
    print(a+b)

multiple()
add()
'''

# if we wan't to use our local varaible in place of global way or as a global variable:
# use global keyword:
'''
a = 2
b = 3
def multiple():
    global a,b
    a = 10       
    b = 20       
    print(a*b)

def add():
    print(a+b)

multiple()
add()
'''
# is the variable is made inside for loop is that variable is global variable:
'''
for i in range(1,5):
    print('hi')

print(i) # loop variable is global.

'''
# is the variable is made inside for if is that variable is global variable:
'''
if True:
    x=100
print(x)
'''
# but if it goes to false it will not store value:
'''
if False:
    x= 100
print(x)
'''

# 
'''
def mul(a,b):  # a, b are parameters.( also comes under local scope category)
    print(a*b)

mul(4,5)  # 4,5 are arguments
mul(6,7)  # 6,7 are arguments

'''
# def function with input()
'''
def mul(a,b):  # a, b are parameters.( also comes under local scope category)
    print(a*b)

x = int(input("Enter the no 1 : "))
y = int(input("Enter the no2 : "))

mul(x,y) # x and y are arguments.

# we can also write this : 

mul(2-1,2+1)  # 2-1 , 2+1 are arguments.

'''
# how to decide how many parameters we have to declare: 
# Question: we have 3 circle :
# Anser : the value which are always to stay constant does not change and we have so make it by def and ask the changing 
# values: eg.

'''
def circle_area(r):
    area = 3.14*r**2
    print(area)

circle_area(4.5)
circle_area(6.7)
'''

# WAP to find simple interest using function.

# formula of SI = P*r*t/100
'''
def SI():
    p=float(input("Enter the principal price : "))
    r=float(input("Enter the rate of interest: "))
    t=float(input("Enter the Time: "))
    simple_interest= (p*r*t)/100
    print(simple_interest)

SI()
print('\n\nSecond Method: \n')
# or we can do this way also :

def si(p,r,t):
    simp = (p*r*t)/100
    print(simp)

si(5000,4.5,6)
si(2000,7.0,2)
'''

# WAP to show odd or even in function: 

def odd_even(n):
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")

odd_even(26)


