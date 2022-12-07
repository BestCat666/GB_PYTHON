#Используем map
#1. В файле находится N натуральных чисел, записанных через пробел.
##Среди чисел не хватает одного, чтобы выполнялось условие
#A[i] - 1 = A[i-1]. Найдите это число.


file = open(r'E:\GB_PYTHON\les_5\file.txt', 'r')
res = file.read()
res1 = list(map(int, res.split()))   
print(res1)

for index in range(1, len(res1)):
    if (res1[index] - 1) != (res1[index-1]):
        print(res1[index] - 1)



# past_el = None

# with open('text.txt') as f:
#     for item in map(int, f.read().split( )):
#         if past_el is None:
#             past_el = item
#         else:
#             if item != past_el + 1:
#                 print(past_el + 1)
#             past_el = item
# 
'''               
with open("text.txt", "r") as f:
    lst = list(map(int, f.read().split()))

res = 0
for key, item in enumerate(lst):
    if key + 1 < len(lst) and item + 1 != lst[key + 1]:
        res = item + 1
    
print(res)

'''