import requests
from bs4 import BeautifulSoup

res = requests.get('http://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
