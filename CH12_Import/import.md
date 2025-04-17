# Chapter : Import In Python

## Module:
- A module is simply a python file that we import into other python files.

### Syntax to call function from a module:

- **syntax 1:**
```
import module
module.function()
```
![code](<images/import syntax1.png>)
![output](images/import_syntax1.png)

- **syntax 2:**
```
import module as alias
alias.function()
```
![code](<images/import 2.png>)
![solution](<images/import sol 2.png>)

> Note: alias = temporary name of module valid for current program only.

- **syntax 3:**
```
from module import fun1,fun2,......
function1()
function2()
.
.
.
```
![import syntax 3](<images/import sentex 3.png>)

- **syntax 4:**
```
from module import *
function1()
function2()
.
.
.
```
![syntax 4](<images/import syntax 4.png>)
> Note: This is the lesser one that is prefered by developer because it is less readable.

## Package : 
- A package is a collection of similar type of modules.
- It is used to mangae the modules easily.
- Physically, A package is just a folder containing similar modules.

### Syntax to import a module from package:

1. syntax - 1 :
` import package.module as alias   `

2. syntax -2 :
` from pakage import module as alias`

3. syntax-3 : to import function
` from package.module import function ` 

![package](<images/package making.png>)

## Commonly used library modules:

1. math
2. random
3. time
4. calendar
5. sys
6. os
7. shutil
8. re
9. threading
10. tkinter

etc.

### 1. math module:
- provides functions related mathematics.

**a. sqrt()**
- this function returns **square root** of given number.

`    sqr_root= math.sqrt(number) `
- Example :

![Math square code](<images/math package/code.png>)
![output](<images/math package/output.png>)

**b. factorial()**
- this functions returns factorial of given number.

` fact_res = math.factorial(number)`
- example:
![code](<images/math package/math.factorial code.png>)
![output](<images/math package/maths. factorial.png>)

**c. dist()**
- this function returns distance between 2 points .

```
distance =math.dist(point1,point2)
point1 = (x1,y1) # tuple
point2 = (x2,y2)  # tuple
```
- example: 
![code](<images/math package/distance code.png>)
![output](<images/math package/distance output.png>)

```
Note: 

This is use in data science to  make recomadation system if you see movies in netflix next time show  same type of movie. 
```

**d. log()**
- this function returns log of given number

```
log_value = math.log(number)    # default base e(a.k.a natural log)
log_value = maths.log (num,base)
```
- Example 
![code](<images/math package/log code.png>)
![output](<images/math package/log output.png>)

**e. ceil()**
- this function returns next interger value of given float number :

` int_value = math.ceil(float_value) `

- example :

![code](<images/math package/ceil code.png>)
![output](<images/math package/ceil output.png>)

**f.floor()**
- this function returns base interger value of given float number.

` int_value = math.floor(float_value)`

- example :
![code](<images/math package/floor code.png>)
![output](<images/math package/floor output.png>)

etc.

> ## help(math)# if you want to learn more about it.


### 2. random Module:
- This module provides functions related to randomness.

**a. randint()**
- this function returns a random int in given range.

`  int_value = random.randint(start,stop) `

- example:
![code](<images/math package/randint code.png>)
![output](<images/math package/randint output.png>)

**b. shuffle()**
- this function makes the list unorder.

` random.shuffle(list_name) `

![CODE](<images/math package/shufle code.png>)
![output](<images/math package/shufle output.png>)

**c choice()**
- this function pick a random value from given sequence.

` value = random.choice(sequence)    # sequence = list/tuple/str/range  `

- example :
![code](<images/math package/choice code.png>)
![output](<images/math package/ceil output.png>)

**d.random()**:
- generating random number between 0 to 1 :

eg. ![code](<images/math package/random code.png>)
![output](<images/math package/random output.png>)

etc.

> ## help(random)# if you want to learn more about it.

### 3 . calandar module:

- This module provides functions related to gregorian calendar : 

**a. month()**
- this function returns calendar of given month

` cal_month = calendar.month(year,month) `

- example : 
![code](<images/math package/calendar month code.png>)
![ouput](<images/math package/calender month ouput.png>)

**b. calendar()**
- this function return calendar of given year.

` cal_year = calendar.calendar(year) `

- example :
![code](<images/math package/year.png>)
![ouput](<images/math package/year ouput.png>)

**c. isleap()**
- this function returns True if given year is leap else False.

` bool = calendar.isleap(year) `

- example : 
![code](<images/math package/year.png>)
![ouput](<images/math package/year ouput.png>)

etc.

> ## help(calendar)# if you want to learn more about it.