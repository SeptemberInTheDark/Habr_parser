import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/articles/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')


for article in soup.find_all('article'):
    text = article.text.lower()

    if any(keyword in text for keyword in KEYWORDS):
        title_tag = article.find('h2', class_="tm-title tm-title_h2")

        time = article.find('time')
        href = article.find('a', class_="tm-title__link")


        if title_tag and time and href:
            print(f"<{time.get_text()}> - <{title_tag.get_text()}> - <{href['href']}>")
