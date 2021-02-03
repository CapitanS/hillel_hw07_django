from django import template
from django.core.cache import cache
from django.db.models import FloatField, Sum
from orders.models import Customer
import requests

from ..forms import CityModelForm


register = template.Library()


@register.filter
def currency(value, name='euro'):
    """
    Takes some value of price and return the value of price with currency
    :param value: Some price
    :param name: Name of currency
    :return: The value of price with currency
    """
    return f'{value}, {name}'


@register.simple_tag()
def total_price() -> float:
    """
    Returns the total price of all bought products of all customers
    :return:
    """
    return Customer.objects.all().annotate(order_price=Sum('product__price',
                                                           output_field=FloatField())
                                           ).aggregate(price=Sum('order_price')).get('price')


# Homework 17. Extra
@register.inclusion_tag('city_form.html')
def city_form(request):
    if request.method == 'POST':
        form = CityModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            text = f'You added {name}. Create new one.'
            form = CityModelForm()

    else:
        form = CityModelForm()
        text = 'Enter new city'

    context = {'form': form,
               'text': text}
    return context


@register.filter
def check_forbidden_words(word):
    """
    Takes some word and check if it in the list of the forbidden words
    """
    # Checks if list of forbidden words in the cache
    forbidden_words = cache.get('forbidden_words')
    if forbidden_words is None:
        # Gets the list of forbidden words
        forbidden_words = requests.get('https://random-word-api.herokuapp.com/word?number=100').text
        cache.set('forbidden_words', forbidden_words, 30)
    # Checks if our word in forbidden list of worlds
    if word in forbidden_words:
        word.replace(word, '*' * len(word))
    return word
