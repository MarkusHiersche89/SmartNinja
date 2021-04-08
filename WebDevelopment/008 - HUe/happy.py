'''
Hausaufgabe 8.1: Der Stimmungsprüfer
Für die erste Übung setzen wir das Stimmungsprüfungsprogramm von zuvor fort. Bitten Sie den Benutzer,
Ihnen mitzuteilen, in welcher Stimmung er sich befindet:

Wenn die Stimmung "glücklich" ist, sollte das Programm ausgedruckt werden "It is great to see you happy!"
Wenn die Stimmung "nervös" ist, antworten Sie mit "Take a deep breath 3 times.". Verwenden Sie elif,
um weitere if-Anweisungen einzugeben : elif mood == "nervous":.
Machen Sie Antworten auch für "traurig", "aufgeregt" und "entspannt".
Die letzte Option sollte die normale sein else, die mit antwortet "I don't recognize this mood".
Wenn Sie fertig sind, laden Sie den Code auf GitHub hoch und teilen Sie den Link dazu auf SmartNinja Slack .
'''

stimmung = str(input("Deine Stimmung: "))
if (stimmung.lower() == "gluecklich"):
    print("It is great to see you happy!")
elif (stimmung.lower() == "nervoes"):
    print("Take a deep breath 3 times.")
elif (stimmung.lower() == "traurig"):
    print("Nimm nen Teddy zum kuscheln.")
elif (stimmung.lower() == "entspannt"):
    print("Behalte deine Stimmung bei.")
else:
    print("Du hast mir ne unbekannte Stimmung gesagt.")