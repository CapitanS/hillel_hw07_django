from django import template
from django.db.models import FloatField, Sum
from orders.models import Customer

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
