from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Note

# Create your views here.
class notes_list(ListView):
    model = Note

class Notes_Detail(DetailView):
    model = Note

