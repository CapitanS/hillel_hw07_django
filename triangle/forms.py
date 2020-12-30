from django import forms


class TriangleForm(forms.Form):
    adjacent_cathetus = forms.IntegerField(min_value=1,
                                           required=True,
                                           label='Adjacent cathetus',)
    opposing_cathetus = forms.IntegerField(min_value=1,
                                           required=True,
                                           label='Opposing cathetus',)
