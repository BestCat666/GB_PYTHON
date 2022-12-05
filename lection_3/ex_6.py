# это аналогично задаче 4 только с функцией map вместо select и filter вместо where

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)