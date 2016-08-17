def prime_number(num):
    """
    Function to check if a number 'num' is prime
    """
    num = abs(int(num))
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
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
print(prime_list_generator(10))
print(prime_number(6))

