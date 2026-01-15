class Diakok:
    def __init__(self,fajl):
        self.fajl=fajl

    def fajlbeolvas(self):
        diakok_lista=[]

        with open("diakok.txt","r",encoding='utf-8') as f:
            sorok=f.readlines()

            for sor in sorok[1:]:
                adat=sor.strip()
                adatok=adat.split(',')

                nev=adatok[0]
                osztaly=adatok[1]

                diakok_lista.append([nev,osztaly])
        return diakok_lista

    def kiir(self,lista):
        for l in lista:
            print(f"Név: {l[0]}, Osztály:{l[1]}")

    def osztalymegszamol(self,lista):
        db=0
        for l in lista:
            if l[1]=="10.A":
                db+=1
        print(f"{db} 10.A osztályos tanuló van.")

    def diakmegszamol(self,lista):
        print(f"A diákok száma: {len(lista)}")

peldeny1=Diakok('diakok.txt')
lista=peldeny1.fajlbeolvas()
peldeny1.kiir(lista)
peldeny1.osztalymegszamol(lista)
peldeny1.diakmegszamol(lista)