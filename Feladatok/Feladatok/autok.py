class Autok:
    def __init__(self,fajl):
        self.fajl=fajl

    def beolvas(self):
        autok_lista=[]

        with open("autok.txt","r",encoding='utf-8') as f:
            sorok=f.readlines()

            for sor in sorok[1:]:
                adat=sor.strip()
                adatok=adat.split(';')

                nev=adatok[0]
                marka=adatok[1]
                uzemanyag=adatok[2]
                evjarat=int(adatok[3])

                autok_lista.append([nev,marka,uzemanyag,evjarat])

        return autok_lista
    
    def kiir(self,lista):
        for list in lista:
            print(f"{list[0]}; {list[1]}; {list[2]}; {list[3]}")


    def legrebbi(self,lista):
        legregebbi=float('inf')
        legregebbi_nev=""

        for list in lista:
            if list[3]<legregebbi:
                legregebbi=list[3]
                legregebbi_nev=list[0]

        print(f"A legregebbi autó neve: {legregebbi_nev}; évjárata: {legregebbi}")

    def markak(self,lista):
        markak_lista=[]
        for list in lista:
            if list[1] not in markak_lista:
                markak_lista.append(list[1])
        print(';'.join(i for i in markak_lista))
        return markak_lista

    def benzinesmegszamol(self,lista):
        db=0
        for list in lista:
            if list[2]=="benzines":
                db+=1
        print(f"A benzines autók száma: {db}")

    def markakiir(self,lista):
        with open("ujautok.txt","w",encoding='utf-8') as fajl:
            fajl.write(';'.join(i for i in lista))

autok1=Autok('autok.txt')
autok_lista=autok1.beolvas()
autok1.kiir(autok_lista)
autok1.legrebbi(autok_lista)
markak_lista=autok1.markak(autok_lista)
autok1.benzinesmegszamol(autok_lista)
autok1.markakiir(markak_lista)


