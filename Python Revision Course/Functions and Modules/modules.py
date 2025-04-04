# A module is simply a file containing Python code that can be reused in other 
#programs. Modules help you organize your code and reuse functionality across
#multiple scripts.


# Why use modules?
# - Code reusability
# - Better organization
# - Easier debugging and maintenance
# - Keeps your main code clean and short


# Types of modules
# - Built-in modules: Come with Python (e.g. math, random, datetime)
# - User-defined modules: Files you create yourself (e.g. my_module.py)
# - External modules: Installed using tools like pip (e.g. requests, numpy)


# Using a Built-in Module

import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.1415926535...


# Import Variations 
# You can modules in different ways: 

import math
print(math.sqrt(25))

from math import sqrt
print(sqrt(36))

from math import pi as PI
print(PI)


# Creating Your Own Module
#Let's say you create a file called my_module.py:

# my_module.py file
def greet(name):
    return f"Hello, {name}!"

pi_value = 3.1416

# You can use it in another file:
# main.py
''' 
import my_module

print(my_module.greet("John"))
print(my_module.pi_value)        

'''


# Using dir() to Explore a Module
import random
print(dir(random))  # Lists all functions and attributes in random module


# Using __name__ == "__main__"
# This lets your module act as both a reusable module and a standalone script.

# my_module.py file
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()  # Only runs if you run my_module.py directly
    

# Installing and Using External Modules
# To install external modules run the bash command below in the terminal:
# pip install requests #

# After installing, you can now use them in your code:
import requests

response = requests.get("https://api.github.com")
print(response.status_code)


