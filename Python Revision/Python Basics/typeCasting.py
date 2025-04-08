# In programming, a type casting refers to the conversion of a literal (or object)
#from one data type to another.  

# Python supports two types of type casting:

#1. Implicit Casting
# With implicit (or automatic) casting, a language compiler/interpreter automatically converts objects
#of one type to another type 

# Python is a strongly typed language which doesn't support automatic type casting between unrelated data
#types. E.g. a string cannot be converted to any number type. However, an integer can be cast into a float.

# An example of implicit type casting is implicit int to float casting which takes place when any arithmetic 
#operation on int and float operands is done.

# Consider we have the addition between the two variables below:
a = 10      # int object
b = 10.5    # float object

# To perform their addition below, the integer 10 is automatically converted to the float 10.0
c = a + b
print (c)       # The result of the addition of the two floating point numbers is 20.5 which is also a floating 
                #point number.

# In implicit type casting, a Python object with lesser byte size is upgraded to match the bigger byte size of the
#other object in the operation. E.g. a boolean object is first upgraded to int and then float, before the addition with floating
#point object.
# Ex:
d = True        # In binary, true = 1 while false = 0. So here, the boolean True is converted to an integer,
                #and then to a floating point number (1.0) before the addition takes place which produces the result
                #11.5
e = 10.5
f = d + e
print (f)


#2. Python Explicit Casting
# Although automatic or implicit casting in Python is limited to int to float, you can use built-in functions
#int(), float() and str() to perform the explicit conversions such as a string to integer.

# Example using int()
g = int (10.25)
print(type(g))      # Result: <class 'float'>

h = int(True)
print (h)           # Result: 1. Since the value of true is 1
print (type(h))     # Result: <class 'int'>

j = int("10" + "02")    # String to integer
print(type(j))          # Result: <class 'int'>
print(j)                # Result: 1002

# Binary string to integer
k = int("110011", 2)    # The string should be made up of 1s and 0s(for binary) only and the base written
                        #after the comma. For octal, the base will be 8, for hexadecimal, the base will be 16 etc. 
                        # For hexadecimal, the string may also contain alphabets from A to F. e.g. "2AD"
print(k)                # Result: 51

# Example using float
l = float ("1.00E4")  
print(type(l))          # Result: <class 'float'>

# Example using str() function
m = str(10.2)
print(m)        # Result: 'a'
print(type(m))  # Result: <class 'str'>

# Conversion of Sequence Types
# Sequence types in Python include list, tuple and string.
# A string and tuple can be converted into a list object by using the list() function. 
# Similarly, the tuple() function converts a string or list to a tuple
# Example:
n = [1,2,3,4,5]         # List
print(type(tuple(n)))    # Result: <class 'tuple'>

o = ('a', 'b', 'c', 'd')
print (type(list(o)))       # Result: <class 'list'>

print(type(str(n)))         # Result: <class 'str'>
print(str(n))               # Result: '1', '2', '3', '4', '5'