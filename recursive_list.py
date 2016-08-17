def sumRecursive_list(recur_list):
    total = 0
    for item in recur_list:
        if type(item) == type([]):
            total = total+ sumRecursive_list(item)
        else:
            total = total + item
            
    return total

####code to find largest element of a recursive list

def recursiveLargest(recur_list):
    largest = None
    first_time = True
    for item in recur_list:
        if type(item ) == type([]):
            val = recursiveLargest(item)
        else:
            val = item
        if first_time or val > largest:
            largest = val
            first_time = False
            
    return largest    

k = [1,2,3,4,5,6,7,8,9,1200]
m = [1,2,3,[4,5,6,[7,8],9],1000]

print("The sum of list {} is equal to: {} and the largest item in the list is:{} ".format(k, sumRecursive_list(k),recursiveLargest(k)))
print("The sum of list {} is equal to: {} and the largest item in the list is:{} ".format(m, sumRecursive_list(m),recursiveLargest(m)))
  
