# Bitwise Operators
# These operators are used to perform bitwise operations on integer-type objects.
# Python has 06 bitwise operators: 

#1. Bitwise AND: &
# E.g.
a = 60
b = 13
print("a: ", a, "b: ", b, "a&b: ", a&b)     # Output: a: 60, b: 13, a&b: 12
# When you use integers as the operands, both are converted in equivalent binary, 
#the & operation is done on corresponding bit from each number, starting from the 
#least significant bit and going towards most significant bit.
# The binary & works like the AND in a truth table. To understand how it works, convert 
#the values of a and b to binary, use the truth table AND, then convert the result from binary
#to decimal.
# You can get the binary values using the bin() function. E.g. 
print(bin(a))

#2. Bitwise OR: |

#3. Bitwise XOR: ^

#4. Bitwise NOT: ~
 
#6. Bitwise Left Shift Operator: >>
# Left shift operator shifts the most significant bits to right by the number 
# on the right side of the "<<" symbol. Hence, "x << 2" causes two bits of the 
# binary representation of to right. E.g.
a = 60
print ("a: ", a)
print("a<<2", a<<2)         # Output: a<<240
#5. Bitwise Left Shift Operator: <<

# 
#  All these operators # (except ~) are binary in nature, in the sense
#  they operate on two operands. Each operand is a binary digit (bit) 1 or 0.