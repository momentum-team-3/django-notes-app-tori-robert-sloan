from django.shortcuts import render
from .models import Notes

# Create your views here.
def notes_list(request):
    user = request.user
    notes = user.notes.all()
    return render(request, ' notes/list_notes.html', {'notes': notes})

def notes_detail(request, pk)
model = Notes

def add_note(request):
    model = Notes