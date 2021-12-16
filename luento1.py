lista = [-12, 3, -65]

def muuta_itseisarvoiksi(lista: list):
    itseisarvo = [abs(ele) for ele in lista]
    return itseisarvo

print(muuta_itseisarvoiksi(lista))