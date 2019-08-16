import requests
import bs4

html = requests.get('https://en.wikipedia.org/wiki/Big_Bang')
soup = bs4.BeautifulSoup(html.text,'lxml')
#print(type(soup))
data = soup.select('p')
#print
contents = []
for i in data:
    contents.append(i.getText())
print(contents[1])
