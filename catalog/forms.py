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
    "title": "Объект",
    "type": "object",
    "required": [
      "name",
      "customer",
      "description",
      "location",
      "equipments",
      "mechanisms"
    ],
    "properties": {
      "name": {
        "type": "string",
        "title": "Название объекта",
        "description": "Как назвать?",
        "minLength": 4,
        "default": "Элеватор"
      },
      "customer": {
        "type": "string",
        "title": "Заказчик",
        "enum": [
          "АгроСоюз",
          "Kernel",
          "other"
        ]
      },
      "description": {
        "type": "string",
        "title": "Примечание",
        "format": "textarea"
      },
      "location": {
        "type": "object",
        "title": "Расположение",
        "format": "grid-strict",
        "properties": {
          "city": {
            "type": "string",
            "title": "Город/село",
            "options": {
              "grid_columns": 3
            },
            "default": "Волочийск"
          },
          "state": {
            "type": "string",
            "title": "Область",
            "enum": [
              "Хмельницкая обл.",
              "Харьковская обл.",
              "other"
            ],
            "options": {
              "grid_columns": 3
            },
            "default": "Хмельницкая обл."
          },
          "citystate": {
            "type": "string",
            "title": "Адрес",
            "description": "автоматически генерируется из двух",
            "template": "{{city}}, {{state}}",
            "watch": {
              "city": "location.city",
              "state": "location.state"
            }
          }
        }
      },
      "equipments": {
        "type": "object",
        "title": "Требования",
        "format": "grid-strict",
        "properties": {
          "provider": {
            "type": "string",
            "title": "Производитель",
            "options": {
              "grid_columns": 2
            },
            "enum": [
              "Schneider Electric",
              "Siemens",
              "other"
            ],
            "default": "Schneider Electric"
          },
          "rack": {
            "type": "string",
            "title": "Конструктив",
            "options": {
              "grid_columns": 2
            },
            "enum": [
              "Контур",
              "Rittal",
              "other"
            ],
            "default": "Контур"
          },
          "bus": {
            "type": "string",
            "title": "Шина",
            "options": {
              "grid_columns": 2
            },
            "enum": [
              "Медь",
              "Алюминий",
              "other"
            ],
            "default": "Медь"
          }
        }
      },
      "mechanisms": {
        "type": "array",
        "format": "tabs",
        "title": "Механизмы",
        "items": {
          "type": "object",
          "title": "Механизм",
          "format": "grid-strict",
          "required": [
            "type",
            "work",
            "power",
            "number"
          ],
          "properties": {
            "type": {
              "type": "string",
              "title": "Тип механизма",
              "options": {
                "grid_columns": 3
              },
              "enum": [
                "Нория",
                "Транспортер",
                "Клапан",
                "Задвижка",
                "other"
              ],
              "default": "Нория"
            },
            "name": {
              "type": "string",
              "title": "Название",
              "options": {
                "grid_columns": 2
              }
            },
            "work": {
              "type": "string",
              "title": "Тип пуска",
              "enum": [
                "Прямой",
                "ПП",
                "ПЧ",
                "Каскад",
                "Реверс",
                "other"
              ],
              "default": "Прямой"
            },
            "power": {
              "type": "number",
              "title": "Pн",
              "options": {
                "grid_columns": 2
              },
              "default": 15
            },
            "number": {
              "type": "number",
              "title": "Шт.",
              "options": {
                "grid_columns": 1
              },
              "default": 1
            },
            "di": {
              "type": "number",
              "title": "DI",
              "options": {
                "grid_columns": 1
              },
              "default": 6
            },
            "do": {
              "type": "number",
              "title": "DO",
              "options": {
                "grid_columns": 1
              },
              "default": 1
            },
            "ai": {
              "type": "number",
              "title": "AI",
              "options": {
                "grid_columns": 1
              },
              "default": 0
            },
            "ao": {
              "type": "number",
              "title": "AO",
              "options": {
                "grid_columns": 1
              },
              "default": 0
            },
            "interface": {
              "type": "string",
              "title": "Интерфейс",
              "enum": [
                "Modbus/RS-485",
                "Modbus/TCP-IP",
                "Profinet",
                "Profibus",
                "other"
              ],
              "default": "Modbus/RS-485"
            }
          }
        },
        "default": [
          {
            "type": "Нория",
            "work": "Прямой",
            "power": 15,
            "number": 1,
            "di": 6,
            "do": 1,
            "ai": 0,
            "ao": 0,
            "interface": "Modbus/RS-485"
          }
        ]
      }
    }
  }

options = {
    "theme": "bootstrap4",
    "iconlib": "fontawesome5",
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
    "disable_collapse": 0,
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


