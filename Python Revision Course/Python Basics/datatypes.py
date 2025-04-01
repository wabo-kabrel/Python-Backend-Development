#1. String data type
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


#2.  List data type
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list2 = [123, 'john']

print (list1)           # Prints complete list
print (list1 [0])       #Prints first element of list1
print (list1[1:3])      # Prints elements starting from 2nd till 3rd 
print (list1[2:])       # Prints elements starting from 3rd element
print (list2 * 2)       # Prints list2 two times
print (list1 + list2)   # Prints concatenated lists


#3. Tuple data type
tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuple2 = (123, 'john')

print (tuple1)               # Prints the complete tuple1
print (tuple1[0])            # Prints first element of tuple1
print (tuple1[1:3])          # Prints elements of tuple1 starting from 2nd till 3rd 
print (tuple1[2:])           # Prints elements of tuple1 starting from 3rd element
print (tuple2 * 2)           # Prints the contents of tuple2 twice
print (tuple1 + tuple2)      # Prints concatenated tuples

# The difference between lists and tuples is that lists are mutable and tuples are immutable. That is, the elements of a list can be changed after creation, while those of a tuple cannot. Tuples can be thought of as constants or read-only, while lists can be thought of as variables.


#4. Range data type 
# Syntax: range(start, stop, step)
for i in range(10):
    print(i)            # Prints numbers from 0 to 9

for i in range(1, 10):
    print(i)            # Prints numbers from 1 to 9

for i in range(1, 10, 2):
    print(i)            # Prints odd numbers from 1 to 9. That is, prints i and then i+2 in the range from 1 to 9.

#5.  Dictionary data type
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


#6.  Binary data type

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


#7.  Set data type