from django import template
from django.db.models import FloatField, Sum
from orders.models import Customer

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
