from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

kontakti = []

class Oseba():
    def __init__(self, ime_priimek, spol, starost, kraj_bivanja,  email):
        self.ime_priimek = ime_priimek
        self.spol = spol
        self.starost = starost
        self.kraj_bivanja = kraj_bivanja
        self.email = email

def csv_file (kontakti):
    with open("web_scraping.csv", "w") as file:
        for oseba in kontakti:
            file.write("%s,%s,%s,%s,%s\n" % (oseba.ime_priimek, oseba.spol, oseba.starost, oseba.kraj_bivanja, oseba.email))

def main():
    url = "https://scrapebook22.appspot.com/"
    html = urlopen(url).read()
    prva_stran = BeautifulSoup(html)
    for povezava in prva_stran.findAll("a"):
        if povezava.string == "See full profile":
            url_profila = url + povezava["href"]
            html_profila = urlopen(url_profila).read()
            profil = BeautifulSoup(html_profila)

            ime_priimek = profil.find("div", {"class": "col-md-8"})
            ime_priimek = ime_priimek.h1.string

            starost = profil.find("div", {"class": "col-md-8"})
            starost = starost.ul.findAll("li")[1].string

            spol = profil.find("span", {"data-gender": True})
            spol = spol.string

            email = profil.find("span", {"class": "email"})
            email = email.string

            kraj_bivanja = profil.find("span", {"data-city": True})
            kraj_bivanja = kraj_bivanja.string

            oseba = Oseba(ime_priimek, spol, starost, kraj_bivanja,  email)
            kontakti.append(oseba)

if __name__ == '__main__':
    main()
csv_file(kontakti)