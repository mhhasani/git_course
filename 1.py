from pprint import pprint
from sys import getsizeof


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
# y = list(map(lambda x: x[1], list(filter(lambda x: x[1] % 2 == 0, y))))
y = [item for item in y if item[0] % 2 == 0]
print(y)
print(s[0])

x = [1, 13, 4, 15, 99, 4]
y = [1, 13, 4, 15, 99, 3]

d = zip(x, y)
print(list(d))

point = 1, 2, 3
print(point)

x = 12
y = 13
x, y = y, x
print(x, y)

set1 = {1, 2, 3, 4, 5, 5}
set2 = {4, 8, 5, 2, 1, 0}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)
x = {"x": 1, "y": 2}
for key, value in x.items():
    print(key, value)
x = [1, 2, 3, 4, 5, 6, 4, 4, 5, 3, 3, 5, 3, 3, 4, 3, 4, 3, 4, 4, 3, 4]
z = x.copy()
for i in range(len(z)):
    z.pop()
print(z)
print(x)
z = [1, 2, 3, 4, 5, 6]
w = [4, 6, 3, 5, 3]
c = [[[*z, *w]], [1]]
print(*c)
first = {"x": 1, "y": 2}
second = {"a": 12}
third = {**first, **second}
print(*first, *second, third)


s = "This is a common interview question"
res = {a: s.count(a) for a in s}
pprint(sorted(res.items(), key=lambda x: x[1])[-1])


try:
    age = int(input("age: "))
except ValueError as error:
    print("please input an int")
    print(error)
else:
    print("Ok!")
