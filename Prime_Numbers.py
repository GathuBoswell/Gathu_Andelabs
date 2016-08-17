def manipulate_data(datastruct, data):
    if datastruct == "list":
        data.reverse()
        return (data)
    elif datastruct == "set":
        items = ["ANDELA", "TIA", "AFRICA"]
        for x in items:
            data.add(x)
        return (data)
    elif datastruct == "dictionary":
        return (data.keys())
    else:
        print("Data structure not recognized")
        
def prime_number(num):
    num = abs(int(num))
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True
        
        
m = [0,1,2,3,4,5,6,7,8,9,10]
n = {1,2,3,4,5}
o = {1:'one', 2:'two', 3:'three'}

print(manipulate_data("list", m))
print(manipulate_data("set", n))
print(manipulate_data("dictionary", o))

print(prime_number(7))