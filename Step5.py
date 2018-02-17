import random
handle = open('recnik.txt', encoding="utf-8")
slovo = ['A', 'B', 'C', 'Ć', 'Č', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']
for br_slova in range(1, 13):
    b = random.randint(0, 26)
    print(br_slova)
    print(slovo[b])

# TODO Izvrsiti normalizaciju random funkcije
# TODO Ulepsati ispis
