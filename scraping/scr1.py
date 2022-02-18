from bs4 import BeautifulSoup

with open("test.html", "r", encoding="utf-8") as myhtml:
    parsed = BeautifulSoup(myhtml, 'html.parser')
    # print(parsed)
    # print(type(parsed))
    print(parsed.body.h3.get_text())
    for i in parsed.find_all('li'):
        print(i.get_text())
