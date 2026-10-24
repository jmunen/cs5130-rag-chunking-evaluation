import requests

URL = "https://fastapi.tiangolo.com/tutorial/path-params/"

response = requests.get(URL)

print(response.status_code)
print(len(response.text))
