def digitalSum(n, summ=0):
    """The digital sum of a number n is the sum of its digits. Write a recursive function digitalSum(n) 
    that takes a positive integer n and returns its digital sum. For example, digitalSum(2019) 
    should return 12 because 2+0+1+9=12."""
    
    if n < 10:
        summ += n
        return summ
    else:
        summ += (n % 10)
        #print ('the sum is:', summ)
        n = (n//10)
        return (digitalSum(n, summ))
    
def digitalRoot(n):
    """The digital root of a non-negative integer n is computed as follows. 
    Begin by summing the digits of n. The digits of the resulting number are then summed,
    and this process is continued until a single-digit number is obtained. 
    For example, the digital root of 2019 is 3 because 2+0+1+9=12 and 1+2=3. 
    Write a recursive function digitalRoot(n) which returns the digital root of n.
    """
    result = digitalSum(n)
    if result == 10 or result > 10 :
        return digitalRoot(digitalSum(result))
    else:
        return result
    
        
print (digitalRoot(99999999999199999999999))