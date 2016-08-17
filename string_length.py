def string_length(var):
    '''Function to return the length of a string or length of strings in a list
    takes as input either a string or a list
    '''
    length = []
    if type(var) == str: # check if argument is str if str return the length
        length.append(len(var))
        return length
    elif type(var) == list:# check if argument is list
        for item in var:
            length.append(len(item))
        return length
    
m = 'hfjhbhe'
k = ['fhfjkkf','ghfhjjkf','tyrhhj']

print(string_length(m))
print(string_length(k))