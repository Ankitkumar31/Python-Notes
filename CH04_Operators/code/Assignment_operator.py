# Assignment Operator: 

# i . variable = value
x = 10
print(x)

# ii. variable = variable
y=x
print(y)

# iii. variable = expression
z = x+y-1
print(z)

# Chained Assignment : 

a=b=c=d=12

print(a,b,c,d,sep='\n')

# Compound Assignment: 

a = 5 
# a=a+2
a+=2
print(a)

a*=3
print(a)

a/=7
print(a)

a-=3
print(a)

a**=4
print(a)

a//=2
print(a)

a%=2
print(a)

# Walrus Assignment: 

# if i want to make or store variable inside the equation
# for eg. i wan't 2**3  expression into a variable so here we use walrus assignment:

p = 20-2**3+2
print(p)

# method 1 : old type or before 3.8 version : 

q = 2**3
p = 20-q+2

print(p)

# method 2:  new version new assignment operator made : 

p= 20-(q:=2**3)+2

print(p)
print(q)

# this is more reliable and easy.






