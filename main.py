import requests
from bs4 import BeautifulSoup

url = 'https://qz.com/africa/latest'

req = requests.get(url)

soup1 = BeautifulSoup(req.content, 'html.parser')

found_title = soup1.find_all("div", {"class":'esSAQ _8S5gh'})

found_link = soup1.find_all("a", {"class":'eBKpx'})
for i in range(len(found_title)):
    print("Title:" + found_title[i].text)
    print("Link:" + "https://qz.com" + found_link[i]["href"])
