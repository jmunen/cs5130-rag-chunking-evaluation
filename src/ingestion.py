import requests
from bs4 import BeautifulSoup

URL = "https://fastapi.tiangolo.com/tutorial/path-params/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

article = soup.find("article")

print(article.get_text("\n", strip=True)[:2000])
