__author__ = "Butin R. A."


#не получилось вынести данные фигур отдельно. Все время были ошибки.

#easy1

import math

class Triangle:

    x1 = 3
    y1 = 4

    x2 = 5
    y2 = 5

    x3 = 6
    y3 = 2

    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
    c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)

    pP = (a + b + c) / 2

   
    def S(self):

        x1 = 3
        y1 = 4

        x2 = 5
        y2 = 5

        x3 = 6
        y3 = 2

        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
        c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)

        pP = (a + b + c) / 2

        square = (pP * ( pP - a) * (pP - b) * (pP - c)) ** 0.5
        print("Площадь:", square)

    def h(self):
        
        x1 = 3
        y1 = 4

        x2 = 5
        y2 = 5

        x3 = 6
        y3 = 2

        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
        c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)

        pP = (a + b + c) / 2
        
        Ha = (2 * math.sqrt(pP * (pP - a) * (pP - b) * (pP - c))) / a
        Hb = (2 * math.sqrt(pP * (pP - a) * (pP - b) * (pP - c))) / b
        Hc = (2 * math.sqrt(pP * (pP - a) * (pP - b) * (pP - c))) / c
        print("Высота", "\nОт первой стороны: ", Ha, "\nОт второй стороны: ", Hb, "\nОт второй стороны: ", Hc)

    def P(self):

        
        x1 = 3
        y1 = 4

        x2 = 5
        y2 = 5

        x3 = 6
        y3 = 2

        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
        c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)

        
        perimetr = a + b + c
        print("Периметр:", perimetr)

qwe = Triangle()
qwe.S()
qwe.h()
qwe.P()



#easy2

class Trapezium():
    
    x1 = 1
    y1 = 1

    x2 = 2
    y2 = 5

    x3 = 6
    y3 = 5

    x4 = 7
    y4 = 1


    def proverka(self):
        

        x1 = 1
        y1 = 1

        x2 = 2
        y2 = 5

        x3 = 6
        y3 = 5

        x4 = 7
        y4 = 1
        
        c = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        d = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
  
        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")
    
    def side(self):
        
        x1 = 1
        y1 = 1

        x2 = 2
        y2 = 5

        x3 = 6
        y3 = 5

        x4 = 7
        y4 = 1
        
        c = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        d = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
        a = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
        b = math.sqrt(((x4 - x1) ** 2) + ((y4 - y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDA: ", b)
        
    def perimeter(self):
                
        x1 = 1
        y1 = 1

        x2 = 2
        y2 = 5

        x3 = 6
        y3 = 5

        x4 = 7
        y4 = 1
        
        c = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        d = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
        a = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
        b = math.sqrt(((x4 - x1) ** 2) + ((y4 - y1) ** 2))
        
        P = a+b+c+d
        print("Периметр:", P)   

    def area(self):
                
        x1 = 1
        y1 = 1

        x2 = 2
        y2 = 5

        x3 = 6
        y3 = 5

        x4 = 7
        y4 = 1
        
        c = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        d = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
        a = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
        b = math.sqrt(((x4 - x1) ** 2) + ((y4 - y1) ** 2))
        
        S = ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))
        print("Площадь:", S, "\n")


asd = Trapezium()
asd.proverka()
asd.side()
asd.perimeter()
asd.area()



