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


class hirsipuu:
    arvattu=[]
    sana=[]
    vaara=[]
    kirjain=""
    yritysta=0

    def __init__(self):
        self.arvattu=[]
        self.sana=[]
        self.vaara=[]
        self.yritysta=0
### määritetään metodi joka arpoo sanan 
    def arvoSana(self, sana):
        self.lista=[]
        sana = sana.upper()
        for char in sana:
            self.lista.append(char)
        self.arvattu=["_","_","_","_","_","_","_"]

###Määritetään metodi, joka tarkistaa onko arvattu kirjain sanassa.
    def tarkista(self,kirjain):
        self.vaara.append(kirjain)
        numero=0

        if kirjain in self.lista:
            for i in self.lista: 
                if kirjain==self.lista[numero]:
                    self.arvattu[numero]=i
                    numero=numero+1
                else:
                    numero=numero+1
        else:
            self.vaara.append(kirjain)
            self.yritysta=self.yritysta+1
                



tikku=hirsipuu()

kirjain="1"
tikku.arvoSana("MAKKARA")
while tikku.yritysta<9:
    print(tikku.arvattu)
    print(tikku.vaara)
    print(tikku.yritysta)
    kirjain=input("Anna kirjain")    
    tikku.tarkista(kirjain)
print("Hävisit")