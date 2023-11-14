import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(URL)
html = response.text
soup = bs(html,'html.parser')
