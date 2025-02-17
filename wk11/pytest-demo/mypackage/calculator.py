def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    fac = 1
    for i in range(n,0,-1):
        fac=fac*i
    print(f'Factorial of {n} is {fac}')
    return fac

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def power(a,b):
    return a**b

def user_input():
    # Take input from the user
    usr_input = input("Enter one or two numbers separated by a space: ")

    result = -1
    # Split the input into a list
    inputs = usr_input.split()

    # If there's only one input
    if len(inputs) == 1:
        number1 = float(inputs[0])
        return number1
    # If there are two inputs
    elif len(inputs) == 2:
        number1 = float(inputs[0])
        number2 = float(inputs[1])
        return number1, number2
    else:
        raise ValueError("Invalid input. Please enter one or two numbers.")
  
    return result
