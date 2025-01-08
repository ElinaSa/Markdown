# TOISTORAKENTEET
# ===============

# WHILE-SILMUKAT
# --------------

# Ikuinen silmukka
while True:
    print('Pyörin ikuisesti')
    poistu = input('Haluatko jatkaa? K/e ') # iso K oletusarvo jos painetaan vain enteriä
    if poistu == 'e':
        break # Poistutaan silmukasta

# Kierromääräinen silmukka
laskuri = 0
while laskuri <10:
    print('Nyt on menossa kierros', laskuri)
    laskuri += 1 # Tai laskuri = laskuri + 1

# FOR-SILMUKAT
# ------------

# Rakenteellisen muuttujan arvojen läpikäynti (iterable)
lista = ['Jonne', 'Tuittu', 'Jakke', 'Calle']
for jasen in lista: # value = hatusta vedetty muuttuja
    print(jasen, 'kuuluu listaan')

# Kierrosmääräinen silmukka
teksti = ''
for laskuri in range(30):
    teksti += 'X' # piirtelee x:iä
    print(teksti)

# Range-komento mahdollistaa alun, lopun ja asekeleet
for parilliset_kymmenet in range(20,100,20):
    print(parilliset_kymmenet)