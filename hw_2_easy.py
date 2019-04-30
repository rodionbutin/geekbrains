__author__ = "Butin R. A."


#easy1
sp = ["яблоко", "банан", "апельсин", "груша", "киви", "ананас"]

i = 1

maxi = 0

for elem in sp:
    print(str(i)+"." + elem.rjust(9))
    i += 1



#easy2
spisok1 = ["стол", "стул", "кресло", "тумбочка", "диван"]
spisok2 = ["кровать", "тумбочка", "комод", "стул"]

spisok1 = set(spisok1) - set(spisok2)

print(spisok1)



#easy3
spisok = [1, 95, 80, 63, -12, 2, 7]
print(spisok)

new_spisok = []

i = 0

for el in spisok :
    if el % 2 == 0:
        el = el / 4
        new_spisok.append(int(el))
    else:
        el = el * 2
        new_spisok.append(int(el))

print(new_spisok)

