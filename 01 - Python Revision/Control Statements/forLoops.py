# A for loop in Python is used to iterate over a sequence like a list,
#string, tuple, dictionary, or a range of numbers.

# Syntax:
'''
    for item in sequence:
        do something 
'''

# Ex1: Looping through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output: apple, banana, cherry


# Ex2: Looping through a string
for letter in "Python":
    print(letter)
# Output: P, y, t, h, o, n


# Ex3: Looping through a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, value)
# Output: name John, age 30, city New York


# Ex4: Using range() function
# The range function generates a sequence of numbers
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# You can add a start and end in the range() function
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5

# Or add a step
for i in range(1, 10, 2):
    print(i)
# Output: 1, 2, 3, 4, 5, 6


# Ex5: Using the break and continue statements
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3
    if i == 5:
        break     # Stop at 5
    print(i)
# Output: 1, 2, 4


# Ex6: Looping with Else
for i in range(3):
    print(i)
else:
    print("Loop finished")
# Output: 0, 1, 2, Loop finished


# Ex7: Nested for loops
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        print(x, y)
# Output: 1 a, 1 b, 2 a, 2 b, 3 a, 3 b
