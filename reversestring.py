def reverse_string(string):
    '''
    function to return the reverse of a string
    returns the reverse or;
    True when the string is an palindromes
    '''
    return_string=''
    
    if any(string) == False: #check if the srting is empty
        return None
    
    for i in range(1, len(string) + 1): # iterate over the string characters
        return_string += string[-i] # append each char from the rear of string to another string
    if return_string == string:# check if the string and the returned string match if True returns True
        return True
    else:
        return return_string
print(reverse_string(''))