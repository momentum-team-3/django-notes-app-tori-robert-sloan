from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Note

# Create your views here.
class NotesList(ListView):
    model = Note

class NotesDetail(DetailView):
    model = Note

class CreateNote(CreateView):
    model = Note
    fields = ["note_title", "note_text"] 
    template_name_suffix = "_create"   
    success_url = '/notes/'