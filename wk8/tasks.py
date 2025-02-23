# Factorial
# Use numbers [1,2,3,4,5]

# Output the factorials of each element

data = [1,2,3,4,5]

def factorial(n):
    fac = 1
    for i in range(n,0,-1):
        fac=fac*i
    print(f'Factorial of {n} is {fac}')
    return fac

# factorial_data = [factorial(x) for x in data] 

factorial_data = [1 if n == 0 else (f := 1, [f := f * i for i in range(1, n + 1)], f)[-1] for n in data]

# [-1] last element
# f:= assign and use an expression
 
print(factorial_data)
    
# factorial(1)
# factorial(2)
# factorial(3)
# factorial(4)
# factorial(5)
