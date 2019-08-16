import requests
import bs4

res = requests.get('https://hackr.io/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
data = soup.select('title')
#type(data)
page=data[0].getText()
print(page)
