 
# Zusammenfassung

## Vorwort

Der Quellcode ist während dem Kurs "Python" von SmartNinja entstanden.<br/>
Kursstart: 16.04.2020.<br/>
SmartNinja [Webseite](https://www.smartninja.org/)<br/>
Die Pythondateien sind in den Ordnern "_uebung" und "_unterricht" aufgeteilt.<br/>
<br/>
Zusatz: Dies ist kein Lehrmaterial von SmartNinja, sondern zusammengeschrieben von mir.

## Inhaltsangabe
[Kommentare | einzeilige u. mehrzeilige](#Kommentare)<br/>
[Variable | Deklaration und Initalisierung](#Variable)<br/>
[Ausgabe | print()](#Ausgabe)<br/>
[Escape-Zeichen](#Escape)<br/>
[Konvertierung | int(), str(), ...](#Konvertierung)<br/>
[Eingabe | input()](#Eingabe)<br/>
[Verzweigung | if, elif, else](#Verzweigung)<br/>
[Schleife | while()](#While-Schleife)<br/>
[Zähl-Schleife | for()](#For-Schleife)<br/>
[Schleife abbrechen | break](#break)<br/>
[Schleifen-Durchlauf abbrechen (Schleife unterbrechen) | continue](#continue)<br/>
[Zufallszahlen | random()](#random)<br/>
[Sting formatieren mit upper() und lower()](#string.upper_string.lower)<br/>
[Listen](#list)<br/>
[String zerteilen mit split()](#string.split)<br/>
[CSV-Dateien lesen und schreiben](#csv_lesen_schreiben)<br/>

## Tag 1 - 16.04.2020

### <a name="Kommentare"></a>Kommentare

Kommentare sind für die Entwickler, um sich Notizen zum Code zu machen. Diese werden vom Interpreter (beim ausführen) ignoriert.
Zum Testen wird auch manchmal eine Codezeile oder ein ganzer Block auskommentiert. Der Vorteil ist, dass der Code an Ort und Stelle stehen bleiben kann und nicht ausgeschnitten werden muss, sondern nur auskommentiert wird.

Einzeilige Kommentare:
```python
# Das ist ein Kommentar
...
x = 2 # Hier wird eine Variable angelegt und zugewiesen
```

Mehrzeilige Kommentare:
```python
"""
Hier steht ein
etwas längerer
Text
"""
```

### <a name="Variable"></a>Variable & Typen

Folgende Typen gibt es:
| Englisch | Deutsch | Beispiel |
|---|---|---|
| Integer | Ganze Zahl | 3 |
| Float | Kommazahl | 10.2 |
| String | Zeichenkette | "Ich liebe meine 4 Kinder und den Burschen!" |
| Boolean | Wahrheitswert | True oder False |
| List | Liste | ["Hy", 2, 7.4, False, 'a']

Deklarieren und Initalisieren:
```python
x = 3	# x  -> deklarieren/anlegen
	# =3 -> initalisieren/zuweisen

vorname = "Markus"

maennlich = True

gewicht = 78.3
```

### <a name="Ausgabe"></a>Ausgabe

Um auf der Konsole (unter Windows CMD/CommandLine und unter Linux Terminal/Shell genannt) Text auszugeben wird der Befehl print() benötigt.

```python
name = "Max"
print("Hallo " + name + "!")
```

### <a name="Escape"></a>Escape-Zeichen

Escape-Zeichen werden benötigt um bei Ausgaben formatiertungen vorzunehmen.

| Zeichen | Bedeutung |
|---|---|
| \n | neue Zeile |
| \t | horizontaler Tabulator |
| \v | vertikaler Tabulator |
| \a | Ton ausgabe |
| \\\ | Backslash |
| \\\" | Doppeltes Anfürungszeichen |

```python
print("Die Rechnung \"7 * 7\" ergibt 49.")
print("Dies ist eine mehrzeilige\nAusgabe zwecks Formatierung.")

# Ausgaben:
#   Die Rechnung "7 * 7" ergibt 49.
#   Dies ist eine mehrzeilige
#   Ausgabe zwecks Formatierung.
```

### <a name="Konvertierung"></a>Konvertierung

Um einen Typ von einer Variable (Wert) zu ändern ist es nötig diesen zu Konvertieren.

```python
x = 3
x_als_text = str(x)
x_als_float = float(x)

text = 123
zahl = int(123)

# In der Ausgabe eine Berechnung und somit auch eine Konvertierung in einem String:
zahl_1 = 5
zahl_2 = 3
print(zahl_1 + " + " + zahl_2 + " = " + str(zahl_1 + zahl_2))
# Ausgabe: 5 + 3 = 8
```

### <a name="Eingabe"></a>Eingabe

Natürlich soll auch der Benutzer Eingaben machen können.

Bei der Funktion "input()", kann in der Klammer angegeben werden, was unmittelbar vor der Eingabe stehen soll.
Die Funktion/methode input() fragt standardmäßig nach einem String ab.
Diesen kann man in jeden beliebigen Datentyp konvertieren.

```python
# Bei String-Eingaben:
name = input("Ihr Name: ")

# Bei Int-Eingabe:
alter = int(input("Ihr Alter: "))

# ...
```

### <a name="Verzweigung"></a>Verzweigung

Etwas häufiger werden Verzeigungen benötigt.
Bsp.: Wenn ich müde bin, dann gehe ich schlafen.

Vergleichsoperatoren:
| Schreibweise | gesprochen |
|---|---|
| < | kleiner |
| <= | kleiner gleich |
| == | gleich |
| != | ungleich |
| >= | größer gleich |
| > | größer |

Boolsche Operatoren:
| Schreibweise | gesprochen |
|---|---|
| and | und |
| or | oder |
| is | gleiches Objekt |
| is not | ungleiches Objekt |
| not | nicht |
 
```python
secret = 1234
eingabe = int(input("Raten Sie eine Zahl: "))

if eingabe < secret :
  print("Ihre Eingabe war zu klein")
elif eingabe == secret :
  print("Perfekt! Erraten.")
else:
  print("Ihre Eingabe war zu groß")

hunger = True
bin_daheim = False

if hunger == True and bin_daheim == True:
  print("Gehe bitte zum Kühlschrenk")
elif hunger == True and bin_daheim == False:
  print("Hole dir was vom Supermarkt")
else:
  print("Kein Handlungsbedarf")
```

## Tag 2 - 20.04.2020

### <a name="While-Schleife"></a>While-Schleife

Die While-Schleife kommt dann Beispielsweise zum Einsatz, um den User zu zwingen einen gültigen Wert einzugeben.
Wenn hierbei der User eine falsche Eingabe macht, bleibt dieser in der Schleife gefangen.

```python
eingabe = ""
while eingabe != "y" and eingabe != "n":
    eingabe = input("Bitte um Ihre Eingabe mit [y]/[n]: ")
    if eingabe == "y" :
        print("Sie haben sich für \"[Y]es\" entschieden.")
        # plus weiterer Code
    elif eingabe == "n":
        print("Sie haben sich für \"[N]o\" entschieden")
        # plus weiterer Code
    else:
        print("Bitte [y] oder [n] eingeben!")
print("Programm beendet")
```
### <a name="For-Schleife"></a>For-Schleife

Die For-Schleife wird in der Regel immer dann genommen, wenn eine Liste oder Zahlen durchgegangen werden soll.

Beispiel 1: Sie wollen die Zahlen von 0 bis 20 ausgeben, jedoch nur die gerade Zahlen

mit "%" (Modulo) kann man den Rest einer Division abfragen.
Rechenbeispiel: 10 / 3 = 3 und 1 Rest (somit ist 10 % 3 gleich 1)

```python
for i in range(20):     # Zahler i wird mit 0 deklariert
                        # Range: Bis wohin die schleife gehen soll
                        # Am Ende von jedem Durchlauf wird "i" um 1 erhöht
    if i % 2 == 0:
        print(i)
```

beispiel 2: Es sollen die zahlen von 10 bis 20 ausgegeben werden
```python
for i in range(10, 20):
    print(i)
```

Beispiel 3: Es sollen Zahlen von 10 bis 40 ausgegeben werden, jedoch nur jede 3. zahl
```python
for i in range(10, 40, 3):
    print(i)
```

### <a name="break"></a>Schleife abbrechen mit break

Angenommen man hat eine While-Schleife und die Zahl wird erraten, dann soll die Schleife beendet werden.

```python
geheim = 1234

while True:
    eingabe = int(input("Zahl: "))
    if eingabe < geheim :
        print("Ihre Eingabe war zu klein")
    elif eingabe == geheim :
        print("Perfekt! Erraten!")
        break
    else:
        print("Ihre Eingabe war zu groß")
```

### <a name="continue"></a>Schleifen-Durchlauf abbrechen (Schleife unterbrechen) mit continue

Wenn die Schleife nicht abgebrochen werden soll (als ganzes), sondern nur der jetzige eine Durchlauf, dann kommt continue() dran.

Beispiel: Es soll bis 30 gezählt werden, jedoch sollen nur die Zahlen welche NICHT durch 3 Teilbar sind ausgegeben werden.
```python
for i in range(30):
    if i % 3 == 0 :
        continue
    print(i)
```

### <a name="random"></a>Zufallszahlen mit random generieren

Um Spiele beispielsweise kniffliger zu gesalten, werden Zufallszahlen benötigt.

Beispiel 1: Zahlenraten zwischen 0 und 100
```python
import random       # Bibliothek einbinden

secret = random.randint(0, 100)     # Zufallszahl zwischen 0 und 100 generieren
zaehler = 0

while True:
    zaehler += 1
    eingabe = int(input("Deine Zahl: "))
    if eingabe < secret :
        print("Deine Zahl war zu klein")
    elif eingabe == secret :
        print("Perfekt! Du hast " + str(zaehler) + " Versuche gebraucht.")
        break
    else:
        print("Deine Zahl war zu groß")
```

### <a name="string.upper_string.lower"></a>Sting formatieren mit upper() und lower()

Um Usereingaben besser mit vordefinierten Werten/Strings besser abgleichen zu können, ist es hilfreich die Usereingabe in Großen bzw. kleinen String zu konvertieren.

Beispiel: Der Juser wird nach Ja/Nein gefragt.
Somait kann dieser für ja folgendes eingeben:
* JA
* Ja
* jA
* ja

Natürlich kann auch das "Nein" verschieden abgefragt werden...

```python
antwort = input("Ihre Antwort: [Ja]/[Nein]")

if antwort.lower() == "ja":             # in Kleinbuchstaben umwandeln
    print("Ihre Antwort war \"Ja\"")
elif antwort.upper() == "NEIN":         # in Großbuchstaben umwandeln
    print("Ihre Antwort war \"Nein\"")
else:
    print("Ihre Antwort war werder \"Ja\" noch \"Nein\"")
```

## Tag 3 - 23.04.2020

### <a name="list"></a>Listen

Die Schreibweise erinnert sehr stark von anderen Sprachen wie Arrays/Verctoren (Bsp. in C#, Java, ...).<br/>
Jedoch sind diese komplex wie ArrayListen.

```python
# Schreibweise:
freunde = ["Max", "Peter", "Susi"]

# Einen Eintrag hinzufügen;
freunde.append("Anna")

# Einen Eintrag entfernen:
freunde.remove("Peter")

# Einzelnes Element ansprechen:
freunde[0] = "Stefan" # das 0te Element (Menschlich gezählt das erste)

# Sortieren:
freunde.sort()

# Alle Elemtente augeben:
print(freunde)
for f in freunde:
    print(f)
```

Eine Liste in Python mus nicht aus einem Typ bestehen...<br/>
Jedoch ist eine gemischte Liste mit Einschränkungen verbunden.<br/>
Gemischte Listen können nicht sortiert werden.<br/>

```python
lotto_ziehung = [2, 45, 12, 23, 8, 11]
lotto_ziehung.sort() # sortiert von der kleinsten zur größten Zahl
print(lotto_ziehung)

obst = ["Birne", "Zwetschke", "Kiwi", "Apfel"]
obst.sort() # Sortiert von Alphabetisch - A bis Z
print(obst)
obst.sort(reverse=True) # Sortiert von Alphabetisch - Z - A
print(obst)
```

Um nur bestimmte Elemente (Bsp.: nur die letzen oder ersten 5 Elemente) auszugeben gibt es einen eigenen Syntax.
```python
text = "Ich liebe meine 4 Kinder und den Burschen!"
print(text[0:4])    # vom 0ten weggezählt bis zum 4. Zeichen.
                    # Hier könnte man auch die "0" weglassen
                    # Ausgabe: "Ich "
print(text[2:-4])   # das Element mit der ID 2 (3. Zeichen) bis zum 4. Zeichen (vom Ende weggezählt)
                    # Ausgabe: "h liebe meine 4 Kinder und den Bursc"
```

### <a name="string.split"></a>String teilen mit split()

Um von einem Text die einzelnen Wörter zu erhalten bentigt man die .split()-Methode.<br/>
Dies ist unter anderem wichtig beim Einlesen von .txt, .csv Dateien.

Beispiel:
```python
text = "Ich liebe meine 4 Kinder und den Burschen!"
woerter = text.split(" ")   # in .split(" ") steht das Zeichen drinnen welches den Text trennen soll
print(woerter)

eingelesene_zeile = "Max,Mustermann,+4367687838830,max.mustermann@mail.zz,1010 Wien"
daten = eingelesene_zeile.split(",")
print(daten)
```

### <a name="csv_lesen_schreiben"></a>CSV-Dateien lesen und schreiben

CSV-Dateien sind oft von Tabellenkalkolationprogrammen oder Datenbanken exportiert worden.<br/>
Hier sind zwar noch alle Datensätze enthalten, jedoch sind diese mit einem Komma oder Semikolon getrennt.<br/>
Bei einem Export vom Tabellen-Kalkulationsprogramm sind Bilder, Grafiken & co entfernt worden.<br/>
<br/>
Das öffnen von Dateien kann auf 2 Wege erfolgen:<br/>
mit => f = open("Datei.txt", "r") <= öffnen<br/>
mit => f.close() <= schließen<br/>
oder mit => with opem("Datei.txt", "r") as file: <=<br/>
<br/>
Attribute:<br/>

| Code | Bedeutung |
|---|---|
| r | Datei nur zum Lesen öffnen. Beginnt am Anfang der Datei zu lesen. Dieser Standardmodus. |
| rb | Öffnen Sie eine Datei zum Lesen nur im Binärformat. Beginnt am Anfang der Datei zu lesen. |
| r+ | Datei zum Lesen und Schreiben öffnen. Dateizeiger am Anfang der Datei platziert. |
| w | Datei nur zum Schreiben öffnen. Dateizeiger am Anfang der Datei platziert. Überschreibt eine vorhandene Datei und erstellt eine neue, wenn sie nicht vorhanden ist. |
| wb | Wie w, jedoch im Binärmodus geöffnet. |
| w+ | Wie w, aber auch zum Lesen aus der Datei. |
| wb+ | Wie wb, aber auch zum Lesen aus der Datei. |
| a | Öffnen Sie eine Datei zum Anhängen. Beginnt am Ende der Datei mit dem Schreiben. Erstellt eine neue Datei, wenn die Datei nicht vorhanden ist. |
| ab | Wie a, jedoch im Binärformat. Erstellt eine neue Datei, wenn die Datei nicht vorhanden ist. |
| a+ | Gleich a a aber auch offen zum Lesen. |
| ab+ | Gleich ein ab, aber auch offen zum Lesen. |

Beispiel:
```python
"""
# Inhalt von person.csv:
Name,Age,Gender
Tina,23,female
Jakob,35,male
Barbara,44,female
"""
counter = 0

lineList = []
with open("person.csv", "r") as item:
    for line in item:
        if counter > 0:
            line = line.rstrip("\n")
            line = line.split(",")
            print(line[0] + " is " + line[2] + " and " + line[1] + " years old.")
        counter += 1

"""
# Inhalt von ninja.txt:
Hallo,
ich bin ein Text.
Lese mich aus ;-)
"""
with open("ninja.txt", "r") as file:
    #print(file.read())
    lines = file.readlines()
    for line in lines:
        print(line)

with open("ninja1.txt", "w") as file1:
    file1.write("Hallo neues File")

with open("ninja1.txt", "a") as file:
    file.append("\nappend")         # unter Windows: statt: "\n", "\r\n" eintragen
```

## Tag 4

## Tag 5

## Tag 6

## Tag 7

## Tag 8


