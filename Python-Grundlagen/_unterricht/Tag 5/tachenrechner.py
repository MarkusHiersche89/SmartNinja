import funktionen as funk

#funk.hallo()
#from funktionen import hallo

def hallo_funk(name="Markus"):
    print(name)

if __name__ == "__main__":
    funk.hallo()
    hallo_funk()
    hallo_funk("Hirsch")

    zahl1 = int(input("1. Zahl eingeben:"))
    operant = input("Rechenart [x,-,*,/]: ")
    zahl2 = int(input("2. Zahl eingeben:"))

    if operant == "+":
        erg = funk.plus(zahl1, zahl2)
    elif operant == "-":
        erg = funk.minus(zahl1, zahl2)
    elif operant == "*":
        erg = funk.mult(zahl1, zahl2)
    elif operant == "/":
        erg = funk.div(zahl1, zahl2)
    else:
        print("\n=> ERROR: Falscher Befehl <=")
        erg = 0

    print("Ergebnis: " + str(erg))

    funk.plus(1,2)

