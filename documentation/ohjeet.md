# Käyttöohje 

Sovellusta voi käyttää joko Herokussa olevalla [testipalvelimella](https://mamelukin-muistilista.herokuapp.com/) tai paikallisessa virtuaaliympäristössä. Paikallisen virtuaaliympäristön käyttöönottoon on asennusohje alla. 


### Rekisteröityminen ja kirjautuminen

Sovelluksen käyttämiseen tarvitset käyttäjätunnuksen. Herokussa voit käyttää jo olemassaolevaa tunnusta testaamiseen:

- Käyttäjätunnus: testi
- Salasana: 123

Voit myös luoda uuden käyttäjän rekisteröitymällä. Kun olet luonut tunnuksen, voit kirjautua sillä sovellukseen.

### Muistilistan toiminta

Sovelluksen ideana on lisätä tehtäviä muistilistaan. Ennen tehtävän lisäämistä kannattanee luoda sopivia kategorioita, joita käyttää tehtävien luokitteluun. Kategorioita voi tarkastella "Listaa kategoriat" -linkin alta, missä niitä voi muokata tai halutessaan poistaa. Kategoriat ovat kaikkien käytössä - kuka tahansa kirjautunut käyttäjä voi muokata tai poistaa niitä. 

Tehtävät taas ovat henkilökohtaisia ja niitä voi luoda milloin vain. Tehtävälle annetaan nimi, prioriteetti, status (tehty vai tekemättä) sekä kategoria. Mitä pienempi prioriteetti, sitä tärkeämpi tehtävä on kyseessä. Tehtävällä voi myös olla monta kategoriaa, mutta se voi olla kokonaan ilmankin. "Listaa tehtävät" -linkin alta tehtäviä voi muokata, merkitä tehdyiksi tai poistaa. 

# Asennusohje

Luo sovellukselle paikallinen repositorio omalle koneellesi komennolla

``` 
git clone git@github.com:Mamelukki/Muistilista.git
``` 

Siirry kyseiseen hakemistoon ja luo sitten sovellukselle virtuaaliympäristö hakemiston juureen komennolla 

``` 
python3 -m venv venv
``` 

Aktivoi virtuaaliympäristö komennolla 

``` 
source venv/bin/activate
``` 

Asenna sovelluksen riippuvuudet komennolla 

``` 
pip install -r requirements.txt
``` 

Käynnistä sovellus komennolla 

``` 
python3 run.py
``` 

Sovelluksen pitäisi nyt olla käytettävissä osoitteessa localhost:5000
