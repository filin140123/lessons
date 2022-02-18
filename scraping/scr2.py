from bs4 import BeautifulSoup
import requests


url = "http://quotes.toscrape.com/"
response = requests.get(url)
html_data = BeautifulSoup(response.text, features="lxml")
quotes = html_data.find_all(class_='quote')

for q in quotes:
    print(q.find(class_="text").get_text())
    print(q.find(class_="author").get_text())
    print("Tags:", q.find(class_="keywords")['content'])

