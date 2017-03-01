from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
wiki_page = urlopen(url).read()
wiki_soup = BeautifulSoup(wiki_page)

wiki_table = wiki_soup.findAll("table", {"class": "wikitable"})
url2 = "https://en.wikipedia.org"
sum_of_views = 0
for key in wiki_table:
    seasons = key.findAll("a", {"href": True})
    for key in seasons:
        if "Season" in key.string:
            url_sezone = url2+key["href"]
            for i in range(0,6):
                season_page = urlopen(url_sezone).read()
                season_soup = BeautifulSoup(season_page)
                season_table = season_soup.findAll("table", {"class": "wikitable plainrowheaders wikiepisodetable"})
                for key in season_table:
                    row = key.findAll("tr",{"class": "vevent"})
                    for key in row:
                        views = key.findAll("td")[-1]
                        views = views.text
                        views = views[0:4]
                        views = float(views)
                        sum_of_views += views

print("Serijo Game of Thornes si je ogledalo %s miljonov uporabnikov" %(sum_of_views))
