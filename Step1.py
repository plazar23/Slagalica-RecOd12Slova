# This Python file uses the following encoding: utf-8

recnik = open('recnik.txt', encoding="utf-8")  # utf-8 je enkodovanje koje sve karaktere ispisuje bez greske
recnik1 = open('recnik1.txt', 'w', encoding="utf-8")  # morao je da se enkoduje upis u utf-8

for line in recnik:   # Listamo reci u recniku
    u = line.lower()  # Smanjujemo velika slova
    recnik1.write(u)  # Ovo ocekuje ulaz u stringu

# Step1 je zavrsen!!!
