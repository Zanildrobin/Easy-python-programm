"""
  Super tolles Programm
"""


class Daten():

    def __init__(self):
        self.laender = {}
        self.hauptstaedte = {}
        self.einwohnerzahlen = {}

    def add_row(self, columns):
        land, hauptstadt, einwohnerzahl = columns
        self.laender[land] = hauptstadt
        self.hauptstaedte[hauptstadt] = land
        self.einwohnerzahlen[land] = einwohnerzahl

    def get_hauptstadt_by_land(self, land):
        if land in self.laender:
            return self.laender[land]

        return None


def daten_einlesen():
    daten = Daten()

    with open("hauptstaedte.txt", "rb") as fobj:
        lines = fobj.read().decode("utf-8").replace("\r", "").split("\n")

    for line in lines:
        daten.add_row(line.split(","))

    return daten


def nutzer_bedienen(daten):
    while True:
        print("Geben Sie eine Stadt oder ein Land ein, um die zugehörige "
              "Hauptstadt/das zugehörige Land zu erhalten.")
        inp = input()

        hauptstadt_by_land = daten.get_hauptstadt_by_land(inp)

        if hauptstadt_by_land:
            print("Die zugehörige Hauptstadt ist:", hauptstadt_by_land)
            print("Diese Stadt hat", daten.einwohnerzahlen[inp], "Einwohner")
        elif inp in daten.hauptstaedte:
            print("Das zugehörige Land ist:", daten.hauptstaedte[inp])
        else:
            print("Die Eingabe wurde nicht erkannt.")


def main():
    daten = daten_einlesen()
    nutzer_bedienen(daten)


if __name__ == "__main__":
    main()
