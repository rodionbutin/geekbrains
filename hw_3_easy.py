__author__ = "Butin R. A."

#easy1

def my_round(x, k):
    a = float(str(x)[:len(str(int(x))) + 1 + k])
    print("a", a)
    b = int(str(x)[len(str(int(x))) + 1 + k: ])
    print("b", b)

    if b > int('5' * len(str(b))):
        a += 1 / 10 ** k
    return a

print(my_round(98.879355959, 5))



#easy2

def lucky_ticket(ticket):
    ticket = str(ticket)
    sum_1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum_2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if sum_1 == sum_2:
        return "lucky"
    else:
        return "not lucky"
    
print(lucky_ticket(123015))
