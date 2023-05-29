import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/news')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    news_headlines = soup.select('.gs-c-promo-heading__title')

    for headline in news_headlines:
        print(headline.text.strip())
else:
    print('Ошибка при получении страницы:', response.status_code)
