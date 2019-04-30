__author__ = "Butin R. A."


#easy1

import random

list1 = []
list2 = []


list1 = [random.randint(1,10) for _ in range (5)]
print(list1)

for elem in list1:
    new_elem = elem ** 2
    list2.append(new_elem)
print(list2)



#easy2

fruits1 = ["Яблоко", "Апельсин", "Банан", "Груша", "Арбуз"]
fruits2 = ["Банан", "Виоград", "Яблоко", "Манго", "Киви"]

common = [el for el in fruits1 if el == el in fruits2]
print(common)



#easy3

list3 = [random.randint(-20,20) for _ in range (10)]
print(list3)

new_list = [elem for elem in list3 if elem % 3 == 0 and elem > 0 and elem % 4 != 0]
print(new_list)

