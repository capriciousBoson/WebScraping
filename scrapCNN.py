import requests
import bs4

url = 'https://www.bbc.com/news'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text , 'lxml')
data1= soup.select('.gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
print(data1)
'''


content = []
for i in data1:
    content.append(i.getText())
    print(i.getText())
'''