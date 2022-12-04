## Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

import datetime 

def get_rand():
    return round((datetime.datetime.now().microsecond)**2 % 10 * (datetime.datetime.now().microsecond)) // 1000
n = get_rand()

print(int(n))



from time import time

def randfromtime(max):
    time1 = time()
    time1 = (time1 - int(time1))
    return int(time1 * max)

print(randfromtime(1000))

