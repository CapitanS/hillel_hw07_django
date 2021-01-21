import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django_jsonforms.forms import JSONSchemaField

from .models import Person


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


# Homework 9. ModelForm for Person
class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', ]
        labels = {'first_name': _('Persons first name'),
                  'last_name': _('Persons last name'),
                  'email': _('Persons email'), }
        help_texts = {'first_name': _('Enter first_name.'),
                      'last_name': _('Enter last_name.'),
                      'email': _('Enter email.'), }


# Test json forms
options = {
    "theme": "bootstrap4",
    "iconlib": "fontawesome5",
    "object_layout": "grid",
    "template": "default",
    "show_errors": "interaction",
    "no_additional_properties": 1,
    "keep_oneof_values": 1,
    "disable_edit_json": 1,
    "disable_properties": 1,
    "enable_array_copy": 1,
    "prompt_before_delete": 1,
    "startval": None
}

schema = 'schema/schema.json'


class CustomForm(forms.Form):

    field = JSONSchemaField(schema=schema, options=options)
