def Multiply(a,b) :
    print('Multiplication of ',a,b,a*b)
    
    result = Add(a,b)
    print("Calling Add Function",result)   
    
    return a*b
    

def Add(a,b):
    print('Addition of ',a, b,a+b)
    return a+b


mul = Multiply(5, 5)
add = Add(5, 5)


print(mul,add)