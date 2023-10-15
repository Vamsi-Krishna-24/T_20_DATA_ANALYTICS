import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450")

soup = BeautifulSoup(req.content,"html.parser")
res= soup.title
print(soup.get_text())
print(res.get_text())