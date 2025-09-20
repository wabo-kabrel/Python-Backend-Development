

# The input() Function
'''The input() function is used to take input from the user via the command line or terminal. It reads the input as a string (even if the user enters numbers), so additional processing may be required for non-string inputs.'''

# Syntax:
'''variable = input(prompt)'''
#Ex:
name = input("Enter your name: ")   # Output: Enter your name
print(f"Hello, {name}!")            # Output: Hello {name}

# Since input() always return a string, you need to explicitly convert the input
# to other data types (e.g. integers, float, etc) if needed.
# Ex: 
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Boolean Input
'''For boolean input, we need to interpret specific strings (e.g. "yes", "no") as True or False'''
# Ex:
response = input("Do you like Python? (yes or no): ").lower() # .lower converts everything to lower
#case letters in case the user enters a response like Yes.
likes_python = response == "yes"
dislike_python = response == "no"
print(f"Likes Python: {response}")

# Validating user input
'''It's important to validate user input to ensure it meets the expected format or constraints. E.g. you
might want to check if the user entered a valid number or a value within a specific range'''
#E.g.
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
             print("Age cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"You are {age} years old.")

# Multi-line Input
'''If you need to accept multiple lines of input, you can use a loop or read input until a specific condition is met (e.g., an empty line).'''
# Ex:
print("Enter your text (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)