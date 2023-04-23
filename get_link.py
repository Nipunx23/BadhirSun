import requests
from bs4 import BeautifulSoup

word = "random"
url = "https://indiansignlanguage.org/"+word

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
yt_link = ''
for Links in soup.find_all("meta",content = True):
    print(Links['content'])
    if 'youtube' in Links:
        yt_link = Links
        break

print(yt_link)