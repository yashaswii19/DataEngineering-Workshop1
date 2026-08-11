import requests
from bs4 import BeautifulSoup

url = "https://sadia-shahzadi.github.io/Portfolio-Website.github.io/"

res = requests.get(url)

print("Status:", res.status_code)

soup = BeautifulSoup(res.content, "html.parser")

print("Title:", soup.title.text)

print("\nHeadings:")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.text.strip())
