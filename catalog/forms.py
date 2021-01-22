import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Person, SendEmail


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


# Homework 13. ModelForm for Person
class SendEmailModelForm(ModelForm):
    class Meta:
        model = SendEmail
        fields = ['text', 'time_sending', 'email', ]
        labels = {'text': _('Reminder'),
                  'time_sending': _('Time'),
                  'email': _('Email'),
                  }
        help_texts = {'text': _('Your reminder.'),
                      'time_sending': _('When remind?'),
                      'email': _('Email for reminding.'),
                      }
        widgets = {
            'time_sending': forms.DateTimeInput(format=('%Y-%m-%d %H:%M:%S')),
        }
