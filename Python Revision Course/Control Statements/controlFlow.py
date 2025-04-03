# Control flow in Python determines the order in which statements and instructions are
#executed in a program. It consists of three main components:

#1. Conditional statements (Decision Making): These are used to make decisions in a program. They include: 
#if, elif and else.

#2. Loops (Iteration): Allow repetitive execution of code.
#   - For loops: Used to iterate over a sequence (like a list, tuple, dictionary)
#   - While loops: Used to execute a block of code as long as a condition is true.
#   - Nested loops: Used to execute a block of code for each item in an iterable ( like a list, tuple, dictionary) and another iterable. 

# Some others are: 
#   - For-else statement: Used to execute a block of code when a for loop finishes normally (i.e., without encountering a break statement). 
#   - While-else statement: Used to execute a block of code when a while loop finishes normally (i.e., without encountering a break statement).   

#3. Loop Control Statements: Used to modify loop execution
#a. Break statement: Stops the loop
for i in range(5):
    if i == 3:
        break  # Stops at 3
    print(i)
# Output: 0, 1, 2

#b. Continue statement: Skips the current iteration
for i in range(5):
    if i == 2:
        continue  # Skips when i is 2
    print(i)
# Output: 0, 1, 3, 4

#c. Pass statement: Does nothing
for i in range(5):
    if i == 2:
        pass  # Does nothing
    print(i)
# Output: 0, 1, 2, 3, 4

#4. Exception Handling (Try-Except)
# Controls program flow when errors occur.
try:
    x = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Cannot divide by zero!")
