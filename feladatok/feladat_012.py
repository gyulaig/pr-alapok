# be: pozitiv egesz
# ki: a szam paros vagy paratlan

szam = int(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print(f" {szam} páros szám.")
else:
    print(f" {szam} páratlan szám.")