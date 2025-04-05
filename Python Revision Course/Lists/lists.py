# A list is an ordered, mutable (changeable) collection of items.
# List can store items of any data type (integers, strings, other lists, etc.)
my_list = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.5, True]


# Creating Lists
numbers = [1, 2, 3]
empty = []
nested = [[1, 2], [3, 4]]

# Indexing and Slicing
#1. Access by Index:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple. First item is at index 0.
print(fruits[-1])    # cherry

#2. Slicing:
print(fruits[0:2])   # ['apple', 'banana']. From index 0 to 1.
print(fruits[:2])    # ['apple', 'banana']. From first item to index 1.
print(fruits[1:])    # ['banana', 'cherry']. From index 1.


# Modifying Lists
#1. Change an item:
fruits[1] = "blueberry"

#2. Add items:
# - append(): Adds to the end.
# - insert(): Adds at a specific index.
# - extend(): Adds multiple items.
fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.extend(["melon", "pear"])

#3. Removing items:
# - remove(value): Removes first match.
# - pop(index): Removes and returns item at index.
# - del: Deletes by index.
# - clear(): Removes all item.
fruits.remove("banana")
item = fruits.pop(1)
del fruits[0]
fruits.clear()


# Looping through lists 
for fruit in fruits:
    print(fruit)

# With index:
for i in range(len(fruits)):
    print(i, fruits[i])



# Useful Lists Methods
# - append(x):  	    Add item to end
# - extend([x]):        Add multiple items
# - insert(i, x):   	Insert at index
# - remove(x):      	Remove first item equal to x
# - pop(i):         	Remove and return item at index i
# - index(x):       	Return first index of x
# - count(x):       	Count number of x in list
# - sort():         	Sort the list (ascending by default)
# - reverse():      	Reverse the list
# - copy():         	Make a shallow copy
# - clear():        	Empty the list

nums = [4, 2, 7, 1]
nums.sort()     # [1, 2, 4, 7]
nums.reverse()  # [7, 4, 2, 1]

# Length of a list
len(fruits)

# Length Comprehension
# A short way to create or transform lists.
squares = [x**2 for x in range(5)]      # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested Lists
# Lists inside lists (like 2D arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][1])  # 2


# Common Pitfalls
# - IndexError if you go beyond list bounds
# - Modifying a list while iterating can cause bugs
# - remove() throws an error if the value isn't found







