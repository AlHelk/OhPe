def kopioi_oikeat_rivit():
    import re
    with open("lahde.txt") as tiedosto:
        for rivi in tiedosto:
            korjatut = re.search('^[A-Z][^?!.]*[.]$', rivi)

    with open("kohde.txt", "w") as tiedosto2:
                tiedosto2.write(korjatut)
