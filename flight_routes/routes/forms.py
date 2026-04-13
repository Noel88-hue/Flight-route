from django import forms
from .models import AirportRoute

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['airport_code', 'position', 'duration']


class SearchForm(forms.Form):
    duration = forms.IntegerField()
    position = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField()