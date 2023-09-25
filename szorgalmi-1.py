# szorgalmi_1
"""
Keszits egy Python programot, ami bekeri egy diak pontszámát (0 es 100 kozotti egesz szam), majd kiszamolja es kiirja a diak osztalyzatat az alábbi skalan:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""
pontszam = int(input("add meg a pontszamot: "))

if 0 <= pontszam <= 100:
    if 90 <= pontszam <= 100:
        osztalyzat = "A"
    elif 80 <= pontszam < 90:
        osztalyzat = "B"
    elif 70 <= pontszam < 80:
        osztalyzat = "C"
    elif 60 <= pontszam < 70:
        osztalyzat = "D"
    else:
        osztalyzat = "F"
    print(f"Az osztalyzatod: {osztalyzat}")
else:
    print("ervenytelen! kerlek, adj meg egy pontszamot 0 es 100 kozott.")

valasz = input("szeretnel ujra szamolni? (igen/nem) (y/n): ").lower()
if valasz != "igen" or 'ige' or 'igne' or 'y' or 'yes':
    print("legyen szep napod")
