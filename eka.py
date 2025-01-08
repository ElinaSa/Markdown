# Se ihan ensimmäinen hei maailma -esimerkki tällä uudella koneella

print('Hello World')

print('Ja tämän sovelluksen koodasi Jakke Jäynä')

# ESIMERKKEJÄ MUUTTUJIEN KÄYTÖSTÄ 
# ===============================

# YKSINKERTAISET MUUTTUJAT
# ------------------------

# Merkkijono string

etunimi = 'Jonne' # Merkkijono string (str)
ika = 16 # Kokonaisluku integer (int)
ytoaineiden_keskiarvo = 2.5 # Liukuluku floating point number (float)
valmistunut = False # Totuusarvo boolean (bool)
print(etunimi, 'sai keskiarvoksi YTO-aineista', ytoaineiden_keskiarvo)
print(etunimi, 'on valmistunut', valmistunut)

# RAKENTEELLISET MUUTTUJAT
# ------------------------

# LIST (lista)
nimilista = ['Jonne', 'Jasmiina', 'Aleksanteri'] # Lista list
print('Listassa ensimmäisenä on', nimilista[0]) # Indeksissä 0 oleva arvo
jasenia = len(nimilista) # Listan jäsenmäärä selviää len-komennolla
print('nimilistassa on', jasenia, 'henkilöä')
nimilista.sort() # Listan sort-metodi aakkostaa sen
print('Aakkostettu lista on ', nimilista)

# TUPLE (monikko)
ryhmat = ('TiVi24A', 'TiVi23B', 'TiVi20oa') # Monikko tuple
print('Meidän ryhmä on', ryhmat[2]) 
# ryhmat[2] = 'Tivi20ka' # Yksittäistä jäsentä ei voi muuttaa
ryhmat = ('TiVi24A', 'TiVi23B', 'TiVi20ka')
print('Meidän uusi ryhmä on', ryhmat[2]) 

# SET (joukko)
# HUOM! Joukon jäseniin ei voi viitata indeksillä
joukko = {'Tuittu', 'Assi', 'Calle'}
print('Ja joukkoon kuuluvat', joukko) # Huomaa, että järjestys voi olla eri
joukko = {'Paavo', 'Assi', 'Calle'} # Joukko ylikirjoitetaan
print('Uudistettu joukko on', joukko)

# DICTIONARY, DICT (sanakirja eli AVAIN-ARVO -PARI)
henkilotiedot = {'etunimi':'Jonne', 'sukunimi': 'Jantteri', 'ika': 16}

print ('Opiskelijan', henkilotiedot['etunimi'], 'ikä on', henkilotiedot['ika'])

opiskelija1 = {'etunimi':'Jonne', 'sukunimi': 'Jantteri', 'ika': 16}
opiskelija2 = {'etunimi':'Iina', 'sukunimi': 'Urpo', 'ika': 17}
opiskelija3 = {'etunimi':'Tuittu', 'sukunimi': 'Kiukkunen', 'ika': 27}

# Lista sanakirjoista -> Taulukko
opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print('Opiskelijalista', opiskelijalista) # Tämän tyyppisiä listoja käytetään tietokannoissa

# QUEUE JA STACK (jono ja pino)
# Jonoilla ja pinoilla ei omia tietotyyppejä, ovat listoja

uusi_opiskelija = {'etunimi': 'Assi', 'sukunimi':'Kalma', 'ika':65 }

#Lisätään uusi arvo olemassa olevaan 
opiskelijalista.append(uusi_opiskelija)

# Tulostetaan opiskelijalistan ensimmäinen jäsen metodi pop(0)
print('Listassa ensimmäisenä on', opiskelijalista.pop(0))
# Tulostetaan opiskelijalistan viimeinen jäsen metodi pop()
print('Ja viimeisenä on', opiskelijalista.pop())