# .
#
# Session 1 | File 1
#
# Inhalt:
# => Variable
#   => Typen: int, String, float
#   => type()
# => Ausgabe
# => Eingabe
# => Kommentare
# => Konvertierung
# => Verzweigung (if, elif, else)
#
# Dev: Markus Hiersche
# Timestamp: 2020-04-16-18-20
#

"""
mehrzeiliger
Kommentar
"""

# einzeiliger Kommentar

x = 10
y = 21

print(x + y)

print(type(x))

string_1 = "Hallo"
string_2 = "Welt"

print(string_1 + " " + string_2 + "!")
print(string_1  + " " + str(y))

z = 2.0
print(type(z))
print(z)
v = int(z)
print(type(v))
print(v)

bool_true = True
bool_False = False
print(type(bool_true))
print(bool_true)

name = input("Dein Name: ")
print("Dein Name lautet: " + name)

zahl1 = int(input("1. Zahl: "))
zahl2 = int(input("2. Zahl: "))

if zahl1 == 15:
    print(zahl1 + " ist gleich 15")
elif zahl1 == 14:
    print(zahl1 + " ist gleich 14")
else:
    print("Zahl ungleich 14 o. 15")
