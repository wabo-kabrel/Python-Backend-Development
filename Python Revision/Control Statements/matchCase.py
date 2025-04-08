# The match-case statement in Python is similar to the switch-case in C.
#It allows you to compare values against multiple patterns and execute code
#based on which pattern matches.

# Syntax:

'''
match variable:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default case (like 'else')
'''

# Ex1: Simple Match
day = "Monday"

match day:
    case "Monday":                          # works like if
        print("Start of the week")
    case "Friday":                          # works like elif
        print("End of the work week")
    case _:
        print("Just another day")           # works like else

# Output: Start of the week

# Ex3: Matching Multiple Patterns
fruit = "apple"

match fruit:
    case "apple" | "banana":
        print("It's a common fruit")
    case "mango":
        print("It's a tropical fruit")
    case _:
        print("Unknown fruit")


# Ex4: Using match with conditions
num = 5

match num:
    case x if x < 0:
        print("Negative number")
    case x if x == 0:
        print("Zero")
    case x if x > 0:
        print("Positive number")


# Ex5: Matching Data Structures
person = ("John", 25)

match person:
    case ("John", age):
        print(f"John is {age} years old")
    case (_, _):
        print("Unknown person")

# Output: John is 25 years old.
