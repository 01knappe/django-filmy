from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from web.models import Film


def index(request):
    context = {
        'nadpis': 'Úvodní stránka',
        'obsah': 'Obsah stránky',
        'historie': 'Historie'
    }

    return render(request, template_name='index.html', context=context)


class FilmSeznamView(ListView):
    model = Film
    context_object_name = 'film_seznam'
    template_name = 'seznam.html'


class FilmDetailView(DetailView):
    model = Film
    context_object_name = 'film'
    template_name = 'detail.html'


class FilmCreate(CreateView):
    model = Film
    fields = ['nazev', 'obsah', 'stat', 'rok', 'zanr', 'foto', 'rezie', 'scenar']
    initial = {'rok': 2021}


class FilmUpdate(UpdateView):
    model = Film
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class FilmDelete(DeleteView):
    model = Film
    success_url = reverse_lazy('seznam')

