# library imports omitted
import requests
from bs4 import BeautifulSoup

number_of_pages = 1

url = 'https://quotes.toscrape.com'

while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='xml')
    if soup.find('li', class_='next'):
        link_next_page = soup.find('li', class_='next').a.get('href')
        url = f'https://quotes.toscrape.com{str(link_next_page)}'
        number_of_pages += 1
    else:
        break

print(number_of_pages)

number_of_quotes_at_once = 5

for page in range(1, number_of_pages+1):
    if number_of_quotes_at_once == 0:
        break
    else:
        r = requests.get(f'https://quotes.toscrape.com/page/{str(page)}/')
        soup = BeautifulSoup(r.content, features='xml')
        quotes = soup.findAll('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author_url_end = quote.find('small', class_='author').find_next_sibling('a').get('href')
            author_url = f'https://quotes.toscrape.com/{author_url_end}'

            number_of_quotes_at_once -= 1
            if number_of_quotes_at_once == 0:
                break
            if number_of_quotes_at_once != 0 and page == number_of_pages and quote == quotes[-1]:
                print(text)
