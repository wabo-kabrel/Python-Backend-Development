#Assigning Variables
counter = 100       #integer variable
miles = 1000.0      #float variable
name = "John Doe"   #string variable

print(counter); print(miles); print(name)       #print variables

print(type(counter)); print(type(miles)); print(type(name))     #print variable types

# Deleting Variables
del counter #deletes the variable counter. Printing counter now will raise an error


# Casting Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print ("x = ", x)
print ("y = ", y)
print ("z = ", z)

# Multiple Variable Assignment
a = b = c = 1       # Instead of writing 03 different lines of a=1; b=1; c=1; we can write a=b=c=1
print(a, b, c)      # Instead of writing 03 different lines of print(a); print(b); print(c); we can write print(a,b,c)

# Assigning Multiple Values to Multiple Variables
num, score, greetings = 1, 2.5, "Hello"

print(num)
print(score)
print(greetings)

# Valid Variable Naming Convention
counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000

print (counter, _count, name1, name2, Age, zara_salary)

# Local Variables
def sum():
    sum = (x+y)
    return sum

print(sum(5+10))

# Global Variables
x = 5
y = 10
def sum():
    print(x + y)
    return sum

print(sum())

# Constants
PI = 3.14       #Python doesn't have any formally defined constants, However you can indicate a variable to be treated as a constant by using all-caps names with underscores(for constant names with more than one word)
print(PI)