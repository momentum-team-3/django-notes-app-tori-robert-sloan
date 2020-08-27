from django.shortcuts import render
from .models import Notes

# Create your views here.
class notes_list(request):
    user = request.user
    notes = user.notes.all()
    return render(request, ' notes/notes_list.html', {'notes': notes})

class notes_detail(request, pk):
    model = Notes

class add_note(request):
    model = Notes