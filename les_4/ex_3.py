#2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# С помощью математических формул нахождения корней квадратного уравнения
##solve(a, b, c)                                                                                                                                                                                                                                                                                                                                                        
def solve(a, b, c):
    flag = False
    x1 = 0
    x2 = 0
    d = b ** 2 - (4 * a * c)
    if d > 0:
        flag = True
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
    elif d == 0:
        x1 = -b  / (2 * a)
    else:
        x1 = "Нет корней"
    if flag:
        return (x1, x2)
    return x1
