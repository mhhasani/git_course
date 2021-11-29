# from pprint import pprint
# from sys import getsizeof


# def f(*n):
#     total = 1
#     for i in n:
#         total *= i
#     return total


# x = 3
# y = [[1, 3], [13, 14], [4, 4], [15, 1], [99, 80], [4, 13]]
# print(id(y))
# print(2)
# for i in range(x):
#     print(i)
#     if i == 2:
#         break
# print(f(1, 4, 2, 6))
# s = "hello world"
# s = "H"
# # del y[0:3]


# def sort_item(item):
#     return item[1]


# y.sort(key=sort_item)
# # y = list(map(lambda x: x[1], list(filter(lambda x: x[1] % 2 == 0, y))))
# y = [item for item in y if item[0] % 2 == 0]
# print(y)
# print(s[0])

# x = [1, 13, 4, 15, 99, 4]
# y = [1, 13, 4, 15, 99, 3]

# d = zip(x, y)
# print(list(d))

# point = 1, 2, 3
# print(point)

# x = 12
# y = 13
# x, y = y, x
# print(x, y)

# set1 = {1, 2, 3, 4, 5, 5}
# set2 = {4, 8, 5, 2, 1, 0}
# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set1 ^ set2)
# x = {"x": 1, "y": 2}
# for key, value in x.items():
#     print(key, value)
# x = [1, 2, 3, 4, 5, 6, 4, 4, 5, 3, 3, 5, 3, 3, 4, 3, 4, 3, 4, 4, 3, 4]
# z = x.copy()
# for i in range(len(z)):
#     z.pop()
# print(z)
# print(x)
# z = [1, 2, 3, 4, 5, 6]
# w = [4, 6, 3, 5, 3]
# c = [[[*z, *w]], [1]]
# print(*c)
# first = {"x": 1, "y": 2}
# second = {"a": 12}
# third = {**first, **second}
# print(*first, *second, third)


# s = "This is a common interview question"
# res = {a: s.count(a) for a in s}
# pprint(sorted(res.items(), key=lambda x: x[1])[-1])


# try:
#     # file = open("2.py")
#     with open("2.py") as file:
#         print(f"{file.name} opened!")

#     age = int(input("age: "))
#     age = 10/age
# except (ZeroDivisionError, ValueError) as error:
#     print("please input an int")
#     print(error)
# else:
#     print("Ok!")
# # finally:
# #     file.close()


# def get_age(age):
#     age = int(input("age: "))
#     if age <= 0:
#         raise ValueError("age must be larger than 0")
#     return 10/age


# try:
#     print(get_age(0))
# except ValueError as error:
#     print(error)


class Point:
    class_name = 1

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


ali = Point("ali")
ali.class_name = "102"
mohsen = Point("mohsen")
Point.name = "unknown"
# print(isinstance(ali, Point))
ali.get_name()
print(mohsen.class_name)

# Write Python code here


class sampleclass:
    count = 0	 # class attribute
    name = "101 "

    @classmethod
    def change_name(cls, name):
        cls.name = name
        return cls()

    def increase(self):
        sampleclass.count += 1


# Calling increase() on an object
s1 = sampleclass()
s1.increase()
print(s1.count)

# Calling increase on one more
# object
s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)

print(s1.change_name("103").name)
print(s1.name, s2.name)


class Score:
    def __init__(self, math, physic):
        self.math = math
        self.physic = physic

    def __eq__(self, other):
        return self.math == other.math and self.physic == other.physic

    def __add__(self, other):
        return Score((self.math + other.math)/2, (self.physic + other.physic)/2)


a = Score(20, 19)
b = Score(18, 18)

print(a == b)
print((a + b).math, (a+b).physic)
