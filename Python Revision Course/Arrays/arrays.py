# An array is a collection of the same type stored in a 
#contiguous memory location.
# Arrays are used when you need to store a large number of 
#numeric data and want performance and memory efficiency.

# Python has a built-in module called 'array' for creating arrays.

# Arrays vs Lists
# - Python lists are more flexible than arrays.
# - Lists can hold different data types (e.g. strings, integers, objects).
# - But if you're working with large numerical datasets, arrays are more
#efficient in memory and performance.


# How to Use Arrays (with the 'array' module):
#1 - Import the array module
import array

#2 - Create an array
from array import array

numbers = array('i', [1, 2, 3, 4, 5])  # 'i' means integer
print(numbers)


# Common type codes:
# - 'i'     int        Signed integer
# - 'f'     float       Floating point
# - 'd'     float       Double precision
# - 'u'     Unicode     Unicode characters


# Basic Array Operations
#1. Access elements
print(numbers[0])  # Output: 1

#2. Update elements
numbers[2] = 10
print(numbers)  # [1, 2, 10, 4, 5]

#3. Add elements
numbers.append(6)

#4. Remove elements
numbers.remove(2)

#5. Get Length 
print(len(numbers))  # 5

#6. Loop through array
for num in numbers:
    print(num)


# Use Case
# When doing heavy math (e.g. data processing, scientific computing), you'll 
#often use:
# - array module – for basic, memory-efficient arrays.
# - NumPy arrays – for more advanced, high-performance numerical operations.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # [2, 4, 6, 8, 10]


