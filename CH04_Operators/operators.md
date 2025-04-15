# Chapter: Operators In Python

-  Operatores perform mathematical, comparision , logical , searching , and others operations on operands.
- operand representd by  value/variable/expression
- operator represented by symbols and keywords
```
Example :  2 + 3 

# here 2 and 3 are operands.
#  ' + ' is operator.
```

## Types Of Operators : 
1. Arithmetic Operators 
2. Assignment Operators
3. Comparision (Relational) operators
4. Logical Operators
5. Bitwise Operators
6. Del Operator
7. Membership operator
8. Identity Operator
9. Ternary Operator

etc => it can be update in future or they can made.

### 1. Arithmetic Operators: 

a. addition (+)  <br>
b. substraction (-) <br>
c. product/multiply (*) <br>
d. true division (/) <br>
e. floor division (//) <br>
f. modulo/ remainder division (%) <br>
g. exponent/power (**)<br>

![arithmetic operators](<images/Airthmetic operator.png>)

![output](<images/Arithmetic output.png>)

### Expression : 
- Any statement that produces result is known as expression.
- it may or may not use operators.
- <mark>if it uses arithemtic operators then evaluation is done according to **precedence and associativity.**</mark>

![precedence and associatiity rule](<images/Precedence&associativity rule.png>)
### Quesiton :

```
i. print(5+5*5)
ii. print(5+5)*5
iii. print(10-2**3*2)
iv. print(100-2**3**2)
v. print(20/5*2)
```
### 2. Assignment Operators :

a. Assignmet : 
- it is used to assign a value to a variable .
- syntax =>
> variable = value/variable/expression.


> Note : it has least priority than other operator.

b. Chained Assignment: 

```
syntax :
    var1=var2=var3......= value
```
c. Compound Assignment: 
- combination of arithmetic and assignment operator.

```
1. var+= value      # var = var+value
2. var-= value      # var= var-value
3. var*=value       # var = var * value
4. var/=value       #     
```

> Note: Python Does not have Increment (a++) and Decrement (a--) operators.

d. Walrus Assignment : 
- it was added in 3.8 version to define and use a variable within expression.

- syntax:
> var:=value

```
exp: 
        physic = 8 # out of 10
        maths = 9
        # if we wan't to store the sum of 2 subject btw equation so: 
        avg=(s:=p+m)/2
        print(avg)
        print(s)
```
