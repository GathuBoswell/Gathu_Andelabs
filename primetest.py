def prime_number(i):
    if i < 2:
        return False
    elif i in [2,3,5]:
        return True
    for x in [2,3,5]:
        if i % x == 0:
            return False
    return True
def prime_list_generator(m):
    """
    function to generate a list of prime numbers between zero and 'm'
    """
    primes = []
    for i in range(m+1):
        if prime_number(i):
            primes.append(i)
    return primes
#print(prime_list_generator(10))
    
print(prime_list_generator(501))
            