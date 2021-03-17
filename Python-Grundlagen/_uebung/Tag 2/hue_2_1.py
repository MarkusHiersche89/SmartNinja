"""

Exercise 2.1: Unit converter
Students can do this exercise in pairs.

Create a program that converts units. Specifically kilometers into miles.

First create a plan for this program.
Together with the instructor define the steps the user will take when using the program.

Plan:

The program greets user and describes what's the purpose of the program.
The program asks user to enter number of kilometers.
User enters the amount of kilometers.
The program converts these kilometers into miles and prints them.
The program asks user if s/he'd want to do another conversion.
If yes, repeat the above process (except the greeting).
If not, the program says goodbye and stops.
The program should constantly run as long as the user would want to do conversions.

When you finish, paste your code on GitHub Gist and share it on the SmartNinja forum.

=== === ===

Übung 2.1: Einheitenumrechner
Die Schüler können diese Übung paarweise durchführen.

Erstellen Sie ein Programm, das Einheiten konvertiert.
Speziell Kilometer in Meilen.

Erstellen Sie zunächst einen Plan für dieses Programm.
Definieren Sie zusammen mit dem Kursleiter die Schritte,
die der Benutzer bei der Verwendung des Programms ausführen wird.

Planen:

Das Programm begrüßt den Benutzer und beschreibt den Zweck des Programms.
Das Programm fordert den Benutzer auf, die Anzahl der Kilometer einzugeben.
Der Benutzer gibt die Anzahl der Kilometer ein.
Das Programm wandelt diese Kilometer in Meilen um und druckt sie aus.
Das Programm fragt den Benutzer, ob er eine weitere Konvertierung durchführen möchte.
Wenn ja, wiederholen Sie den obigen Vorgang (mit Ausnahme der Begrüßung).
Wenn nicht, verabschiedet sich das Programm und stoppt.
Das Programm sollte ständig ausgeführt werden, solange der Benutzer Konvertierungen durchführen möchte.

Wenn Sie fertig sind, fügen Sie Ihren Code in GitHub Gist ein und teilen Sie ihn im SmartNinja-Forum.

"""

print("*** Kilometer in Milen- Umrechner ***")

while True:
    # Eingabe:
    kilometer = float(input("\nKilometer: "))

    # Umrechnung:
    milen = kilometer * 0.621371

    # Ausgabe:
    print(str(kilometer) + " hat " + str(milen) + " Meilen.")

    # Nochmal umrechnen?:
    nochmal = input("\nNochmal? [y]/[n]: ")

    # wenn der User weder Y, y, N oder n eingegeben hat:
    while nochmal.lower() != "n" and nochmal.lower() != "y":
        print("\nBitte gültigen Wert eingeben!")
        nochmal = input("Nochmal? [y]/[n]")

    # Programmende:
    if(nochmal.lower() == "n"):
        print("\nProgramm wird beesndet")
        break