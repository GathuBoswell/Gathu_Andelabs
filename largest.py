### program to find from a list of integers, the largest.

def large_Num(listy):
    largest = listy[0]
    for i in listy:
        if i > largest:
            largest = i
        else:
            largest = largest
    return largest



m = [1,2,3,1010,4,5,6,7,8,99]
n = ["apples", "oranges", "mangoes", "banana", "zoo"]
largest = large_Num(m)
largest1  = large_Num(n)
print("The largest integer from the list {} is: {}".format(m, largest))
print("The largest integer from the list {} is: {}".format(n, largest1))

#import time
#def sumof2(n):
    #start =time.time()
    
    #theSum = 0
    #for i in range(1, 1+n):
        #theSum = theSum + i
        
    #end = time.time()
    
    #return theSum, end-start

#t, u = sumof2(1000)
#print('sum is {} required {} seconds '.format(t, u))
#for i in range(5):
    #print('sum is %d required %.30f seconds '%sumof2(1000))
