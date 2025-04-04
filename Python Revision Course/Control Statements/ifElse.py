# If-Else statements are used for decision making. They allow your program 
#to execute different blocks of code based on conditions.

# Syntax

'''
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
'''

# Ex: Checking if a number is positive or negative

num = int(input("Enter a number: "))
if ((num%2) == 0):
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")
    

# We use elif for multiple conditions

num2 = int(input("Enter a number: "))

if (num2 > 0):
    print(f"The number {num2} is positive")
elif(num2 < 0):
    print(f"The number {num2} is negative")
else:
    print(f"The number {num2} is 0")
    

# Nested If-Else Statements
num3 = int(input("Enter a third number: "))

if num3 > 0:
    if num3 % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number or zero")
    

# Short-hand If-Else (Ternary Operator)
# Python allows you to write if-else statements in a single line
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)

# Boolean Conditions with If-Else
# Python treats values like 0, None, "" (empty string), and [] (empty list) as False.
name = ""

if name:
    print("Name is not empty")
else:
    print("Name is empty")
                            # Output: Name is empty
