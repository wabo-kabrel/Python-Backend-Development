#1. What are decorators?
# - Decorators in Python are used to add extra/special features to an existing 
#   function without changing the function's original code.
# - A decorator is represent with @ 


#2. Real life example:
# - In everyday life you have a plain donut 🍩 (your function).
# - You add chocolate icing 🍫 (your decorator) — now your donut has more flavor
#   without changing the inside.


#3. How they work
# - In Python, a decorator which is a funcfion, takes another function as an input.
# - It returns a new function that adds something extra before/after calling
# - the original function
# - Basic structure: 
"""
def decorator_function(original_function):
    def wrapper_function():
        print("Something before the function runs.")
        original_function()
        print("Something after the function runs.")
    return wrapper_function
    
"""


#4. Simple example
"""
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
"""

# Output:
"""
Before the function
Hello!
After the function
"""

# Explanation:
    # - @my_decorator means “pass say_hello into my_decorator”.
    # - The decorator wraps say_hello with extra code.


#5. Example with arguments
# - If your function takes arguments, your decorator must handle them:
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Kabrel")
"""
