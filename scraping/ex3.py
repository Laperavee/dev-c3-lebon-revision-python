import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.scrapethissite.com/pages/forms/?page_num=1"
response = requests.get(URL)
html = response.text
soup = bs(html,'html.parser')
teams = soup.find_all('tr',{'class':'team'})
for team in teams:
    print(team.get_text().replace('\n',"").replace("   ",""))