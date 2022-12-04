#Логические операции
#>, >=, <, <=, ==, !=
#not, and, or – не путать с &, |,^
#Кое-что ещё: is, is not, in, not in
a = 1<4
print(a)
a = 1<4 and 5>2
print(a)
a = 1 == 2
print(a)
a = 1 != 2
print(a)
a = 'qwe'
b = 'qwe'
print(a == b)
a = [1,2]
b = [1,2]
print(a == b)
a = 1<3<5
print(a)

f = 1>2 or 4<6 # True если хотя бы одно верно
print(f)
f = [1,2,3,4]
print(f)
print(2 in f) # 2 в списке
print(not 2 in f) # 2 в списке, поэтому false

is_odd = f[0] % 2 ==0
print(is_odd)

is_odd = not f[0] % 2 # получается 1 -- отрицание 1 это 0, 0 это fasle
print(is_odd)
