from django.shortcuts import render
from .models import Notes

# Create your views here.
def notes_list(request):
    user = request.user
    notes = user.notes.all()
    return render(request, ' notes/list_notes.html', {'notes': notes})

def notes_detail()

def add_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('show_note', pk=note.pk)
    else:
        form=NoteForm()
        return render(request, 'notes/add_note.html',{'form':form})