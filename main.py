import requests
from bs4 import BeautifulSoup
import re

url = "http://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/syu/1giin.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')  # BeautifulSoupの初期化

profile = []
table = soup.findAll("table")[2]
tds = table.findAll("tr")
tds.pop(0)
for td in tds:
    sh1td5 = td.find("td", {"class": "sh1td5"})
    n = sh1td5.find("a")
    nametext = n.text
    link = n.get("href")
    sepa =
    print(nametext + " " + link)

#names = soup.findAll("td", {"class": "sh1td5"})
# for n in names:
#    print(n.text)
#shtd = tbody.findAll("td", {"class": "sh1td5"})
# print(shtd)
