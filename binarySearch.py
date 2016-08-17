def binarySearch(search_list, searched_item, start = 0, end = None):
    """Code to implement binary search"""
    if end == None:
        end = len(search_list)
        
    position = (( end - start )//2 + start)
    
    if search_list[position] != searched_item and (len(search_list) - 1 == position):
        return "Item not in the list"   
    elif search_list[position] == searched_item:
        return position      
    
    elif search_list[position] < searched_item:
        return binarySearch(search_list, searched_item, start = (position + 1), end = end)
    
    elif search_list[position ] > searched_item:
        return binarySearch(search_list, searched_item, start = start, end = position)    
    
search_list = [0,1,2,3,4,5,6,7,8,9,10,56,67]
searched_item = 1
print (binarySearch(search_list, searched_item))
    
