#[exp for item in iterable]
#[exp for item in iterable(if conditional)]
#[exp <if conditional> for item in iterable (if conditional)]

lst = [i for i in range(1,21) if i % 2 == 0]
print(lst)

lst2 = [(i,i) for i in range(1,21) if i % 2 == 0]   # получаем список кортежей [(2, 2), (4, 4), (6, 6), ....]
print(lst2)


def f(x):
    return x**3
lst3 = [f(i) for i in range(1,21) if i % 2 == 0]   # получаем список из i в кубе (только чётные)
print(lst3)
lst4 = [(i, f(i)) for i in range(1,21) if i % 2 == 0]   # получаем список из i + i в кубе (только чётные) кортеж
print(lst4)

