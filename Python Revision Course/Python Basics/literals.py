# Python literals or constants are the notation for representing a fixed value
#in source code.
# Example:
a = 10

# Different types of python literals
#1. Integer Literal
#i Decimal literals: Represent signed(e.g. 1) or unsigned(e.g. -1) numbers.
#Digits ranging from 0 to 9 are used to create decimal literal values. 
# E.g.
a = 1
#ii. Octal Literal: Eight digit symbols ranging from 0 to 7 but prefixed by 0o or 0O.
#E.g.
b = 0O34
#iii. Hexadecimal Literal: Series of hexadecimal symbols ranging from 0 to 9 and a to f.
#Prefixed by 0x or 0X. E.g.
c = 0X1C

#2. Python Float Literal 
# E.g. 
d = 2.2
# For floating literal which is too large or too small, where number of digits before or after
#the decimal point is more, the symbol E or e followed by a positive or negative integer follows
#after the integer part. E.g.
e = 1.23E5          # This is equivalent to 123000
f = 1.23E-2         # This is equivalent to 0.0123

#3. Python Complex Literal
# A complex number comprises of a real and imaginary component. The imaginary component is any number
# (integer or floating point) multiplied by square root of "-1".
# In literal representation (&bsol;sqrt{−1}) is represented by "j" or "J". Hence, a literal representation 
# of a complex number takes a form x+yj.
# E.g.
d = 2 + 3j
print(type(d))          # Output: <class 'complex'>

#4. String Literals
# E.g.
e = "Hello"

#5. List Literals 
# E.g.
f = [1, 2, 3]

#6. Tuple Literals
g = (1, 3, 8)

#7. Dictionary Literals
h = {
    'name': 'John Doe',
    'age': 20
}