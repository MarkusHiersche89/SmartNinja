'''
Hausaufgabe 9.2: FizzBuzz
Der Benutzer gibt eine Zahl zwischen 1 und 100 ein
Das FizzBuzz-Programm beginnt, bis zu dieser Nummer zu zählen (es druckt sie im Terminal aus).
Wenn die Zahl durch 3 teilbar ist, wird anstelle der Zahl "fizz" ausgegeben.
Wenn die Zahl durch 5 teilbar ist, wird "Buzz" ausgegeben.
Wenn es sowohl mit 3 als auch mit 5 teilbar ist, wird "fizzbuzz" gedruckt.
'''

eingabe = 99

while 1 < eingabe < 100:
    eingabe = int(input("Zahl zwischen 1 und 100 eingeben: "))
    if eingabe % 5 == 0 and eingabe % 3 == 0:
        print("fizzbuzz")
    elif eingabe % 3 == 0:
        print("fizz")
    elif eingabe % 5 == 0:
        print("buzz")
    else:
        print(str(eingabe))