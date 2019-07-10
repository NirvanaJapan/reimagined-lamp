import requests
response = requests.get("http://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/syu/1giin.htm")
print (response.text)
html_doc = requests.get("https://review-of-my-life.blogspot.com").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
print(soup.prettify())
