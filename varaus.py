from datetime import datetime
import pickle

salit = {"Sali 1": 50, "Sali 2": 45, "Sali 3": 70}
naytokset = []

def aloitus():
    print("Tervetuloa varaussysteemiin.")
    while True:
        rooli = input("Valitse rooli (Asiakas / Ylläpitäjä): ")
        if rooli == "Asiakas":
            asiakas_rooli()
            break
        elif rooli == "Ylläpitäjä":
            while True:
                salasana = input("Anna salasana: ")
                if salasana == "salasana":
                    yllapitaja_rooli()
                    break
                else:
                    print("Väärä salasana, yritä uudelleen.")
            break
        else:
            print("Ei hyväksyttävä rooli, valitse Asiakas tai Ylläpitäjä.")

def asiakas_rooli():
    while True:
        valinta_asiakas = input("Haluatko varata paikan vai tarkastella näytöksiä? Valitse (Varaus / Tarkastelu / Lopeta): ")
        if valinta_asiakas == "Varaus":
            varaus()
        elif valinta_asiakas == "Tarkastelu":
            selaa_naytoksia()
        elif valinta_asiakas == "Lopeta":
            break
        else:
            print("Ei kelvollinen valinta. Yritä uudelleen.")

def yllapitaja_rooli():
    print("Oikea salasana")
    while True:
        valinta_yp = input("Haluatko lisätä vai tarkastella näytöksiä? (Lisää / Tarkastelu / Lopeta): ")
        if valinta_yp == "Lisää":
            lisaa_naytos()
        elif valinta_yp == "Tarkastelu":
            selaa_naytoksia()
        elif valinta_yp == "Lopeta":
            break
        else:
            print("Ei kelvollinen valinta. Yritä uudelleen.")

def lataa_tiedosto():
    with open("db.txt", "rb") as tiedosto:
        return pickle.load(tiedosto)

def tallenna_tiedostoon():
    with open("db.txt", "wb") as tiedosto:
        pickle.dump(naytokset, tiedosto) 

def tallenna_naytos_listaan(elokuva: str, kesto: int, sali: str, pvm: str, klo: str, id):
    try:
        ajankohta = datetime(int(pvm[2]), int(pvm[1]), int(pvm[0]), int(klo[0]), int(klo[1])) 
        vapaat_paikat = salit[sali]
        naytoksen_tiedot = (elokuva, kesto, sali, vapaat_paikat, ajankohta, id)
        naytokset.append(naytoksen_tiedot)
    except:
        print("Viimeisimmän näytöksen lisääminen epäonnistui. Yritä uudelleen")

def varaus():
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
            
        lopetus = input("Kirjoita 'lopeta' poistuaksesi lisäysjärjestelmästä, muutoin jätä tyhjäksi. ")
        if lopetus == "lopeta":
            break

def selaa_naytoksia():
    while True:
        valinta = input("Valitse millä haluat hakea (Elokuva / Päivämäärä / Id / Näytä kaikki elokuvat), (Taakse), jos haluat siirtyä taaksepäin,\ntai (Varaus) jos haluat siirtyä paikkavaraukseen: ")
        if valinta == "Elokuva":
            ek = input("Valitse elokuva: ")
            for i in naytokset:
                if i[0] == ek:
                    print(f"Elokuva: {i[0]}, Ajankohta: {i[4]}, {i[2]}, Vapaita paikkoja: {i[3]}, Id: {i[5]}")
        elif valinta == "Päivämäärä":
            pvm_valinta = str(input("Valitse päivämäärä (päivä.kuukausi.vuosi): "))
            for i in naytokset:
                aika = i[4].strftime("%d.%m.%Y")
                if aika == pvm_valinta:
                    print(f"Elokuva: {i[0]}, Kesto: {i[1]} minuuttia, Ajankohta: {i[4]}, {i[2]}, Vapaita paikkoja: {i[3]}, Id: {i[5]}")
        elif valinta == "Id":
            id_valinta = int(input("Valitse id: "))
            for n in naytokset:
                if n[5] == id_valinta:
                    print(f"Elokuva: {n[0]}, Kesto: {n[1]} minuuttia, Ajankohta: {n[4]}, {n[2]}, Vapaita paikkoja: {n[3]}, Id: {n[5]}")
        elif valinta == "Näytä kaikki elokuvat":
            elokuvat = {}
            for i in naytokset:
                if i[0] not in elokuvat:
                    elokuvat[i[0]] = i[1]
            for i in elokuvat:
                print(f"{i}, kesto: {elokuvat[i]} minuuttia")
        elif valinta == "Varaus":
            varaus()
            break
        elif valinta == "Taakse":
            break

        else:
            print("Ei kelvollinen valinta. Yritä uudelleen.")

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

    naytos_id = 1000
    n = 0
    while n < 10000:
        for i in naytokset:
            if i[-1] == naytos_id:
                naytos_id += 1
        n += 1
    tallenna_naytos_listaan(elokuva, kesto, sali, defg, abc, naytos_id)
    k += 1

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
                if defg[2] % 4 == 0 and (defg[2] % 100 != 0 or defg[2] % 400 == 0):
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
aloitus()
tallenna_tiedostoon()