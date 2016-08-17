def selection_sort(items_list, sorted_list = []):
    """Sorts a list of items into ascending order using the
       selection sort algoright.
       """    
    for x in range(len(items_list)):
        smallest = items_list[0]
        for i in items_list:
            if i > smallest:
                smallest = smallest
            else:
                smallest = i
        items_list.remove(smallest)
        sorted_list.append(smallest) 
    return sorted_list
               

m  = [13,12,1,5,10,15,6,8,8,9,10,15,15,16,17,1,0]
k = [1]
i = []

print(selection_sort(m))
            