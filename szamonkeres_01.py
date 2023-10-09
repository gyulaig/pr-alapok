print('Gyulai Gergo Zsolt')
jegy = int(input('Kerek egy jegyet 1-5: '))

if jegy == 5:
    print(f'A jegyed {jegy} jeles')
elif jegy == 4:
    print(f'A jegyed {jegy} jo')
elif jegy == 3:
    print(f'A jegyed {jegy} kozepes')
elif jegy == 2:
    print(f'A jegyed {jegy} elegseges')
elif jegy == 1:
    print(f'A jegyed {jegy} elegtelen')
elif jegy > 5 or jegy < 1:
    print(f'A jegyed {jegy} ami nem megfelelo')