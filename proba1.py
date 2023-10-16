# proba1

def menut_kiir(tipus):
    if tipus == 2:
        print("1. Uj adat bevitele")
        print("2. Kilepes a programbol")
    elif tipus == 3:
        print("1. Uj adat bevitele")
        print("2. Adatok modositasa / torles")
        print("3. Kilepes a programbol")
    elif tipus !=2 or tipus != 3:
        print("A megadott szam nem 2 sem 3")

menut_kiir(int(input("Kerek egy menu szamot: ")))