import requests
import bs4

def wiki_scrapper(topic):
    url = 'https://en.wikipedia.org/wiki/'+topic
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text , 'lxml')
    data1= soup.select('p')
    content = []
    for i in data1:
        content.append(i.getText())
    print(content[1])

def main():
    topic=input('Enter a topic to search wiki: ')
    wiki_scrapper(topic)
