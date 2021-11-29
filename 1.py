def f(*n):
    total = 1
    for i in n:
        total *= i
    return total


x = 3
y = [[1, 3], [13, 14], [4, 4], [15, 1], [99, 80], [4, 13]]
print(id(y))
print(2)
for i in range(x):
    print(i)
    if i == 2:
        break
print(f(1, 4, 2, 6))
s = "hello world"
s = "H"
# del y[0:3]


def sort_item(item):
    return item[1]


y.sort(key=sort_item)
y = list(map(lambda x: x[1], filter(lambda x: x % 2 == 0)))
print(y)
print(s[0])
