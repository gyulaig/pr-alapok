# feladat_002
'''
Kerjunk be a billentyuzetrol ket egesz szamot, es irassuk ki a ket szam osszeget akepernyore
'''
'''
nev = input("Kerek egy nevet: ")
print(f"A megadott nev a kovetkezo: {nev}")
'''

szam1 = int(input("Adj meg egy szamot: "))
szam2 = int(input("Adj meg egy masik szamot: "))
szam3 = float(szam1)

osszeg = szam1 + szam2

print(f"A ket szam osszege: {szam1 + szam2}")
print(f"A ket szam osszege: {osszeg}")
print(f"A szam1 valtozo tipusa: {type(szam1)}")
print(f"A szam2 valtozo tipusa: {type(szam2)}")
print(f"A szam3 valtozo erteke: {szam3}")
print(f"A szam3 valtozo tipusa: {type(szam3)}")
print(f"A osszeg valtozo tipusa: {type(osszeg)}")