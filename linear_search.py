def linearSearch(list_searched, item_searched, i=0):
    """Linear serach code to return the first occurence of the item being checked for"""
    if len(list_searched) == 0:
        return "List is empty"
    
    last_item = len(list_searched) - 1
    
    if list_searched[i] == list_searched[last_item] and list_searched[i] != item_searched:
        return 'Item not in list'
    elif list_searched[i] != item_searched:
        i += 1
        return (linearSearch(list_searched, item_searched, i))
    
    elif list_searched[i] == item_searched:
            return i
        
l = [1,4,23,78,901,45,654,3456,654,654, 'wysla']
item = 'wysla'

print ("The item {} is at position {} of the list".format(item, linearSearch(l, item)))
            
        
    