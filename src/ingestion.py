import requests
from pathlib import Path

PAGES = {
    "path_params": "https://fastapi.tiangolo.com/tutorial/path-params/",
    "query_params": "https://fastapi.tiangolo.com/tutorial/query-params/",
    "request_body": "https://fastapi.tiangolo.com/tutorial/body/",
    "dependencies": "https://fastapi.tiangolo.com/tutorial/dependencies/",
    "handling_errors": "https://fastapi.tiangolo.com/tutorial/handling-errors/",
    "security_first_steps": "https://fastapi.tiangolo.com/tutorial/security/first-steps/",
    "testing": "https://fastapi.tiangolo.com/tutorial/testing/",
}

for name, url in PAGES.items():
    response = requests.get(url)
    response.raise_for_status()

    output_path = Path(f"data/raw/{name}.html")
    output_path.write_text(response.text, encoding="utf-8")

    print(f"Saved {name} to {output_path}")
