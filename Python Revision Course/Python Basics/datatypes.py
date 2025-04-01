# String data type
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

# List data type
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list2 = [123, 'john']

print (list1)           # Prints complete list
print (list1 [0])       #Prints first element of list1
print (list1[1:3])      # Prints elements starting from 2nd till 3rd 
print (list1[2:])       # Prints elements starting from 3rd element
print (list2 * 2)       # Prints list2 two times
print (list1 + list2)   # Prints concatenated lists

# Tuple data type
tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuple2 = (123, 'john')

print (tuple1)               # Prints the complete tuple1
print (tuple1[0])            # Prints first element of tuple1
print (tuple1[1:3])          # Prints elements of tuple1 starting from 2nd till 3rd 
print (tuple1[2:])           # Prints elements of tuple1 starting from 3rd element
print (tuple2 * 2)           # Prints the contents of tuple2 twice
print (tuple1 + tuple2)      # Prints concatenated tuples

# The difference between lists and tuples is that lists are mutable and tuples are immutable. That is, the elements of a list can be changed after creation, while those of a tuple cannot. Tuples can be thought of as constants or read-only, while lists can be thought of as variables.

# Range data type 
# Syntax: range(start, stop, step)
for i in range(10):
    print(i)            # Prints numbers from 0 to 9

for i in range(1, 10):
    print(i)            # Prints numbers from 1 to 9

for i in range(1, 10, 2):
    print(i)            # Prints odd numbers from 1 to 9. That is, prints i and then i+2 in the range from 1 to 9.

# Dictionary data type


# Binary data type