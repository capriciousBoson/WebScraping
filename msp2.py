import bs4
import requests

url = 'https://www.mysmartprice.com/msp/search/search.php?search_type=auto&typed_term=iphone%20x&s=iphone%20x#s=iphone%20x'

page = requests.get(url)
soup = bs4.BeautifulSoup(page.text , 'lxml')

containers2 = soup.findAll('div',{'class':'sctn prdct-grid prdct-grid--s prdct-grid--spcftn-0 clearfix prdct-grid--prdct-s'})
print(containers2)
'''
productnames = []
links=[]
for items in containers:
    product=items.findAll("a" , {"class" : "sctn prdct-grid prdct-grid--s prdct-grid--spcftn-0 clearfix prdct-grid--prdct-s"})
    productnames.append(product[0].getText())
    links.append(items.a["href"])
print(productnames)
print(links)
'''