#1. String Data Type
var1 = 1            # int data type
var2 = 2.5          # float data type
var2 = True         # boolean data type
var4 = "10 + 3j"    # complex data type

str1 = "Hello World"


print (str)         # Prints complete string
print (str[0])      # Prints first character of the string
print (str[2:5])    # Prints characters starting from 3rd to 5th
print (str[2:])     # Prints characters starting from 3rd character
print (str  * 2)    # Prints string two times
print (str + "TEST") # Prints concatenated string


#2.  List Data Type
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list2 = [123, 'john']

print (list1)           # Prints complete list
print (list1 [0])       #Prints first element of list1
print (list1[1:3])      # Prints elements starting from 2nd till 3rd 
print (list1[2:])       # Prints elements starting from 3rd element
print (list2 * 2)       # Prints list2 two times
print (list1 + list2)   # Prints concatenated lists


#3. Tuple Data Type
tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuple2 = (123, 'john')

print (tuple1)               # Prints the complete tuple1
print (tuple1[0])            # Prints first element of tuple1
print (tuple1[1:3])          # Prints elements of tuple1 starting from 2nd till 3rd 
print (tuple1[2:])           # Prints elements of tuple1 starting from 3rd element
print (tuple2 * 2)           # Prints the contents of tuple2 twice
print (tuple1 + tuple2)      # Prints concatenated tuples

# The difference between lists and tuples is that lists are mutable and tuples are immutable. 
# That is, the elements of a list can be changed after creation, while those of a tuple cannot. 
# Tuples can be thought of as constants or read-only, while lists can be thought of as variables.


#4. Range Data Type 
# Syntax: range(start, stop, step)
for i in range(10):
    print(i)            # Prints numbers from 0 to 9

for i in range(1, 10):
    print(i)            # Prints numbers from 1 to 9

for i in range(1, 10, 2):
    print(i)            # Prints odd numbers from 1 to 9. That is, prints i and then i+2 in the range from 1 to 9.

#5.  Dictionary Data Type
#Dictionaries are used to store key-value pairs. A dictionary is enclosed by curly braces {} and values can be assigned and accessed using square braces [].
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tiny_dict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])         # Prints value for 'one' key
print (dict[2])             # Prints value for 2 key
print (tiny_dict)           # Prints complete dictionary
print (tiny_dict.keys())    # Prints all the keys
print (tiny_dict.values())  # Prints all the values


#6.  Binary Data Type

# A binary data type in Python is a way to represent data as a series of binary digits, 
# which are 0's and 1's. It is like a special language computers understand to store and 
# process information efficiently.
# This data type is commonly used when dealing with things like files, images, or anything that can be represented
# using just two possible values.
# We have 03 ways to represent binary data type:

# a. Bytes
# The byte data type in Python represents a sequence of bytes, where each byte is an integer value between 0 and 255.
# It is commonly used to store binary data such as images, files, or network packets.
# We create bytes in Python using the built-in bytes() function or by prefixing a sequence of number with b.
# Example: Using bytes() function to create bytes
b1 = bytes ([65, 66, 67, 68, 69])
print (b1)                          # output = b'ABCD'

# Example: Using prefix b to create bytes
b2 = b'Hello'
print(b2)                           # output = b'Hello'

# b. Bytearray
# The bytearray data type in Python is similar to the bytes data type, but it is mutable, 
# meaning you can modify the values stored in it after it is created.
# You can create the bytearray using the bytearray() function or by prefixing a sequence of number with ba, 
# or by encoding a string using a "UTF-8" encoding.

# Example: Using bytearray() function to create bytearray
value = bytearray([72, 101, 108, 108, 111])
print (value)                           # output = bytearray(b'Hello')

# Example: Creating a bytearray by encoding a string
val = bytearray('Hello', 'utf-8')
print (val)                             # output = bytearray(b'Hello')


# c. Memoryview
# The memoryview data type in Python is a read-only view of a sequence of bytes.
# It is used to access the underlying data of a bytes object without copying it.
# You can create the memoryview using the memoryview() function or by prefixing a sequence of number with memoryview.
# Example: Using memoryview() function to create memoryview
data = b'Hello'
value = memoryview(data)
print (value)                           # output = <memory at 0x7f8d8c0e7f60>

