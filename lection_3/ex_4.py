'''
def select(f,col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x:(x, x**2), res)
print(res)

'''
path = 'E:/GB_PYTHON/lection_3/file.txt'
file = open(path, 'r')
data = file.read() + ' '
print(file.read())
file.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))

print(out)
