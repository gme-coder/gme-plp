# basic calculator program  

# asking user to input two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# asking user to input the operation they want to perform
operation = input("Enter either (+, -, *, /) to show type of operation: ")

# performing the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':      
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':  
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

#print the result
print(f"{num1}{operation}{num2} = {result }")