import requests

url = "https://www.google.com/"
resp = requests.get(url)
print(f"Request to {url}. Status code is {resp.status_code}.")
