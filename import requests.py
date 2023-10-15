import requests
from bs4 import BeautifulSoup
url=("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450")
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
res=soup.team1
print(soup.get_text())
