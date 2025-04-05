#1. Program to find unique numbers in a list
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)

#2. Program to sum all numbers in a list
L = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L)
print ("Sum of all numbers sum() function:", ttl)

#3. Program to create a list of 5 random integers
import random                       # Import the random module
L3 = []
for i in range(5):
   x = random.randint(0, 100)       # .randint(a, b) is a function from Python's random module
                                    #that returns a random integer between two values.
   L3.append(x)
print (L3)