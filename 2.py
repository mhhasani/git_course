n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
x = []
for i in range(n):
    x.append([])
    for j in range(m):
        x[i].append([])
for I in range(k):
    a, b, l = input().split()
    a = int(a)
    b = int(b)
    l = int(l)
    for i in range(a-1, l+a-1):
        for j in range(b-1, l+b-1):
            x[i][j].append(I+1)
my_list = []
for i in range(n):
    for j in range(m):
        my_list.append(x[i][j])
my_finallist = [i for j, i in enumerate(my_list) if i not in my_list[:j]]
res = 0
for i in list(my_finallist):
    if i == []:
        res += 1

print(len(list(my_finallist))-res)
