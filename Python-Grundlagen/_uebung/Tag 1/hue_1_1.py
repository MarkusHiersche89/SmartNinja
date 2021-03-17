"""
Homework 1.1: The mood checker
If there's enough time, student's can start working on the homework at this session already.

For the first exercise let's continue the mood checking program from before. Ask user to tell you what mood s/he is in:

if the mood is "happy", the program should print out "It is great to see you happy!"
if the mood is "nervous", respond with "Take a deep breath 3 times.". Use elif to enter more if statements:
elif mood == "nervous":.
Make up responses also for "sad", "excited" and "relaxed".
The last option should be the normal else, which responds with "I don't recognize this mood".

=== === ===

Hausaufgabe 1.1: Der Stimmungsprüfer
Wenn genügend Zeit vorhanden ist, können die Schüler bereits in dieser Sitzung mit den Hausaufgaben beginnen.

Für die erste Übung setzen wir das Stimmungsprüfungsprogramm von zuvor fort.
Bitten Sie den Benutzer, Ihnen mitzuteilen, in welcher Stimmung er sich befindet:

Wenn die Stimmung "glücklich" ist, sollte das Programm "Es ist schön, Sie glücklich zu sehen!" ausdrucken.
Wenn die Stimmung "nervös" ist, antworten Sie mit "Atmen Sie dreimal tief ein".
Verwenden Sie elif, um weitere if-Anweisungen einzugeben: elif Mood == "nervös":.
Machen Sie Antworten auch für "traurig", "aufgeregt" und "entspannt".
Die letzte Option sollte die normale Option sein, die mit "Ich erkenne diese Stimmung nicht" antwortet.

"""

print("*** Stimmungsprüfer ***")

mood = input("Wie ist Ihre Stimmung? ")

if mood == "glücklich":
    print("Es ist schön, Sie glücklich zu sehen!")
elif mood == "nervös":
    print("Atmen Sie dreimal tief ein")
elif mood == "traurig":
    print("Schade, dass du traurig bist")
elif mood == "aufgeregt":
    print("Interessant, dass du aufgeregt bist")
elif mood == "entspannt":
    print("Groovie...")
else:
    print("Ich erkenne diese Stimmung nicht")