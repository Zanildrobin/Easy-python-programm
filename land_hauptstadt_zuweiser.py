laender = {}
laender_2 = {}
fobj = open("hauptstaedte.txt", "r")
for line in fobj:
    line = line.strip()
    zuordnung = line.split(" ")
    laender[zuordnung[0]] = zuordnung[1]
    laender_2[zuordnung[1]] = zuordnung[0]
fobj.close()
while True:
    inp = input("Geben Sie eine Stadt oder ein Land ein, um die zugehörige Hauptstadt/das zugehörige Land zu erhalten.")
    if inp in laender:
        print("Die zugehörige Hauptstadt ist:",laender[inp])
    elif inp in laender_2:
        print("Das zugehörige Land ist:", laender_2[inp])
    else:
        print("Die Eingabe wurde nicht erkannt.")
