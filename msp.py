import bs4
import requests

url = 'https://www.mysmartprice.com/mobile/oneplus-6t-msp14895'

page = requests.get(url)
soup = bs4.BeautifulSoup(page.text , 'html.parser')


containers = soup.findAll("div" , {"class" : "prc-tbl__row-wrpr"})
cpu= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--cpu"})
ram= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--ram"})
storage= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--strge"})
battery= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--bttry"})
camera= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--cmra"})
screensize= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--aspct"})
sim= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--sim"})
os= soup.findAll("li" , {"class" : "kyspc__item kyspc__item--os"})

productdata = []
for item in cpu:
    productdata.append(item.getText())
for item in ram:
    productdata.append(item.getText())
for item in storage:
    productdata.append(item.getText())
for item in battery:
    productdata.append(item.getText())
for item in camera:
    productdata.append(item.getText())
for item in screensize:
    productdata.append(item.getText())
for item in sim:
    productdata.append(item.getText())
for item in os:
    productdata.append(item.getText())

#print(len(containers))
print(containers[0])

stores = []
prices = []
for items in containers:
    stores.append(items["data-storename"])
    prices.append(items.getText())

print(stores)
print(prices)
print(productdata)


