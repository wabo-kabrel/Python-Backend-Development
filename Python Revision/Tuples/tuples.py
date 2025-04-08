# A tuple is a collection of ordered, immutable elements. It's similar
#to a list, but once created, you can't modify its contents.


# Syntax:
'''
    my_tuple = (1, 2, 3)

'''
# NB: Even though the parentheses () are common, the commas are what actually
#define a tuple.
t = 1, 2, 3     # This is still a tuple


# Ex:
person = ("Alice", 25, "Engineer")
print(person[0])  # Output: Alice


# Key Features:
# - Tuples can hold different data types.
# - They can have repeated values.
# - Elements have a fixed position/index.
# - Cannot change after creation (immutable).

# Why Use Tuples?
# - Faster than lists (more memory efficient).
# - Useful for fixed data (e.g. coordinates, database rows).
# - Can be used as dictionary keys.
# - Great for function returns.


# Tuples Operations
#1. Indexing:
t = (10, 20, 30)
print(t[1])  # Output: 20

#2. Slicing:
print(t[1:])  # Output: (20, 30)

#3. Looping:
for item in t:
    print(item)

#4. Unpacking:
x, y, z = t
print(x)  # Output: 10. Since t = (10, 20, 30)


# Immutability Example
t = (1, 2, 3)
t[0] = 10  # ❌ Error: 'tuple' object does not support item assignment


# Nested Tuples
nested = ((1, 2), (3, 4))
print(nested[0][1])  # Output: 2


# When to Use Tuples
# - When data doesn't change.
# - As a function return (e.g. returning multiple values).
# - When performance matters.

