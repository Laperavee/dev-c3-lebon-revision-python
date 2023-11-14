import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(URL)
html = response.text
soup = bs(html,'html.parser')
countries = soup.find_all('div',{'class':'col-md-4 country'})
for country in countries:
    country_name = country.find("h3").get_text().replace('\n',"").replace("  ","")
    country_capital = country.find("span",{"class":"country-capital"}).get_text().replace('\n', "").replace("  ", "")
    print(country_name, "capitale =",country_capital)