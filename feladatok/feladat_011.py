# feladat_011
'''
kerjunk be ket szamot e sirassuk ki hiogy a szami 1 kisebb mint a szxam2
vagy a szam 2 kisebbmint a szam1
vagy a szam1 egyenlo a szam2 vel
'''
szam1 =int(input("adj megy egy szamo /szam1/: "))
szam2 =int(input("adj megy egy szamo /szam2/: "))

if szam1 > szam2:
    print('a szam1 nagyobb mint a szam2')
elif szam1 < szam2:
    print('a szam2 nagyobb mint a szam1')
elif szam1 == szam2:
    print('a ket szam egyenlo')
    
# if szam1 > szam2:
#     print('a szam1 nagyobb mint a szam2')
# if szam1 < szam2:
#     print('a szam2 nagyobb mint a szam1')
# if szam1 == szam2:
#     print('a ket szam egyenlo')

# if szam1 > szam2:
#     print('a szam1 nagyobb mint a szam2')
# elif szam1 < szam2:
#     print('a szam2 nagyobb mint a szam1')
# else:
#     print('a ket szam egyenlo')