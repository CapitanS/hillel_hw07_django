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
schema = {
    "title": "Person",
    "type": "object",
    "required": [
      "name",
      "age",
      "date",
      "favorite_color",
      "gender",
      "location",
      "pets"
    ],
    "properties": {
      "name": {
        "type": "string",
        "description": "First and Last name",
        "minLength": 4,
        "default": "Jeremy Dorn"
      },
      "age": {
        "type": "integer",
        "default": 25,
        "minimum": 18,
        "maximum": 99
      },
      "favorite_color": {
        "type": "string",
        "format": "color",
        "title": "favorite color",
        "default": "#ffa500"
      },
      "gender": {
        "type": "string",
        "enum": [
          "male",
          "female",
          "other"
        ]
      },
      "date": {
        "type": "string",
        "format": "date",
        "options": {
          "flatpickr": {}
        }
      },
      "location": {
        "type": "object",
        "title": "Location",
        "properties": {
          "city": {
            "type": "string",
            "default": "San Francisco"
          },
          "state": {
            "type": "string",
            "default": "CA"
          },
          "citystate": {
            "type": "string",
            "description": "This is generated automatically from the previous two fields",
            "template": "{{city}}, {{state}}",
            "watch": {
              "city": "location.city",
              "state": "location.state"
            }
          }
        }
      },
      "pets": {
        "type": "array",
        "format": "table",
        "title": "Pets",
        "items": {
          "type": "object",
          "title": "Pet",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "cat",
                "dog",
                "bird",
                "reptile",
                "other"
              ],
              "default": "dog"
            },
            "name": {
              "type": "string"
            }
          }
        },
        "default": [
          {
            "type": "dog",
            "name": "Walter"
          }
        ]
      }
    }
  }
options = {
    "theme": "bootstrap4",
    "iconlib": "bootstrap4",
    "object_layout": "grid",
    "template": "default",
    "show_errors": "interaction",
    "required_by_default": 0,
    "no_additional_properties": 1,
    "display_required_only": 0,
    "remove_empty_properties": 0,
    "keep_oneof_values": 1,
    "ajax": 0,
    "ajaxCredentials": 0,
    "show_opt_in": 0,
    "disable_edit_json": 1,
    "disable_collapse": 1,
    "disable_properties": 1,
    "disable_array_add": 0,
    "disable_array_reorder": 0,
    "disable_array_delete": 0,
    "enable_array_copy": 0,
    "array_controls_top": 0,
    "disable_array_delete_all_rows": 0,
    "disable_array_delete_last_row": 0,
    "prompt_before_delete": 1,
    "lib_aceeditor": 0,
    "lib_autocomplete": 0,
    "lib_sceditor": 0,
    "lib_simplemde": 0,
    "lib_select2": 0,
    "lib_selectize": 0,
    "lib_choices": 0,
    "lib_flatpickr": 0,
    "lib_signaturepad": 0,
    "lib_mathjs": 0,
    "lib_cleavejs": 0,
    "lib_jodit": 0,
    "lib_jquery": 0,
    "lib_dompurify": 0
  }


class CustomForm(forms.Form):
    field = JSONSchemaField(schema=schema, options=options)


