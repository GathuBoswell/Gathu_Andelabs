def find_missing(a,b):
    
    if len(a) == len (b): #check which list has the extra number
        return 0
    
    if len(a) > len(b):
        for item in a: ## if list a has the extra number
            if item in b:
                continue
            else:
                return item
    else: ## if list b has the extra number
        for item in b:
            if item in a:
                continue
            return item        
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6,75,67]

print(find_missing(a, b))