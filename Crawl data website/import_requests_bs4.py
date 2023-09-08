import requests
from bs4 import BeautifulSoup
response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")

soup = BeautifulSoup(response.content, "html.parser")

print("soup",soup)

titles = soup.findAll('div', class_='box-category-content')

print("titles",titles)

script = soup.findAll('script')

# print("script",script)

links = [link.find('a').attrs["href"] for link in titles]

print("links",links)