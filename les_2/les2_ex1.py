#lst = []
#print(dir(lst))

lst = []
 
 
def add_to_lst(item):
    if isinstance(item, int):
        lst.append(item)
 
 
add_to_lst(66)
add_to_lst('ww')
add_to_lst(65.5)
add_to_lst(2)
add_to_lst(None)
print(lst)


