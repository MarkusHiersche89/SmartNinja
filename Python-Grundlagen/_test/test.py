#
# zum temporären testen...
#

"""
liste = ["Hallo", 1, 2.3, 'a']

for item in liste:
    print(str(item))

print("################################")

v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13]
print(v) # Alle Elemente
print(v[0]) # 1. Element
print(v[-1]) # letzte Element
v += [14, 15]
v.append(16)
print(v)
print(v[5:])
print(v[:-5])
print(v[5:5])
print(v[5:-5])

print("################################")



print("################################")

text = "Hallo mein Name lautet Markus"
woerter = text.split(" ")
print(woerter)
counter = 0
for item in woerter:
    if item == "Markus":
        woerter[counter] = "Susi"
    counter += 1
print(woerter)
"""
"""
list = [1,3,5,2,6,4]
list.sort()
print(list)

list = ["a", "r", "d", "l"]
list.sort()
print(list)

list = ["Hallo", "Hy", "Ciao", "Grüß Gott"]
list.sort()
print(list)

list = ["Hy", 23, 1.234, 'a', True]
#list.sort()
print(list)

list.append("wer")
list[0] = 123
print(list)

obst = ["Birne", "Zwetschke", "Kiwi", "Apfel"]
obst.sort() # Sortiert von Alphabetisch - A bis Z
print(obst)
obst.sort(reverse=True) # Sortiert von Alphabetisch - Z - A
print(obst)

text = "Ich liebe meine 4 Kinder und den Burschen!"
print(text[0:4])
print(text[2:-4])

woerter = text.split(" ")
print(woerter)

eingelesene_zeile = "Max,Mustermann,+4367687838830,max.mustermann@mail.zz,1010 Wien"
daten = eingelesene_zeile.split(",")
print(daten)
"""

"""
with open("text.txt", "r") as file:
    for line in file:
        print(line)
"""

f = open("datei.txt", "r")
for line in f:
    print(line)
f.close()
