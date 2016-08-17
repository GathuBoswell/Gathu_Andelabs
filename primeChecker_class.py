class PrimeChecker(object):
    '''Class to check if a number is prime
       Implements method is_prime to check prime number
    '''
    def __init__(self, number = ""):
        self.number = number
  
    def is_prime(self):
        #try:
        if self.number == "":
            return False   
        elif len(self.number) > 0:
            """
            A try and except block to catch the 
            error when the input string cant be converted to integer
            """
            try:
                self.number = int(self.number)
                if self.number == 2:
                    return True
                elif not self.number & 1:
                    """
                    This steps checks for all even numbers
                    for x & y:
                    returns: Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0
                    eg: 2 & 2 returns - 2 or in bitwise - 10
                    """
                    return False
                for x in range(3, int(self.number**0.5) + 1, 2):
                    if self.number % x == 0:
                        return False
                return True               
            except ValueError:
                return 'given string cant be converted to Integer!!!'
                
    
g = PrimeChecker("101")
print(g.is_prime())
