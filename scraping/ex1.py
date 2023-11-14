import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(URL)
html = response.text
soup = bs(html,'html.parser')
countries = soup.find_all('h3',{'class':'country-name'})
for country in countries:
    print(country.getText().replace('\n',"").replace("  ",""))