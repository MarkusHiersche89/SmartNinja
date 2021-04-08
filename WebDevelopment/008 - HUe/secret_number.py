'''
Hausaufgabe 8.2: Errate die Geheimnummer
Wir haben einen ersten Kunden - ein lokales Casino! Sie möchten ihr Geschäft auf Computerspiele ausweiten,
damit wir ein Glücksspiel für sie entwickeln können. Für den Anfang etwas Kleines und Einfaches -
ein Spiel namens Guess the secret number .

Deine Aufgabe ist es, dieses Spiel zu erstellen:

Zuerst eine Zahl im Programm "fest codieren" (die Zahl in eine Variable schreiben). Sie können diese
Variable aufrufen secret.
Dann muss der Benutzer herausfinden, was diese Nummer ist (mit input()). Speichern Sie die Vermutung
des Benutzers in einer Variablen namens guess.
Überprüfen Sie, ob Ihr secretBenutzer dem entspricht guess.
Wenn die Vermutung des Benutzers falsch ist, teilen Sie ihm dies mit (verwenden Sie print()und wenn / sonst).
Wenn die Vermutung des Benutzers richtig ist, gratulieren Sie ihm.
Wenn Sie fertig sind, laden Sie den Code auf GitHub hoch und teilen Sie den Link dazu auf SmartNinja Slack .
'''

import random

secret = random.randrange(1, 201)
print(str(secret))

finish = False

while not finish:
    zahl = int(input("Rate ein Zahl: "))
    if zahl > secret:
        print("zu gross")
    elif zahl < secret:
        print("zu klein")
    else:
        print("erraten")
        finish = True