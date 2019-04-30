__author__ = "Butin R. A."


#normal1

x = [1, 1]

def fb (n, m):
    i = 2
    while i <= m:
        x.append(int(x[-1]) + int(x[-2]))
        i += 1
    return x[n-1 : m]
    
print(fb(1, 10))

