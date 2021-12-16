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
                tulosta_naytos(naytos)
                
                

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
    else:
        print("Salissa ei ole tarpeeksi tilaa!")
    
def tulosta_naytos(naytos):
    print(f"Elokuva: {naytos[0]}\nKesto: {naytos[1]} minuuttia\nAjankohta: {naytos[4]}\n{naytos[2]}\nVapaita paikkoja: {naytos[3]}\nId: {naytos[5]}")

def lisaa_naytos():
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

naytokset = lataa_tiedosto()
print(naytokset)
aloitus()
tallenna_tiedostoon()