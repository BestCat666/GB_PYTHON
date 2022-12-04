#1. Задайте строку из набора чисел. Напишите программу,которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

#lst = list(map(str, input('Введите элементы массива через пробел: ').split()))
#print(lst)
str_ = '43 25 56 54 121'.split()
for index in range(len(str_)):
    str_[index] = int(str_[index])

print(max(str_),min(str_), sep = ' ')


##lst = [int(item) for item in "14 55 66".split(" ")]
#print(f"max: {max(lst)} min: {min(lst)}")


