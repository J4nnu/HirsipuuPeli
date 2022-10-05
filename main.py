# from tkinter import *
# master = Tk()
# Label(master, text='Enter Your Name').grid(row=0)
# Label(master, text='Enter Your Email').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()

# Tehdään graafinen hirsipuupeli

from pickle import TRUE
import random
class hirsipuu:
    oikein=[] #Listaan kerätään oikein arvatut kirjaimet
    sana=[] #listaan tallennetaan arvailtava sana
    arvatut_kirjaimet=[] #listaan tallennetaan arvatut kirjaimet.
    kirjain="" #Arvattu kirjain
    yritysta=0 #yritysten määrä


    def __init__(self): #Luodaan uusi peli olio
        self.oikein=[]
        self.sana=[]
        self.arvatut_kirjaimet=[]
        self.yritysta=0


### määritetään metodi joka arpoo sanan ja tekee listan johon oikeat kirjaimet lisätään. 
    def arvoSana(self):

        with open("Sanoja.txt", "r") as file:  #Avataan tekstitiedosto johon on tallennettu sanoja. Arvotaan yksi sana.
            sanoja = file.read()
            sanoja = list(map(str, sanoja.split()))
        uusi_sana = random.choice(sanoja)
        uusi_sana = uusi_sana.upper() #Muutetaan kaikki merkit isoiksi. 

        for char in uusi_sana:
            self.sana.append(char) #Lisätään arvuuteltava sana "sana" listaan
        for char in uusi_sana:
            self.oikein.append("_") #tehdään tyhjä lista jossa on oikea määrä _ viivoja korvaamaan kirjaimet. 


###Määritetään metodi, joka tarkistaa onko arvattu kirjain sanassa.
    def tarkista(self,kirjain):
        kirjain = kirjain.upper() #Muutetaan kirjain isoksi. 
        self.arvatut_kirjaimet.append(kirjain) #Lisätään kirjain heti arvattujen listaan
        x=0 #Apumuuttuja jonka avulla oikea kirjain saadaan oikeaan kohtaan listassa.
        if kirjain in self.sana:
            for i in self.sana: #käydään lista läpi merkki kerrallaan ja korvataan sanan "_" merkki kirjaimella.
                if kirjain==self.sana[x]: 
                    self.oikein[x]=i
                    x=x+1
                else:
                    x=x+1
                
        else: #jos kirjain ei ole sanassa, lisätään 1 yrityksiin
            self.yritysta=self.yritysta+1

    def tulos(self):
        if self.yritysta==9:
            print("Hävisit pelin! Oikea sana oli: ","".join(uusipeli.sana))

        if self.sana == self.oikein:
            print("Onneksiolkoon voitit!")

#Pääohjelma
uusipeli=hirsipuu()
uusipeli.arvoSana()
while uusipeli.yritysta<9 and uusipeli.sana != uusipeli.oikein: #Kökkö tapa seurata kun peli voitetaan tai hävitään.
    print("Arvattava sana\n"," ".join(uusipeli.oikein))
    print("Arvatut kirjaimet\n",",".join(uusipeli.arvatut_kirjaimet))
    print("Yrityksiä: ",uusipeli.yritysta,"/9")
    kirjain=input("Anna kirjain: ")    
    uusipeli.tarkista(kirjain)
uusipeli.tulos() #Voiton/häviön jälkeen kutsutaan tulos metodia joka ilmoittaa tuloksen. 