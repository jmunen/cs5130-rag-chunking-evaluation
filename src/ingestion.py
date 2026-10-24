import requests
from pathlib import Path

URL = "https://fastapi.tiangolo.com/tutorial/path-params/"

response = requests.get(URL)
response.raise_for_status()

output_path = Path("data/raw/path_params.html")

output_path.write_text(response.text, encoding="utf-8")

print(f"Saved raw document to {output_path}")
