__author__ = "Butin R. A."

#normal1

import random
import math

list1 = [random.randint(-100,100) for _ in range (10)]
print(list1)

list2 = []

for el in list1:
    if el > 0:
        new_el = int(math.sqrt(el))
        if math.sqrt(el) == int(math.sqrt(el)):
            list2.append(new_el)
print(list2)



#normal2

date = "30.07.2017"

day = date[:2]
month = date[3:5]
year = date[6:]


months = {"01": "январь", "02": "февраль", "03": "март", "04": "апрель",
         "05": "май", "06": "июнь", "07": "июль", "08": "август",
         "09": "сентябрь", "10": "октябрь", "11": "ноябрь", "12": "декабрь"}

days = {"01": "первое", "02": "второе", "03": "третье", "04": "четвертое",
       "05": "пятое", "06": "шестое", "07": "седьмое", "08": "восьмое",
       "09": "девятое", "10": "десятое", "11": "одиннадцатое",
       "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое",
       "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое",
       "18": "восемнадцатое", "19": "девятнадцатое", "20": "двадцатое",
       "21": "двадцать первое", "22": "давдцать второе",
       "23": "двадцать третье", "24": "двадцать четвертое",
       "25": "двадцать пятое", "26": "двадцать шестое",
       "27": "двадцать седьмое", "28": "двадцать восьмое",
       "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"}


date1 = days[day] + " " + months[month] + " " + year + " года"
print(date1)



#normal3

import random

n = int(input("Введите кол-во: "))

list3 = [random.randint(-100,100) for _ in range (n)]
print(list3)



#normal4

import random

list4 = [random.randint(0,10) for _ in range (10)]
print(list4)

list5 = list(set(list4))
print(list5)

list6 = []
for elem in list4:
    if list4.count(elem) == 1:
        list6.append(elem)
print(list6)
