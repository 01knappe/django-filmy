from django.forms import ModelForm

from .models import *

class FilmModelForm(ModelForm):
    class Meta:
        model = Film
        fields = ['nazev', 'obsah', 'stat', 'rok', 'zanr', 'foto', 'rezie', 'scenar']