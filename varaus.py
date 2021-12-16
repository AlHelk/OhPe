from datetime import datetime
import pickle

salit = {"Sali 1": 50, "Sali 2": 45, "Sali 3": 70}
naytokset = []

def aloitus():
    print("Tervetuloa huoramaiseen varaussysteemiin.\nKiitos että nuolit perseen ja mulkun -Anssi.")
    while True:
        rooli = input("Valitse rooli (Asiakas / Ylläpitäjä): ")
        if rooli == "Asiakas":
            asiakas_rooli()
            break
        elif rooli == "Ylläpitäjä":
            yllapitaja_rooli()
            break
        else:
            print("Ei hyväksyttävä rooli, valitse Asiakas tai Ylläpitäjä.")

def asiakas_rooli():
    valinta_asiakas = input("Haluatko varata paikan vai tarkastella näytöksiä? Valitse (Varaus / Tarkastelu): ")
    if valinta_asiakas == "Varaus":
        elokuva = input("Valitse elokuva: ")
        for naytos in naytokset:
            if naytos[0] == elokuva:
                aika = naytos[4].strftime("%d.%m %H:%M")
                print(f"Ajankohta: {aika}, sali: {naytos[2]}, Vapaita paikkoja: {naytos[3]}, Id: {naytos[5]}")
        varaus = int(input("Valitse id: "))
        maara = int(input("Kuinka monta paikkaa haluat varata: "))
        for i in naytokset:
            if i[5] == varaus:
                varaa_paikka(i, maara)

def yllapitaja_rooli():
    print("wenis")
    lisaa_naytos()

def lataa_tiedosto():
    with open("jotai.txt", "rb") as tiedosto:
        return pickle.load(tiedosto)

def tallenna_tiedostoon():
    with open("jotai.txt", "wb") as tiedosto:
        pickle.dump(naytokset, tiedosto) 

def tallenna_naytos_listaan(elokuva: str, kesto: int, sali: str, pvm: str, klo: str, id):
    ajankohta = datetime(int(pvm[2]), int(pvm[1]), int(pvm[0]), int(klo[0]), int(klo[1])) 
    vapaat_paikat = salit[sali]
    naytoksen_tiedot = (elokuva, kesto, sali, vapaat_paikat, ajankohta, id)
    naytokset.append(naytoksen_tiedot)

def varaa_paikka(naytos, maara):
    a = list(naytos)
    if a[3] >= maara:
        a[3] -= maara
        b = tuple(a)
        c = naytokset.index(naytos)
        naytokset[c] = b
        print(f"Varattiin {maara} paikkaa.")
    else:
        print("Salissa ei ole tarpeeksi tilaa!")
    
def tulosta_naytos(naytos):
    print(f"Elokuva: {naytos[0]}\nKesto: {naytos[1]} minuuttia\nAjankohta: {naytos[4]}\n{naytos[2]}\nVapaita paikkoja: {naytos[3]}\nId: {naytos[5]}")

def lisaa_naytos():
    print("Näytösten ja elokuvien lisäys")
    while True:
        kertoja = int(input("Montako kertaa peräkkäin näytös toistuu: "))
        if kertoja > 1:
            monta_naytosta(kertoja)
        else:
            elokuva = str(input("Anna elokuvan nimi: "))
            kesto = int(input("Elokuvan kesto minuuteissa: "))
            sali = str(input("Valitse sali: "))
            pvm = str(input("Päivämäärä: ")).split(".")
            klo = str(input("Kellonaika: ")).split(":")
            naytos_id = 1000
            n = 0
            while n < 10000:
                for i in naytokset:
                    if i[-1] == naytos_id:
                        naytos_id += 1
                n += 1
            tallenna_naytos_listaan(elokuva, kesto, sali, pvm, klo, naytos_id)
            
        lopetus = input("Näytös lisätty, kirjoita 'lopeta' poistuaksesi lisäysjärjestelmästä, muutoin jätä tyhjäksi. ")
        if lopetus == "lopeta":
            break

def selaa_naytoksia():
    valinta = input("Valitse millä haluat hakea (Elokuva/Päivämäärä/Id/Näytä kaikki elokuvat)")
    if valinta == "Elokuva":
        ek = input("Valitse elokuva: ")
        for i in naytokset:
            if i[0] == ek:
                pass
    if valinta == "Päivämäärä":
        pass
    if valinta == "Id":
        pass

def monta_naytosta(kertoja: int):
    elokuva = str(input("Anna elokuvan nimi: "))
    kesto = int(input("Elokuvan kesto minuuteissa: "))
    sali = str(input("Valitse sali: "))
    pvm = str(input("Päivämäärä: ")).split(".")
    klo = str(input("Kellonaika: ")).split(":")
    abc = []
    defg = []
    k = 0
    for i in pvm:
        defg.append(int(i))
    for j in klo:
        abc.append(int(j))

    while True:
        if k >= kertoja:
            break
        m = kesto + 15
        minuutit = abc[1]
        tunnit = abc[0]
        t = 0
        while m >= 60:
            m -= 60
            t += 1
        
        if minuutit + m >= 60:
            t += 1
            m -= 60
            abc[1] = minuutit + m
        else:
            abc[1] = minuutit + m

        abc[0] = tunnit + t            
        if abc[0] >= 24:
            abc[0] = 24 - abc[0]
            if defg[1] in [1, 3, 5, 7, 8, 10, 12]:                
                if defg[1] == 12 and defg[0] >= 31:
                    defg[2] += 1
                    defg[0] = 1
                    defg[1] = 1
                else:
                    if defg[0] >= 31:
                        defg[1] += 1
                        defg[0] = 1
                    else:
                        defg[0] += 1              
            elif defg[1] == 2:
                if defg[2] == defg[2] % 4 == 0 and (defg[2] % 100 != 0 or defg[2] % 400 == 0):
                    if defg[0] == 29:
                        defg[0] = 1
                        defg[1] += 1
                    else:
                        defg[0] += 1
                else:
                    if defg[0] == 28:
                        defg[1] += 1
                        defg[0] = 0
                    else:
                        defg[0] += 1
            else:
                if defg[0] == 30:
                    defg[1] += 1
                    defg[0] = 1
                else:
                    defg[0] += 1
                
        naytos_id = 1000
        n = 0
        while n < 10000:
            for i in naytokset:
                if i[-1] == naytos_id:
                    naytos_id += 1
            n += 1
        tallenna_naytos_listaan(elokuva, kesto, sali, defg, abc, naytos_id)
        k += 1
        
naytokset = lataa_tiedosto()
print(naytokset)
aloitus()
tallenna_tiedostoon()