from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("http://quotes.toscrape.com/")
html_data = BeautifulSoup(response.text, features="lxml")
quotes = html_data.find_all(class_='quote')

with open('quotes.csv', 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Text', 'Author', 'Tags'])
    for q in quotes:
        text = q.find(class_="text").get_text()
        author = q.find(class_="author").get_text()
        tags = q.find(class_="keywords")['content']
        csv_writer.writerow([text, author, tags])
