from pathlib import Path
from bs4 import BeautifulSoup

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

for input_path in RAW_DIR.glob("*.html"):
    html = input_path.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")

    if article is None:
        print(f"Skipped {input_path.name}: no article found")
        continue

    for link in article.select("a.headerlink"):
        link.decompose()

    for image in article.find_all("img"):
        image.decompose()

    output_path = PROCESSED_DIR / input_path.name
    output_path.write_text(str(article), encoding="utf-8")

    print(f"Processed {input_path.name}")