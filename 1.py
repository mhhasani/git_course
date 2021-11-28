x = 3
y = [1, 2, 3, 4]
print(id(y))
for i in range(len(y)):
    print(x)
    print(id(y[i]))
for i in range(x):
    print(i)
    if i == 2:
        break
