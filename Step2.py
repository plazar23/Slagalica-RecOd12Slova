recnik1 = open('recnik1.txt', 'r', encoding="utf-8")  # morao je da se enkoduje upis u utf-8
recnik2 = open('recnik2.txt', 'w', encoding="utf-8")  # morao je da se enkoduje upis u utf-8

pomocnalista = list()

for rec in recnik1:                                                             # Listamo kroz reči u rečniku
    brojslova = 0                                                               # Inicijalizujemo brojač slova
    del pomocnalista[:]                                                         # Brišemo sadržaj liste
    for slovo in rec:                                                           # Listamo kroz slova u reči
        if slovo != '\n':                                                       # Proveravamo da li je slovo različito od newline karaktera
            brojslova += 1                                                      # Iterujemo brojač
            pomocnalista.append(slovo)                                          # Dodajemo slovo u listu
    pomocnalista.sort()                                                         # Sortiramo listu slova po abecednom redu
    string = ','.join(pomocnalista)                                             # Pravimo string formata slovo-zarez-slovo
    recnik2.write(rec.rstrip() + ' ' + str(brojslova) + ' ' + string + '\n')    # Upisujemo stringove odvojene razmakom i dodajemo newline karakter


# # Deo koda za debagovanje
# print('Nova rec')
# print(rec.rstrip())
# print(brojslova)
# print(string)
