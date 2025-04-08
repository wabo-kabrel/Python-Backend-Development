# In Python, errors are problems in a program that cause it to stop running.
# When an error occur, Python creates an object called an exception. If the
#exception is not handled, the program crashes.

# Types of Errors in Python
#1 - Syntax Errors
'''These are mistakes in the structure of the code. Python doesn't even try to run
the code if there's a syntax error.'''
#Ex:
''' if True
    print("Hello")  # Missing colon '''

# Error:
'''SyntaxError: expected ':' '''

#2. Runtime Errors (Exceptions)
# These occur while the program is running and can crash your program unless handled
#properly.


# Common Built-in Exceptions in Python
#Python has many built-in exceptions. Here are the most common ones:
# - ZeroDivisionError:          Raised when a number is divided by zero.
# - TypeError:                  Raised when an operation is applied to an object of inappropriate type.
# - ValueError:                 Raised when a function gets an argument of correct type but inappropriate value.
# - NameError:                  Raised when a variable is not defined.
# - IndexError:                 Raised when a sequence index is out of range.
# - KeyError:               	Raised when a key is not found in a dictionary.
# - FileNotFoundError:      	Raised when trying to open a non-existent file.
# - AttributeError:         	Raised when an invalid attribute is accessed on an object.
# - ImportError:            	Raised when an import fails.


# Example of an Exception
x = 10
y = 0
print(x / y)



# Handling Exceptions with try-except
# You can use try-except blocks to catch and handle exceptions, so your
#program doesn't crash. 
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")


# The 'else' and 'finally' Blocks
# - else: Runs if no exception occurs.
# - finally: Always runs, whether or not an exception occurred.
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")



# Raising Exceptions Manually
# You can raise your own exceptions using the 'raise' keyword.
age = -5
if age < 0:
    raise ValueError("Age can't be negative")
# Output:   ValueError: Age can't be negative



# Custom Exceptions
# You can create your own exceptions by inheriting from the Exception class.
class MyCustomError(Exception):
    pass

raise MyCustomError("This is a custom error!")



                    # Summary

#   Concept	                Purpose
# - Syntax Errors	        Errors in code structure
# - Exceptions	            Runtime issues
# - try-except	            Handling errors
# - else	                Executes if no error
# - finally	                Executes no matter what
# - raise	                Trigger custom errors
# - Custom Exceptions	    Define your own error types