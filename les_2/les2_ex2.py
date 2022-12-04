#Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#Пример: Для N = 5: 1, -3, 9, -27, 81

print('Введите число')
num = int(input())

for i in range(0, num):
    print((-3)**i) 
'''

N = int(input('Введите значение N:'))
def sequence(n):
    for i in range(n):
        print((-3) ** i, end=' ')
sequence(N)
'''