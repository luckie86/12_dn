from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()
prva_stran = BeautifulSoup(html)

citati = prva_stran.findAll("p", {"class": "quoteContent"})

for citat in citati:
    if "marriage" in citat.string:
        print citat.string
