from django import forms
from firstApp.models import Movies
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'

