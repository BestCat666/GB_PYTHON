##Задайте список. Напишите программу, которая определит, присутствует ли в  заданном списке строк некое число.
#['22', '33', '123', 'fwefe', 'ytyy', '55']
 
lst = ['22', '33', '123', 'fwefe', 'ytyy', '55']
num = (input('Введите число: '))
#print(type(lst))
#exit()
if num in lst:
    print(num)


'''
lst = ['22', '33', '123', 'fwefe', 'ytyy', '55']
num = (input('Введите число: '))
#print(type(lst))
#exit()
result = 'нет'
for i in lst:
    if num == i:
        result = 'данное число есть в списке'
        break
print(result)
'''