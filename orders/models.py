from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Homework 11. Relations.
class City(models.Model):
    """
    Represents model of city of customer and supplier
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents model of product
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """
    Represents model of supplier
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE, verbose_name='city of supplier')

    def __str__(self):
        """String for representing the supplier object."""
        return f'{self.last_name}, {self.first_name}'


class Customer(models.Model):
    """
    Represents model of customer
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='city of customer')
    product = models.ManyToManyField(Product, verbose_name='products of customer')

    def __str__(self):
        """String for representing the customer object."""
        return f'{self.last_name}, {self.first_name}'
