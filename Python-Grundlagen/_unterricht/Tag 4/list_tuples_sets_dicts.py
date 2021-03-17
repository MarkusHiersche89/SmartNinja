#text = "hallo, mein Name ist Markus, ich bin 30 Jahre alt."
#x = text.split(", ")
#print(x)

# [] => liste
# () => tuple
# {} => dictionary => unique
# ?? => ?? => nicht indexiert

liste = ["Apfel", "Banane", "Kirsche", "Orange", "Melone"]
print(type(liste))
print(liste)
if "Orange" in liste:
    print("Orange existiert")
print(len(liste))
liste.insert(2, "Ananas")
print(liste)
liste.remove("Kirsche")
print(liste)
print(liste.pop(2)) # liefert Element zurück und entfernt es aus der Liste
print(liste)
liste1 = liste.copy() # Copy #1
liste2 = list(liste)  # Copy #2
liste3 = liste1 + liste2
liste4 = list(("Apfel", "Banane", "Kirsche", "Orange", "Melone"))
print(liste1)
print(liste2)
print(liste3)
print(liste4)
del liste[0]
print(liste)
del liste
#print(liste) # NameError: name 'liste' is not defined

print("\n***\n")
## Dictionary

dictionary = {"marke" : "Ford", "Modell" : "Mustang", "Baujahr" : 1964} # key : value
print(type(dictionary))
print(dictionary)
x = dictionary["Modell"]
print(x)
y = dictionary.get("Modell")
print(y)
dictionary["Baujahr"] = 2020
print(dictionary)
for x in dictionary:
    print(x)
for x in dictionary:
    print(dictionary.get(x))
for x in dictionary:
    print(str(x) + " : " + str(dictionary.get(x)))
for x in dictionary.values():
    print(x)
if "Modell" in dictionary:
    print("Ja, Modell existiert")