# Example: Creating a memoryview by prefixing a sequence of number with mv
val = memoryview([72, 101, 108, 108, 111])
print (val)                             # output = <memory at 0x7f8d8c0e7f60>
# If you have an array object, you can create a memoryview using the buffer interface as shown below
import array
arr = array.array('i', [1, 2, 3, 4, 5])
print (memoryview(arr))                 # output = <memory at 0x7f8d8c0e7f60>


#7.  Set Data Type 
# A set in Python is an unordered collection of unique elements.
set1 = {1, 2, 3, 4, 5}
set2 = {'Java', 'Python', 'JavaScript'}
print(set1)                         # output = {1, 2, 3, 4, 5}
print(set2)                         # output = {'Java', 'Python', 'JavaScript'}


# 8.  Python Boolean Data Type
# This data type represent one of the two values either True or False.
# Python bool() function allows you to evaluate the value of any expression and 
# return either True or False based on the expression.
a = True
print(a)        # display the value of a. That is, output = True
print(type(a))      # display the data type of a. That is, output = <class 'bool'>, indicating
                            #it's a boolean.
                            

# The following is another program which evaluates the expressions and prints the return values

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))


#9. None Data type
# The nonetype is represents the null type of values of or absence of a value.
# In the example below, we are assigning None to a variable x and printing its type,
# which will be nonetype
x = None

# Printing its value and type
print("x = ", x)                # Output: x = None
print("type of x = ", type(x))  # Output: type of x = <class 'NoneType'>



# Getting  Data Type
# We use the in-built  type() function to get data types in Python
# Example:
# Getting data type of values
print(type(123))
print(type(9.99))
# Getting type of variables 
a = 10
b = 2.12
c = "Hello"
d = (10, 20, 30)
e = [10, 20, 30]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Output
# <class 'int'>
# <class 'float'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'tuple'>
# <class 'list'>

# Setting Data Type
# Data types in Python are set automatically at run time. No need to set it manually.
# Example:
x = 10
print("x = ", x)    # Prints value of x. Output: x = 10
print("type of x = ", type(x))  # Prints type of x. Output: type of x = <class 'int'>

# Now, assigning string value to
# the same variable
x = "Hello World!"
print("x = ", x)        # Output: x = Hello World
print("type of x = ", type(x))      # Output: type of x = <class 'str'> 


# Primitive and Non-primitive  Data Types
# 1. Primitive Data Types are the fundamental data types that are used to create complex
# data types. These primitive data types include: Integers, Floats, Booleans, and Strings.

#2. Non-primitive Data Types store values or collection of values. They include: Lists, Tuples.
# Dictionaries, and Sets.


# Python Data Type Conversion
# To convert data between different Python data types, you simply use the the type name as a
# function. 
# Example:
print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3.3")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)

# Data Type Conversion Functions

#1. Python int() function
# Converts x to an integer. Base specifies the base if x is a string.

#2. Python long() function
# Converts x to a long integer. Base specifies the base if x is a string. This function
#has been deprecated.

#3. Python float() function
# COnverts x to a floating-point number.

#4. Python complex() function
# Converts x and y to a complex number, and returns a complex number whose real part is
# x and imaginary part is y. That is, it create a complex number.

#5. Python str() function
# Converts object x to a string representation 

#6. Python repr() function
# Converts object x to an expression string.

#7. Python eval() function 
# Evaluates a string and returns an object.

#8. Python tuple() function
# Converts to a tuple.

#9. Python list() function
# Converts to a list.

#10. Python dict() function
# Converts to a dictionary.

#11. Python set() function
# Converts to a set.

#12. Python frozenset() function
# Converts to a frozen set.

#13. Python chr() function
# Converts an integer to a character.

#14. Python ord() function
# Converts a single character to its integer value.

#15. Python unichr() function
# Converts an integer to a unicode character.

#16. Python hex() function
# Converts an integer to a hexadecimal string

#17. Python oct() function 
# Converts an integer to an octal string

