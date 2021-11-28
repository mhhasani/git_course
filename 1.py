def f(*n):
    total = 1
    for i in n:
        total *= i
    return total
x = 3
y = [1, 2, 3, 4, 5]
print(id(y))
print(2)
for i in range(x):
    print(i)
    if i == 2:
        break
print(f(1,4,2,6))
