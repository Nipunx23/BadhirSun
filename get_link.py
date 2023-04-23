import requests
from bs4 import BeautifulSoup

word = "random"
url = "https://www.youtube.com/@isldictionary/search?query="+word

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
all_links = soup.find_all('a')
for links in all_links:
    print(links['href'])
