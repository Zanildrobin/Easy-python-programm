laender = {}
laender_2 = {}

with open("hauptstaedte.txt", "r") as fobj:
    lines = fobj.readlines()
    lines = [line.strip() for line in lines]

for line in lines:
    zuordnung = line.split(" ")
    laender[zuordnung[0]] = zuordnung[1]
    laender_2[zuordnung[1]] = zuordnung[0]

while True:
    print("Geben Sie eine Stadt oder ein Land ein, um die zugehörige Hauptstadt/das zugehörige Land zu erhalten.")
    inp = input()

    if inp in laender:
        print("Die zugehörige Hauptstadt ist:", laender[inp])
    elif inp in laender_2:
        print("Das zugehörige Land ist:", laender_2[inp])
    else:
        print("Die Eingabe wurde nicht erkannt.")
