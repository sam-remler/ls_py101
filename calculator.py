# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import sys

print('Welcome to Calculator!')
operation = sys.argv[1]
number1 = sys.argv[2]
number2 = sys.argv[3]

if operation == 'add':
    output = int(number1) + int(number2)
elif operation == 'subtract':
    output = int(number1) - int(number2)
elif operation == 'multiply':
    output = int(number1) * int(number2)
elif operation == 'divide':
    output = int(number1) / int(number2)
else:
    raise TypeError("Not a valid operation; should be add, subtract, multiply, divide")

print(f"The result is: {output}")