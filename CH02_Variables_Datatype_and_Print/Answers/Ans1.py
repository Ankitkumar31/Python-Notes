'''
1. Write a python program to print the following string in a specific format(see the output).
output:

Twinkle , twinkle, little star,
        How I wonder what you are!
              up above the world so high,
              Like a diamond in the sky.
Twinkle , twinkle , little star,
        How I wonder what you are
'''

# There are two methods : 

# Method 1 : Using multi string in print function which is writen mannualy.

print(''' 
      Twinkle , twinle, little star
              How i wonder what you are!
                  up above the world so high,
                  like a diamon in the sky.
      Twinkel, twinkle ,little star,
            How I wonder what you are
''')

# Method 2 : Using escape sequence character : 
print ("\nSecond method:\n")
print("Twinkle , twinkle,little star\n\tHow i wonder what you are!\n\t\tup above the world so high,\n\t\tlike a diamon in the sky.\nTwinkle, twinkle little star\nHow i wonder what you are")

