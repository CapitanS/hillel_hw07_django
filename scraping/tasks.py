from bs4 import BeautifulSoup
from celery import shared_task
from django.core.mail import send_mail
import lxml
import requests


from .models import Authors, Quotes


@shared_task()
def scraping_quotes():
    """
    Function for scraping 'https://quotes.toscrape.com' on purpose to add in database new quotes and their authors.
    5 quotes per once.
    If new quotes aren't - it will be sending message to email. Call the send_email_with_message().
    :return:
    """
    # Some constants
    # URL for scraping
    url = 'https://quotes.toscrape.com'
    # Number of quotes at once
    number_of_quotes_at_once = 5
    # Number of page to start
    current_number_of_page = 1

    # Scraping pages
    while number_of_quotes_at_once != 0:
        r = requests.get(f'{url}/page/{str(current_number_of_page)}/')
        soup = BeautifulSoup(r.content, features='xml')
        quotes = soup.findAll('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text

            # Check if quote exist in our base.
            if not Quotes.objects.filter(text=text).exists():
                # Get the author of quote url
                author_url_end = quote.find('small', class_='author').find_next_sibling('a').get('href')
                author_url = f'{url}/{author_url_end}'

                author_r = requests.get(author_url)
                author_soup = BeautifulSoup(author_r.content, features='xml')
                author_block = author_soup.find('div', class_='author-details')

                # Get the author of quote title
                author_title = author_block.find('h3', class_='author-title').text

                # Check if author exist in our base.
                if not Authors.objects.filter(author_title=author_title).exists():
                    author_born_date = author_block.find('span', class_='author-born-date').text
                    author_born_location = author_block.find('span', class_='author-born-location').text
                    author_description = author_block.find('div', class_='author-description').text

                    # Add author in our base and save.
                    author = Authors.objects.create(author_title=author_title,
                                                    author_born_date=author_born_date,
                                                    author_born_location=author_born_location,
                                                    author_description=author_description)
                else:
                    author = Authors.objects.get(author_title=author_title)

                # Add quote in our base and save.
                quote = Quotes.objects.create(text=text, author=author)
                quote.save()

                # Decrease number of quotes at once by 1
                number_of_quotes_at_once -= 1

            # If there are no new quotes - send message
            if number_of_quotes_at_once != 0 and quote == quotes[-1] and not soup.find('li', class_='next'):
                send_email_with_message.delay()
                number_of_quotes_at_once = 0
                break

        current_number_of_page += 1


@shared_task()
def send_email_with_message():
    """
    Send the message about absence of new quotes.
    :return:
    """
    send_mail(
        subject='About quotes',
        message='Fin de la comedie',
        from_email='admin@admin.com',
        recipient_list=['bla@bla.com']
    )
