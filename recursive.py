def recursiveup(n, k=0):
    """Function to print up to a given number recursively
       eg. recursiveup(6) prints
       0,1,2,3,4,5,6 
    """
    if (k == n):
        print(k)
        print('hello world')
    else:
        print(k)
        recursiveup(n, k+1)
        
def recursivedown(n):
    """Function to print down to a given number recursively
       eg. recursiveup(6) prints
       6,5,4,3,2,1,0
    """    
    if (n == 0):
        print('hello world')
    else:
        print(n)
        recursivedown(n-1)
       
        

recursiveup(6)