#  membership operators in Python help us determine whether an item is present in a 
#given container type object, or in other words, whether an item is a member of the 
#given container type object.
# Python has two types of membership operators: 'in' and 'not in' operators.

#1. in Membership Operator
# The in operator checks if a value or variable exists within a sequence
#(such as strings, lists, tuples, sets, or dictionaries)
# Syntax: 
# value in sequence
# Ex:
print ('a' in 'apple')          # Output: True
print ('b' in 'apple')          # Output: False

fruits = ['apple','banana','cherry']
print('cherry' in fruits)       # Output: True

digits = (1, 3, 4, 5)
print(1 in digits)              # Output: True

data = {
    'name': 'Alice',
    'age' : '25'
}
print('address' in data)        #  Output: False


#2. not in Operator:
# The not in operator checks if a value does not exist within a given sequence. It is essentially the negation of the in operator. If the value is not found, it returns True; otherwise, it returns False
# Syntax: 
# value not in sequence
# Ex:
print('x' not in 'hello')       # Output: True

unique_colors = {'red', 'blue', 'green'}
print('black' not in unique_colors)  # Output: True
print('blue' not in unique_colors)   # Output: False

# Practical Use Case:

# Checking user input
user_input = input("Enter a fruit name: ")
fruits = ['apple', 'banana', 'cherry']

if user_input in fruits:
    print(f"{user_input} is a valid fruit!")
else:
    print(f"{user_input} is not in the list.")
