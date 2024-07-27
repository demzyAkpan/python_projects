import requests
from bs4 import BeautifulSoup


source = requests.get('https://www.nytimes.com/').text
soup = BeautifulSoup(source, features='lxml')
#print(soup.prettify())

headlines = soup.find('story-wrapper css-zirthl')
print(headlines)