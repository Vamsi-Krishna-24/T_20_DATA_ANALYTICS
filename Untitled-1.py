import pandas as pd
from bs4 import BeautifulSoup
import requests
url = ["https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450"]
webpage=requests.get(url)
web=webpage.content
soup=BeautifulSoup(web,"html,parser")
print(soup)