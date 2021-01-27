# Homework_14. Celery Beat.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:
Scraping the site `https://quotes.toscrape.com` for quotes and their authors.

1. Add Authors, Quotes models with connections between them.
2. Create a periodic task that will add `5 NEW` quotes 
   and their authors with information every `ODD` hour.
3. When the quotes are over, send yourself an email that there are no more quotes.
   Use console mail sending.

---------------------
BASE_DIR: `/scraping/`

SCHEDULE_IN_FILE: `/django_example_project/celery.py`

TECHNOLOGY_STACK: `Celery`, `Django`, `RabbitMQ`

---------------------

### License

GPLv3
