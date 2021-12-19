# OhPe-2021-harj
Ohjelmoinnin perusteet harjoitustyö

Tekijät Aatos Helkkula ja Eemil Suominen

Aiheena elokuvateatterin varausjärjestelmä

Ylimääräisiä kirjastoja ovat `datetime` päivämäärien hallintaan ja `pickle` paikka- ja varausjärjestelmän tietokannan hallintaan.

## Käyttöohjeet
Aluksi ohjelman käynnistyessä käyttäjältä kysytään roolia.
Tähän on saatavilla vaihtoehdot 'Asiakas' tai 'Ylläpitäjä'.
Ylläpitäjän roolille on annettu _todella_ yksinkertainen salasanasuojaus menetelmällä
```
if input == salasana
    käyttäjä päästetään sisään
```

### Asiakas
Asiakkaalle annetaan aluksi kolme vaihtoehtoa
![image](https://user-images.githubusercontent.com/7459186/146674548-3cdabf40-d88b-492a-a8a9-4e92059bb59b.png)

Valitsemalla `varaus` asiakkaalta kysytään mihin elokuvaan varaus halutaan tehdä.
Tässä kohtaa asiakas ei kuitenkaan tiedä mihin elokuviin liput on mahdollista varata.
Siksi onkin suositeltavaa että asiakas valitsisi aluksi `tarkastelu`, jolloin ohjelma tulostaa ohjelmistossa olevat elokuvat ja näytökset.

### Ylläpitäjä
Valittaessa ylläpitäjän rooli, ohjelma antaa jälleen kolme vaihtoehtoa (salasanaa lukuunottamatta)
![image](https://user-images.githubusercontent.com/7459186/146674900-2a8d6d61-df26-455a-9a9f-b0cafa719703.png)
Ylläpitäjän on mahdollista lisätä ohjelmistoon elokuvia ja näytöksiä, sekä tarkastella niitä.

![image](https://user-images.githubusercontent.com/7459186/146674970-057cc1d6-6178-49f1-92cf-1e0fcf619ceb.png)
Lisätessä näytöksiä on ohjelman toiminnan kannalta tärkeää syöttää tiedot oikeassa muodossa.
Esimerkiksi sali on annettava muodossa `Sali 1`, eikä vain pelkkä numero.
