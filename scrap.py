import requests
import pandas as pd
from bs4 import BeautifulSoup
req = requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450")
soup=BeautifulSoup(req.content,"html.parser")
print(soup.getText())

