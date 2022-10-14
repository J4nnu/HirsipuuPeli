# HirsipuuPeli

Klassinen hirsipuupeli komentorivillä. 
Peliin kuuluu 3 tiedostoa. main.py josta peli käynnistetään. 
hirsipuu.py joka sisältää hirsipuu luokan metodeineen. 
Sanoja.txt jossa on arvailtavia sanoja. Sanoja voi lisätä tai poistaa kunhan sanat erottaa välilyönnillä.

## Toiminta
Alussa peli kysyy aloitetaanko uusi peli vai suljetaanko sovellus. 
Kun uusi peli aloitetaan, luodaan **hirsipuu** luokasta **uusipeli** niminen olio.
Olioon arvotaan sana *arvoSana* metodilla.
komentoriville, tai terminaaliin tulostetaan arvuuteltava sana _ merkillä, arvatut kirjaimet, sekä väärien yritysten määrä.
Jos arvaat kirjaimen oikein, se asetetaan arvattavaan sanaan oikeaan kohtaa _ merkin tilalle sekä arvattujen kirjaimien listaan.. 
Jos arvaus on väärä, kirjain lisätään arvattujen kirjaimien listaan ja väärien yritysten laskuri nousee. 
Jos löydät kaikki oikeat kirjaimet, peli onnittelee ja kysyy pelataanko uudestaan vai lopetetaanko. Jos aloitetaan uusi peli, arvotaan uusi sana ja aloitetaan alusta. Lopetuksella peli sammuu. 
Jos et arvaa sanaa, ja laskuri menee 9/9, peli ilmoittaa tappiosta ja näyttää oikean sana sekä kysyy pelataanko uusi peli.

![tuloste](/voitto.PNG)

![tappio](/havio.PNG)

<<<<<<< HEAD
![voitto](/voitto.PNG)
=======
![voitto](/voitto.PNG)
>>>>>>> 0ac8768c9e1f396dab077a8f7a8b61f5322a0480
