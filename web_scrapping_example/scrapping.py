# library imports omitted
import json

from bs4 import BeautifulSoup
import requests


# constant
url_hackernews = 'https://news.ycombinator.com/rss'


# scraping function
def hackernews_rss(url_hackernews: str):
    articles_list = []
    try:
        r = requests.get(url_hackernews)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text

            article = {
                'title': title,
                'link': link,
                'published': published,
            }
            articles_list.append(article)
        return save_function_loop(articles_list)
    except Exception as e:
        print('The scraping job failed. See exception: ')  # noqa: T001
        print(e)  # noqa: T001


def save_function_json(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


def save_function_loop(article_list):
    with open('articles.txt', 'w') as f:
        for a in article_list:
            f.write(str(a) + '\n')


print('Starting scraping')  # noqa: T001
hackernews_rss(url_hackernews)
print('Finished scraping')  # noqa: T001
