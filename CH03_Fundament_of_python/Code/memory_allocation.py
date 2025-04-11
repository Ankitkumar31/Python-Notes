x = 10
print(f"The value of x: {x}")
print(id(10))
print(id(x))

# id() function is used to give the virtual address of the variable or value.Virtual means it is not 
# original stored value it is created by program a random value. 

y = 10 
print(id(y))
z = 10
print(id(z))
# python is going to share same address to y for memory management reason .  
# This same thing python do for other same value variables . 


# we are going to change y value : 

y= 5
print(id(x))
print(id(y))
print(id(z))

# now the address of y is change and new address is ther 
