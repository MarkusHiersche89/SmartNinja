
def hallo():
    a = 6
    print("Willkommen zu underem Taschenrechner (+,-,*,/)")

#if __name__ == "__main__":
#    hallo()

def plus_or(a, b):
    c = a + b
    print(c)

def minus(a, b):
    c = a - b
    return c

def plus(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Div. durch 0 nicht möglich")
        return 0
    else:
        return a / b

"""
erg = plus(1,5)
print(erg)
erg = minus(5,2)
print(erg)
plus(erg, 4)
"""
