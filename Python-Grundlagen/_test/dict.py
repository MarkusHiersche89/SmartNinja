import json

with open("dict.txt", "r") as t:
    telefonbuch = json.loads(t.read())

while True:
    print("\n***Menü:***")
    print("[1] Eintrag hinzufügen")
    print("[2] Alle Einträge anzeigen")
    print("[3] Speichern")
    print("[0] Programm beenden")
    auswahl = int(input("Ihre Auswahl: "))
    if auswahl == 0:
        print("Programm wird beendet")
        break
    elif auswahl == 1:
        name = input("\nName: ")
        tel = input("Telefon: ")
        ort = input("Ort: ")
        telefonbuch.append({"name": name, "phone": tel, "city": ort})
    elif auswahl == 2:
        print("\nAlle Einträge:")
        for t in telefonbuch:
            print("Name: " + t.get("name") + " | Tel: " + t.get("phone") + " | Ort: " + t.get("city"))
    elif auswahl == 3:
        with open("dict.txt", "w") as d:
            d.write(json.dumps(telefonbuch))
    else:
        print("\nFalsche Eingabe gemacht!")
