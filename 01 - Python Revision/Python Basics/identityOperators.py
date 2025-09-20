# Identity operators are used to compare the memory locations of two objects.
# Python has two identity operators: 'is' and 'is not'
#1. is Operator
# The is operator checks if two variables refer to the same object in memory. It 
#returns True if both variables point to the same object; otherwise, it returns False.
# Syntax:
# value1 is value2
# Ex:
a = 5
b = 5
print(a is b)       # Output: True

c = [1, 2, 3]
d = c
e = [1, 2, 3]

print(c is d)  # Output: True (c and d point to the same object)
print(c is e)  # Output: False (d and e have the same values but are different objects)

#2. is not Operator
# The is not operator checks if two variables do not refer to the same object in memory.
# It is the negation of the is operator.

# Syntax: x is not y
# Ex:   
x = 1000
y = 1000
print(x is not y)  # Output: True (large integers are not interned). For immutable objects 
#like integers, strings, and tuples, Python may reuse memory locations for efficiency (a concept known as interning ).

