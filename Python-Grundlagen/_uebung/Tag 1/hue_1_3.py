"""

Homework 1.3: Calculator
Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").

Then use if/elif/else statements to do the right operation. A hint:

if operation == "+":

=== === ===

Hausaufgabe 1.3: Rechner
Schreiben Sie ein Programm, das die grundlegenden arithmetischen Operationen ausführt:

Addition (+),
Subtraktion (-),
Multiplikation (*),
und Teilung (/).
Bitten Sie den Benutzer, zwei Zahlen und die arithemtische Operation ("+", "-", "*" oder "/") einzugeben.

Verwenden Sie dann die Anweisungen if / elif / else, um die richtige Operation auszuführen. Ein Hinweis:

if operation == "+":

"""

print("*** Rechner ***")

zahl_1 = float(input("1. Zahl: "))
zahl_2 = float(input("2. Zahl: "))
operator = input("Rechenoperation: ")

if operator == "+":
    print(str(zahl_1) + " + " + str(zahl_2) + " =  " + str(zahl_1+zahl_2))
elif operator == "-":
    print(str(zahl_1) + " - " + str(zahl_2) + " =  " + str(zahl_1-zahl_2))
elif operator == "*" or operator == "x":
    print(str(zahl_1) + " * " + str(zahl_2) + " =  " + str(zahl_1*zahl_2))
elif operator == "/" or operator == ":":
    if zahl_2 != 0.0:
        print(str(zahl_1) + " / " + str(zahl_2) + " =  " + str(zahl_1/zahl_2))
    else:
        print("Division durch 0 ist nicht möglich!")
elif operator == "%":       # <== Spaßfaktor, nicht Teil der Aufgabe ;-P
    print(str(zahl_1) + " % " + str(zahl_2) + " =  " + str(zahl_1 % zahl_2))
else:
    print("Unbekannte Rechenoperation")