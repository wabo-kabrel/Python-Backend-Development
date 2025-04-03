# In Python, operator precedence determines the order in which operators are evaluated
#in an expression. When an expression contains multiple operators, Python follows a 
#predefined set of rules to decide which operator should be applied first. This ensures 
#that expressions are evaluated consistently and avoids ambiguity.

# Operator Precedence Table
# Search online or ask chat gpt.

# Some Key Points About Operator Precedence
#1. Python follows BODMAS

#2. Exponential ( ** ) is Right-Associative
# Unlike most other operators, exponential groups from right to left.
result = 2 ** 3 ** 2        # Equivalent to 2 ** (3 ** 2)
print(result)               # Output: 512

#3. Chained Comparisons:
# Python allows chaining comparisons (e.g., a < b < c), which are evaluated
#as a < b and b < c.

result2 = 1 < 2 < 3
print(result2)  # Output: True