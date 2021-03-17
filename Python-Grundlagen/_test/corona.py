# https://api.covid19api.com/   <== API
# https://covid19api.com/       <== Website
# Ländercode: https://www.oenb.at/Statistik/Klassifikationen/ISO-Codes/ISO-Code-Verzeichnis-fuer-Laender--und-Waehrungscodes.html

import json
from urllib.request import urlopen

download = input("Daten neu herunterladen [j/n]: ").lower()

if download == "j":
    print("Download gestartet... Bitte um etwas Geduld.")
    website = "https://api.covid19api.com/all"
    data = json.loads(urlopen(website).read())

    with open('corona.json', 'w') as file:
        json.dump(data, file)
else:
    with open("corona.json", "r") as file:
        data = json.load(file)

while True:
    land_code = input("\nLändercode / [end für beenden]: ").upper()
    if land_code == "END":
        print("Programm beendet")
        break
    best = 0
    tote = 0
    geheilt = 0
    inf = 0
    land = ""
    date = ""
    zaehler = 0
    print("\n*** Daten von " + land_code + " ***")
    for c in data:
        # GANZER DATENSATZ
        # {"Country": "Afghanistan",
        #  "CountryCode": "AF",
        #  "Province": "",
        #  "City": "",
        #  "CityCode": "",
        #  "Lat": "33.94",
        #  "Lon": "67.71",
        #  "Confirmed": 0,
        #  "Deaths": 0,
        #  "Recovered": 0,
        #  "Active": 0,
        #  "Date": "2020-01-22T00:00:00Z"
        # }
        # BRAUCHBARE DATEN
        # { "Country": "Afghanistan",       LAND
        #   "CountryCode": "AF",            LAENDER_CODE
        #   "Confirmed": 0,                 ERKRANKT
        #   "Deaths": 0,                    TOTE
        #   "Recovered": 0,                 GEHEILT
        #   "Active": 0,                    KRANK
        #   "Date": "2020-01-22T00:00:00Z"  DATUM
        if c.get("CountryCode") == land_code:
            print(str(c.get("Date")) + " | Bestätigt: " + str(c.get("Confirmed")) + " | Tote: " + str(c.get("Deaths")) + " | Geheilte: " + str(c.get("Recovered")) + " | Infiziert: " + str(c.get("Active")))
            if date == c.get("Date"):
                best += c.get("Confirmed")
                tote += c.get("Deaths")
                geheilt += c.get("Recovered")
                inf += c.get("Active")
                zaehler += 1
            else:
                date = c.get("Date")
                best = c.get("Confirmed")
                tote = c.get("Deaths")
                geheilt = c.get("Recovered")
                inf = c.get("Active")
                zaehler = 1
            land = c.get("Country")
    try:
        sterbe_rate = tote / best * 100
        heil_rate = geheilt / best * 100
        infiziert = 100 - sterbe_rate - heil_rate
        print("\n*** Personen in " + land + ": ***")
        print("Bestätigt: " + str(best))
        print("Gestorben: " + str(tote))
        print("Geheilt: " + str(geheilt))
        print("Erkrankt: " + str(best - tote - geheilt))

        print("\n*** % von erkrankten in " + land + ": ***")
        print("Bestätigt: " + "100")
        print("Gestorben: " + str(sterbe_rate))
        print("Geheilt: " + str(heil_rate))
        print("Erkrankt: " + str(infiziert))

        print("\nQuelle: Johns Hopkins University (CSSE)")
        print(str(zaehler) + " Einträge vom letzten Tag gefunden")
    except:
        print("\nDaten konnten nicht ausgelesen werden!")