from bs4 import BeautifulSoup
import requests

url = "https://eastbaypioneers.com/sports/softball/roster"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
print(soup)