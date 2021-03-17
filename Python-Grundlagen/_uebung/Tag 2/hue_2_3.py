"""

Homework 2.3: Make string lowercase
Sometimes you'd like to make some string lowercase. For example, you have a string like this:

"Today Is A BeautiFul DAY"
And you'd like to make it like this:

"today is a beautiful day"
There is a very nice solution in Python to do this. Use Google search and find out how to do it.

Where would this come handy? For example if you ask user "Would you like to continue (yes/no)?", the user might respond: "yes", "Yes", "YES" or even "YeS". In this case, changing your user's response into lowercase letters would be very helpful in your if-else statement.

When you finish, paste your code on GitHub Gist and share it on the SmartNinja forum.

=== === ===


679/5000
Hausaufgabe 2.3: Zeichenfolge klein schreiben
Manchmal möchten Sie eine Zeichenfolge in Kleinbuchstaben schreiben. Zum Beispiel haben Sie eine Zeichenfolge wie folgt:

"Heute ist ein schöner Tag"
Und du möchtest es so machen:

"heute ist ein schöner Tag"
In Python gibt es dafür eine sehr schöne Lösung. Verwenden Sie die Google-Suche und finden Sie heraus, wie es geht.

Wo würde das nützlich sein? Wenn Sie beispielsweise den Benutzer fragen "Möchten Sie fortfahren (Ja / Nein)?", Antwortet der Benutzer möglicherweise: "Ja", "Ja", "JA" oder sogar "JA". In diesem Fall wäre es in Ihrer if-else-Anweisung sehr hilfreich, die Antwort Ihres Benutzers in Kleinbuchstaben zu ändern.

Wenn Sie fertig sind, fügen Sie Ihren Code in GitHub Gist ein und teilen Sie ihn im SmartNinja-Forum.

"""

text = "Today Is A BeautiFul DAY"
text_klein = text.lower()   # umwandeln in kleinen Text

print("Text large: " + text)
print("Text small: " + text_klein)