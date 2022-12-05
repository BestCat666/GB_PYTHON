#def sum(x, y):
#    return x + y

sum = lambda x, y: x + y   # это выражение равно функции выше!

def mult(x, y):
    return x * y

def math_2(op, a, b):
    print(op(a, b))
    #return op(a, b)

math_2(sum, 4, 7)
math_2(lambda x, y: x + y , 4, 7)   # можно записать сразу так
