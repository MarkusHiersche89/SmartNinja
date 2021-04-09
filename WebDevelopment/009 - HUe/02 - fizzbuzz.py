'''
Hausaufgabe 9.2: FizzBuzz
Der Benutzer gibt eine Zahl zwischen 1 und 100 ein
Das FizzBuzz-Programm beginnt, bis zu dieser Nummer zu zählen (es druckt sie im Terminal aus).
Wenn die Zahl durch 3 teilbar ist, wird anstelle der Zahl "fizz" ausgegeben.
Wenn die Zahl durch 5 teilbar ist, wird "Buzz" ausgegeben.
Wenn es sowohl mit 3 als auch mit 5 teilbar ist, wird "fizzbuzz" gedruckt.
'''

eingabe = 99

eingabe = int(input("Zahl zwischen 1 und 100 eingeben: "))
for item in range(1, eingabe+1):
    if item % 5 == 0 and item % 3 == 0:
        print("fizzbuzz")
    elif item % 3 == 0:
        print("fizz")
    elif item % 5 == 0:
        print("buzz")
    else:
        print(str(item))