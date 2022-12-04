# Функция - это фрагмент программы, используемый многократно
#def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

#import lection1_function as h
#print(h.f(1))


#def new_string(symbol, count = 2):
# return symbol * count
#print(new_string('!', 5)) # !!!!!
#print(new_string('!')) # !!!
#print(new_string(4)) # 12


#def concatenatio(*params):
# res: str = ""
# for item in params:
#   res += item
# return res
#print(concatenatio('a', 's', 'd', 'w')) # asdw
#print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

def f(*args, dop_arg = 0):
 print(args, '|', dop_arg)

f(12, [33, '333'], False, dop_arg = 55)

def f(*args, **kwargs):
 print(args, '|', kwargs)

f(12, 33, 44, abc = 22, cde = 99)


