import requests
from bs4 import BeautifulSoup as bs
import csv

nbpages = 10
data = []
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
        if int(team_inf[-1]) > 0:
            data.append(team_inf)
with open("result.csv", "w") as file:
    filecsv = csv.writer(file, delimiter=",")
    filecsv.writerows(data)