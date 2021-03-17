"""

Homework 1.2: Guess the secret number
We have a first customer - a local Casino! They want to expand their business to computer gambling so they w
ant us to build a gambling game for them. For the beginning something small and simple - a
game called Guess the secret number.

Your task is to create this game:

First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.
Then the user has to find out what this number is (using input()). Store user's guess in a variable called guess.
Check if your secret is equal to user's guess.
If the user's guess is wrong, let him/her know that (use print() and if/else).
If the user's guess is correct, congratulate him/her.

=== === ===

Hausaufgabe 1.2: Errate die Geheimnummer
Wir haben einen ersten Kunden - ein lokales Casino! Sie möchten ihr Geschäft auf Computerspiele ausweiten,
damit wir ein Glücksspiel für sie entwickeln können.
Für den Anfang etwas Kleines und Einfaches - ein Spiel namens Guess the secret number.

Deine Aufgabe ist es, dieses Spiel zu erstellen:

Zuerst eine Zahl im Programm "fest codieren" (die Zahl in eine Variable schreiben).
Sie können diese Variable geheim nennen.
Dann muss der Benutzer herausfinden, was diese Nummer ist (mit input ()).
Speichern Sie die Vermutung des Benutzers in einer Variablen namens erraten.
Überprüfen Sie, ob Ihr Geheimnis der Vermutung des Benutzers entspricht.
Wenn die Vermutung des Benutzers falsch ist, teilen Sie ihm dies mit (verwenden Sie print () und if / else).
Wenn die Vermutung des Benutzers richtig ist, gratulieren Sie ihm.

"""

print("*** Geheimzugang ***")

geheim = 123

erraten = int(input("Ihre Zahl: "))

if erraten == geheim:
    print("Gratulation, Sie kennen wohl die Zahl.")
else:
    print("Falsche Zahl eingegeben")