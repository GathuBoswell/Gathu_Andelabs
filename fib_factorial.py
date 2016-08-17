def iterative_factorial(n):
    fact = 1
    if n == 1 or n < 1:
        return 1
    
    for i in range(1, n+1):
        fact = fact * i  
    return fact

def recursive_factorial(n, prod=1):
    if n == 1 or n < 1:
        return (prod * 1)
    else:
        prod = (prod * n)
        return (recursive_factorial((n-1), prod))
    
    
print (recursive_factorial(5))
    