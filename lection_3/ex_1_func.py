#def sum(x):
#    return x+10

#def mult(x):
#    return x**2

#print(sum(mult(2)))

def f(x):
    return x**2
g = f            #функция может быть положена в переменную!
print(type(f))
print(type(g))
print(f(4))
print(g(4))


def calc1(x):
    return x + 10
print(calc1(10))

def calc2(x):
    return x * 10
print(calc2(10))

def math_(operation, num):
    print(operation(num))   #operation - это функция 
math_(calc2, 10)            # кладём вместо аргумента название(без вызова) функции
math_(calc1, 10) 

# функции с 2 аргументами
def sum(x, y):
    return x + y

def mult(x, y):
    return x * y

def math_2(op, a, b):
    print(op(a, b))
    #return op(a, b)

math_2(mult, 4, 7)

