#Напишите программу, которая принимает на вход два числа и 
#проверяет, является ли одно число квадратом другого


print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
if a**2 == b or b**2 == a:
    print('да')
else:
    print('нет')
