def dupli(listy):
    """Function to check consecutive dulicate items in a list"""
    if len(listy) == 0:
        return "List is Empty"
    else:
        temp = [listy[0]]
        for i in range(len(listy) - 1):
            if  temp[-1] == listy[i]:
                continue
            else:
                temp.append(listy[i])
        return temp
A = [1,1,2,3,3,3,3,34,4,5,6,5,7,7]
print(dupli(A))

            
        
        