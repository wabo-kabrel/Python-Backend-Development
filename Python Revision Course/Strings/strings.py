# A string is a sequence of  characters enclosed in quotes
text = "Hello world!"
name = 'Kabrel'


# Python supports:
# - Single quotes: 'Hello world!'
# - Double quotes: "Hello"
# - Triple quotes: ''' OR """ for multiline strings

paragraph = """This is a
multiline string"""


# String Indexing
# Each character in a string has an index (starting from 0):
greet = "hello"
print(greet[0])  # h
print(greet[4])  # o

# Negative Indexing
print(greet[-1])  # o
print(greet[-2])  # l


# String Slicing
# You can extract parts of a string:
message = "Hello, world!"
print(message[0:5])   # Hello
print(message[7:])    # world!
print(message[:5])    # Hello
print(message[-6:-1]) # world       # Format: string[start:stop:step]



# Common String Methods
# - upper():    	    Converts to uppercase
# - lower():    	    Converts to lowercase
# - capitalize():    	Capitalizes first character
# - title():        	Capitalizes first letter of each word
# - strip():        	Removes whitespace
# - replace(a, b):  	Replaces substring a with b
# - find():         	Returns index of first match
# - split():        	Splits string into a list
# - join():         	Joins elements of a list with a string

text = "  hello Python  "
print(text.strip())       # 'hello Python'
print(text.upper())       # '  HELLO PYTHON  '
print(text.replace("Python", "World"))  # '  hello World  '

words = "one,two,three".split(",")
print(words)  # ['one', 'two', 'three']

joined = "-".join(words)
print(joined)  # one-two-three



# String Concatenation
#1. Concatenation:
first = "John"
last = "Doe"
full = first + " " + last
print(full)  # John Doe

#2. Repetition:
laugh = "ha" * 3
print(laugh)  # hahaha



# String Formatting
#1. f-Strings (recommended in Python 3.6+)
name = "John"
age = 21
print(f"My name is {name} and I am {age} years old.")

#2. .format() method
print("My name is {} and I am {} years old.".format(name, age))

#3. % formatting (older style)
print("My name is %s and I am %d years old." % (name, age))


# NB: Strings are immutable. Once created, cannot be changed.
text = "hello"
# text[0] = 'H'  ❌ Error: strings are immutable



# Checking Content
s = "Python3"

print(s.isalpha())   # False (because of the number)
print(s.isdigit())   # False
print(s.isalnum())   # True
print(s.startswith("Py"))  # True
print(s.endswith("3"))     # True



# Looping Strings
for char in "hello":
    print(char)



# Escape Characters 
# \n       	New line
# \t        Tab
# \\       	Backslash
# \'        Single quote
# \"  	    Double quote

print("Hello\nWorld")     # Line break
print("I\'m learning Python")  # I'm learning Python
