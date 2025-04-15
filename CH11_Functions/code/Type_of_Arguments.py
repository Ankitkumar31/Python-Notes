def show(a,b):
    print(a,b)

show(10,20) # Postional Argument

# by default postion depends on place of call and in that searies
# it will store to value

show(a=10,b=20)  # Keyword Argument
show(b=20,a=10)    # keyword Argument

def show(a=0,b=1):
    print(a,b)

show() # default argument 
show(10) # default argument
show(b=20) # default argument 

# use cases of these 3 argument : 

def show(a,b):
    print(a,b)

show(10,b=20)  
# show (a= 10,20) error , first we pass position argument then keyword
# show (a=10,b=20,a=30) # error keyword arg repeted : 'a'
# show(a=10,c=20) # error , unexpected keyword arg:'c'

# show(10,a=20) # error, got multiple value for 'a'


#def show(a=1,b):
 #   print(a,b)   # throw error first you have give position argument.