# Built-in functions in Python include:

#1. Input/Output
# - print(): prints the output to the console
# - input(): accepts user input as a string

# Ex: 
name = input("Enter your name: ")
print("Hello", name)


#2. Type Conversion
# - int():      integer
# - float():    floating point
# - str():      string
# - bool():     boolean
# - complex():  complex number
# - list():     list
# - tuple():    tuple

# Ex:
age = int("25")
print(age + 5)  # Output: 30


#3. Math and Numbers
# - abs(x):     absolute value
# - round(x):   rounds to nearest integer
# - pow(x,y):   x raised to the power y
# - max():      largest item in an iterable
# - min():      smallest item in an iterable
# - sum():      sum of items in an iterable

# Ex:
print(abs(-7))      # 7
print(round(3.6))   # 4
print(pow(2, 3))    # 8

#4. Working with Iterables
# - len():          length of an object
# - range():        generates a sequence/range of numbers
# - enumerate():    returns index + value in a loop
# - zip():          combine multiple iterables
# - sorted():       returns a sorted list
# - reversed():     reverses an iterable

# Ex:
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
# - Output: 0 a, 1 b, 2 c


#5. Logical and Utility
# - all():      returns True if all elements are True
# - any():      returns True if at least one element is True
# - eval():     evaluates a string as code
# - type():     returns the type of a variable
# - id():       returns the memory ID

# Ex:
print(all([True, True, False]))  # False
print(type(10))                  # <class 'int'>

# You can see all built-in functions by using the code below:
# print(dir(__builtins__)) or through this link https://docs.python.org/3/library/functions.html

