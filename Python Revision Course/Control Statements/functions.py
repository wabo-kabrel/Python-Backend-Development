# A function is defined in Python using the def keyword.
def greet():
    print("Hello, world!")
greet()                     # Calling the function

# Functions can take inputs known as parameters or arguments
def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!

# Functions can return values using the Return keyword
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# You can assign default parameters 
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("John")  # Output: Hello, John!

# You can call functions using named arguments, improving readability.
def profile(name, age):
    print(f"{name} is {age} years old.")

profile(age=25, name="John")

# Arbitrary Arguments
# For flexible number of arguments:
# *args: Non-keyworded arguments (tuple)
# **kwargs: Keyworded arguments (dictionary)
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # Output: 10
