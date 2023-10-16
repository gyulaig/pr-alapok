gondolt_szam = 3  

szam = int(input("Kérem, adjon meg egy számot 1 és 5 között: "))

if szam == gondolt_szam:
    print("Gratulálok, Eltalálta a számot!")
elif szam < gondolt_szam:
    print("A száma kisebb mint a gondolt szám!")
else:
    print("A száma nagyobb mint a gondolt szám!")