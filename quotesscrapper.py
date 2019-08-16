import bs4
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
driver.get('https://www.brainyquote.com/top_100_quotes')
res = driver.execute_script("return document.documentElement.outerHTML")
soup = bs4.BeautifulSoup(res , 'lxml')
driver.quit()

containers = soup.findAll('a')
qt = []
for items in containers:
    qt.append(items.text)

qt = qt[80:146]

quotes = []
#quotes[] contains all the quotes
authors = []
# authors[] contains all the respective authors of quotes[i]
i=0
while i < len(qt)-1:
    quotes.append(qt[i])
    i +=1
    authors.append(quotes[i])
    i=i+1
print(quotes)
print(len(quotes))
print(authors)
print(len(authors))


