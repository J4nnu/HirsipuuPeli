#Hirsipuupeli jossa arvotaan tekstitiedostosta satunnainen sana jota koitetaan arvata kirjain kerrallaan.
from hirsipuu import hirsipuu

#Pääohjelma
valikko = int(input("Tervetuloa! Tämä on hirsipuu peli! \nAloita uusi peli valitsemalla [1],  Lopeta ja sulje peli valitsemalla [2]."))
if valikko==1:
    uusipeli=hirsipuu()
    uusipeli.arvoSana()
    while uusipeli.yritysta<9 and uusipeli.sana != uusipeli.oikein: #Kökkö tapa seurata kun peli voitetaan tai hävitään.
        print("Arvattava sana\n"," ".join(uusipeli.oikein))
        print("Arvatut kirjaimet\n",",".join(uusipeli.arvatut_kirjaimet))
        print("Yrityksiä: ",uusipeli.yritysta,"/9")
        kirjain=input("Anna kirjain: ")    
        uusipeli.tarkista(kirjain)
    uusipeli.tulos() #Voiton/häviön jälkeen kutsutaan tulos metodia joka ilmoittaa tuloksen. 
    valikko=int(input("Pelaa uudestaan, valitse 1. Lopeta ja sulje, valitse 2."))
else:
    print("Exit") 