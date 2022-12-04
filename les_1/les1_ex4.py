#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#*Примеры:*
#- 6,78 -> 7
# - 5 -> нет



print('Введите а')
a = float(input())
print(round(a,1))

#####
numb = float(input('Введите число'))
num_new = numb*10%10
print(int(num_new))
######
n = float(input('введите число: '))
if n % 1 == 0:
    print('нет')
else:
    n1 = int(n % 1 * 10)
    print(n1)
#####
n = float(input())
if n != int(n):
    print(int(n*10%10))
else: 
    print("No")

