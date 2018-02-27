recnik2 = open('recnik2.txt', 'r', encoding="utf-8")  # morao je da se enkoduje upis u utf-8
reci4slova = open('reci4slova.txt', 'w', encoding="utf-8")
reci5slova = open('reci5slova.txt', 'w', encoding="utf-8")
reci6slova = open('reci6slova.txt', 'w', encoding="utf-8")
reci7slova = open('reci7slova.txt', 'w', encoding="utf-8")
reci8slova = open('reci8slova.txt', 'w', encoding="utf-8")
reci9slova = open('reci9slova.txt', 'w', encoding="utf-8")
reci10slova = open('reci10slova.txt', 'w', encoding="utf-8")
reci11slova = open('reci11slova.txt', 'w', encoding="utf-8")
reci12slova = open('reci12slova.txt', 'w', encoding="utf-8")
ostalereci = open('osatlereci.txt', 'w', encoding="utf-8") #ovo je lepse u petlji da se odradi, i da postoji niz koji se 
#sastoji od imena fajlova

pomocnalista = list()
pomocnistring = str()

for line in recnik2:                                              # Ravzvrstavamo u fajlove
    del pomocnalista[:]
    pomocnalista = line.split()
    if int(pomocnalista[1]) < 4 or int(pomocnalista[1]) > 12:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        ostalereci.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 4:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci4slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 5:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci5slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 6:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci6slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 7:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci7slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 8:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci8slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 9:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci9slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 10:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci10slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 11:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci11slova.write(pomocnistring + '\n')
    elif int(pomocnalista[1]) == 12:
        del pomocnalista[1]
        pomocnalista.reverse()
        pomocnistring = str(' '.join(pomocnalista[:]))
        reci12slova.write(pomocnistring + '\n')
