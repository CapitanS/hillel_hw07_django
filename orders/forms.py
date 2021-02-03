from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import City


# Homework 17. ModelForm for City
class CityModelForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        labels = {'name': _('City'), }
        help_texts = {'name': _('Enter city.'), }
