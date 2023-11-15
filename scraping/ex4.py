import requests
from bs4 import BeautifulSoup as bs
nbpages = 10
for i in range(0,nbpages):
    URL = f"https://www.scrapethissite.com/pages/forms/?page_num={i+1}"
    response = requests.get(URL)
    html = response.text
    soup = bs(html,'html.parser')
    teams = soup.find_all('tr',{'class':'team'})
    for team in teams:
        team_info = team.find_all('td')
        team_inf = []
        for info in team_info:
            team_inf.append(info.get_text().replace("  ","").replace('\n',''))
        print(team_inf[0],team_inf[1],team_inf[2],team_inf[5],"%")