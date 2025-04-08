# A set is an unordered, unindexed collection of unique elements
#in Python.


# Syntax:
'''
    my_set = {1, 2, 3}

'''


# Features:
# - Defined using {} or the set() constructor.
# - Each item is unique.
# - You can only store immutable (hashable) items like numbers, strings, tuples.
# - You can't access items by index.
# - You can add or remove items (mutable).


# NB: You can't create an empty set with {} — that creates an empty dictionary. 
#Use set() instead.
empty_set = set()


# Ex:
fruits = {"apple", "banana", "orange"}
print(fruits)  # Unordered output


# Common Set Operations
#1. Add an item
fruits.add("grape")

#2. Remove an item
fruits.remove("apple")      # Raises an error if not found.
fruits.discard("apple")     # Does not raise an error if not found.

#3. Check membership
"apple" in fruits  # True or False

#4. Set Union (OR)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}

#5. Set Intersection (AND)
print(a & b)  # Output: {3}

#6. Set Difference
print(a - b)  # Output: {1, 2}
print(b - a)  # Output: {4, 5}

#7. Symmetric Difference
print(a ^ b)  # Output: {1, 2, 4, 5}


# Use Cases of Sets
# - Removing duplicates from a list.
my_list = [1, 2, 2, 3, 4, 4]
unique = set(my_list)  # {1, 2, 3, 4}

# - Fast membership tests ('in' is faster in sets than in lists).
# - Set math (union, intersection, etc.).
# - Comparing data collections.


# NB: 
# - Unhashable types (like lists or dictionaries) can't be added to a set.
s = {1, [2, 3]}  # ❌ Error: unhashable type: 'list'

# - Sets are not ordered, so you can't index or slice them.


# frozenset:
# Used to created an immutable version of a set.
fs = frozenset([1, 2, 3])
# fs.add(4) ❌ Not allowed, it's frozen


