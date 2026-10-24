from pathlib import Path
from bs4 import BeautifulSoup

input_path = Path("data/raw/path_params.html")
output_path = Path("data/processed/path_params.html")

html = input_path.read_text(encoding="utf-8")

soup = BeautifulSoup(html, "html.parser")

article = soup.find("article")

if article is None:
    raise ValueError("Could not find article content")

output_path.write_text(str(article), encoding="utf-8")

print(f"Saved processed document to {output_path}")
