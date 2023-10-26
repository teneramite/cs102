import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError('--Division by zero is not allowed--')
    return a / b

'''while True:
    a = float(input("Enter the first number>>"))
    op = input("Enter an operation to perform>>")   
    b = float(input("Enter the second number>>"))

    if op == "+":
        print(addition(a, b))
    elif op == "-":
        print(subtraction(a, b))
    elif op == "*":
        print(multiplication(a, b))
    elif op == "/":
        if b == 0:
            print("Division by zero is not allowed")
        else:
             print(division(a, b))     
            
    else:
        print("Error: operation is not available")'''

