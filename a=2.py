import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.bikewale.com/royalenfield-bikes/")

soup = BeautifulSoup(req.content,"html.parser")
image=soup.findAll('div',class_="o-bqHweY o-bfyaNx o-brXWGL PhYMAu ")
print(image)
