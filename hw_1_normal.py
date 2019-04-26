__author__ = "Butin R. A."

#normal1
x = input("Введите число: ")
a = 0

for b in x:
    if int(b) > a:        
        a = int(b)
print(a)

#normal1_1
y = input("Введите число: ")

maxi = 0
n = 0
c = 0

while n < len(y):
    c = int(y[n])
    if c > maxi:
        maxi = c
    n += 1

print(maxi)



#normal2
a = int(input("a: "))
b = int(input("b: "))
a =  a + b
b = a - b
a = a - b
print("a = ", a)
print("b = ", b)




#normal3
import math
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
x = int(input("Введите x: "))

yr = a * x ** 2 + b * x + c
k = math.sqrt(yr)
print("Корень уравнения: ", k)


