lst = [x for x in range(1,20)]
print(lst)
lst = list(map(lambda x:x+10, lst))
print(lst)


data = list(map(int,input().split()))
print(data)

data2 = map(int,'1 2 3 4 555 6'.split())

for e in data2:
    print(e)