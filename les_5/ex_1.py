lst = [1, 2, -3, 44, -76, 32, 1]
print(max(lst))

print(max([abs(x) for x in lst]))

print(max(map(abs, lst)))

print(max(lst, key = abs))

lst2 = [(1, 2), (6, 2), (4, 2), (6, 1)]
print(max(lst2, key = lambda x: x[1]))


lst3 = [2, 33, 12, 34, 56, 67]
a = list(filter(lambda x: x % 2 == 0, lst3)) # или not x % 2
print(a)
for index, x in enumerate(lst3):
    print(index, x)
print(list(enumerate(lst3)))

