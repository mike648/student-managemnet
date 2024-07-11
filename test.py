# f = open('scratch.txt', 'a')
# (f.write("Hello\n"))
# f.close()

# Prime number in a interval
# class Test:


# def primeFun(start, end):
#
#     for num in range(start, end+1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 print(num)
# primeFun(1, 20)


arr = [1, 2, 3, 5]
ar = []
for i in range(1, 6):
    ar.append(i)

for i in arr:
    for j in ar:
        if i == j:
            break
    else:
        print(i)















#Biggest
# class Biggest:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def big(self):
#         if self.a > self.b and self.a > self.c:
#             print(f"{self.a} is biggest")
#         elif self.b > self.c:
#             print(f"{self.b} is biggest")
#         else:
#             print(f"{self.c} is biggest")
#
# b1 = Biggest(1, 2, 3)
# b1.big()
# b2 = Biggest(23, 44, 56)
# b2.big()

# class Base:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return self.r
#
# class Circle(Base):
#     def area(self):
#         return (4*3.14*self.r**3)/3
# class Tri(Base):
#     def area(self):
#         return 3.14*self.r**2

# t1 = Tri(5)
# res = t1.area()
# print(res)
# c1 = Circle(3)
# res2 = c1.area()
# print(res2)
























