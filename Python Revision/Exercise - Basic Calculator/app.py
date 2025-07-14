# This is a basic calculator that collects 3 inputs from the user: the first number, the second
# number, and the operator.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

if (operator == "+"):
    result = num1 + num2
    print("The addition of the two numbers is ", result)
    
elif (operator == "-"):
    result = num1 - num2
    print("The difference of the two numbers is ", result)

elif (operator == "/"):
    result = num1/num1
    print("The quotient is ", result)

elif (operator == "*"):
    result = num1*num2
    print("The product is ", result)
    
elif (operator == "%"):
    result = num1%num2
    print("The modulus is ", result)
    
else:
    print("Invalid operator")
