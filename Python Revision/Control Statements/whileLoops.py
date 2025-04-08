# A while loop is used to execute a block of code repeatedly as 
#long as a condition remains true.

# Syntax:
'''
while condition:
    code to execute
'''

# The loop only stops running when the condition becomes false.

# Ex1:
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count to avoid infinite loop
# Output: 1, 2, 3, 4, 5


# We use the Break statement to immediately exit or stop a loop
num = 1
while num < 10:
    if num == 5:
        break  # Exit the loop when num reaches 5
    print(num)
    num += 1
# Output: 1, 2, 3, 4, 5


# We use the Continue statement to skip an iteration in a loop
num2 = 0
while num2 < 5:
    num2 += 1
    if num2 == 3:
        continue  # Skip number 3. That is, won't print 3.
    print(num2)
# Output: 1, 2, 4, 5


# Using an Else clause with While
# The else block runs when the  while condition becomes False, unless the loop
#is stopped with the break statement.
num3 = 1
while num3 < 4:
    print(num3)
    num3 += 1
else:
    print("Loop ended naturally")
# Output: 1, 2, 3, Loop ended naturally


# Infinite Loop (Be careful!)
# Here, if the condition never becomes False, the loop runs forever.
while True:
    print("This is an infinite loop!")
    break  # Use break to stop it
# Output: This is an infinite loop! (and then stops)