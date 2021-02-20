from datetime import datetime, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .models import Contact, Person


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
class SendEmailModelForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3}), label='Enter the reminder')
    time_sending = forms.DateTimeField(required=True,
                                       widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
                                       label='Enter the time for reminding',
                                       input_formats={'%Y-%m-%D %H:%M'})
    email = forms.EmailField(required=True, label='Enter the email for sending the reminder')

    # Rewrite method 'clean_' for checking 'time_sending'
    def clean_time_sending(self):
        time = self.cleaned_data['time_sending']

        # Checking that the 'time_sending' is not in the past
        if time < timezone.now():
            raise forms.ValidationError(_("Invalid time - It can't be at the past!"))

        # Checking that the 'time_sending' is not more than 2 days in advance
        if time > timezone.now() + timedelta(days=2):
            raise forms.ValidationError(_("Invalid time - It can't be more than 2 days in advance!"))

        return time


# Homework 19.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['timestamp', ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
