from celery import Celery

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from celery.schedules import crontab
from .models import Authors, Quotes
from django.core.mail import send_mail

app = Celery('tasks')


# scheduled task execution
app.conf.beat_schedule = {
    # executes every 1 minute
    # 'scraping-task-one-min': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab()
    # }
    'scraping-every-10-seconds': {
        'task': 'tasks.scraping_quotes',
        'schedule': 10.0
    }
}


@app.task
def scraping_quotes():
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
                if not Quotes.objects.filter(text=text).exists():
                    author_of_quote = quote.find('small', class_='author').text
                    quote = Quotes.create(text=text, author=author_of_quote)
                    quote.save()
                    number_of_quotes_at_once -= 1
                    author_url_end = quote.find('small', class_='author').find_next_sibling('a').get('href')
                    author_url = f'https://quotes.toscrape.com/{author_url_end}'
                    author_r = requests.get(author_url)
                    author_soup = BeautifulSoup(author_r.content, features='xml')
                    author_block = author_soup.find('div', class_='author-details')
                    author_title = author_block.find('h3', class_='author-title').text
                    if not Authors.objects.filter(author_title=author_title).exists():
                        author_born_date = author_block.find('span', class_='author-born-date').text
                        author_born_location = author_block.find('span', class_='author-born-location').text
                        author_description = author_block.find('div', class_='author-description').text
                        author_detail = {
                            'author_title': author_title,
                            'author_born_date': author_born_date,
                            'author_born_location': author_born_location,
                            'author_description': author_description
                        }
                        author = Authors.objects.create(author_detail)
                        author.save()
                if number_of_quotes_at_once == 0:
                    break
                if number_of_quotes_at_once != 0 and page == number_of_pages and quote == quotes[-1]:
                    send_email_with_message()


@app.task
def send_email_with_message():
    send_mail(
        subject='About quotes',
        message='Fin de la comedie',
        from_email='my@email.com',
        recipient_list=['bla@bla.com'],
        fail_silently=False,
    )
