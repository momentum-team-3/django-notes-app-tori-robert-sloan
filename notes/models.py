from django.db.models import Model, TextField, CharField, DateTimeField

# Create your models here.
class Note(Model):
    note_text = TextField(max_length=1500, null=False, blank =False)
    note_title = CharField(max_length=255, null=False, blank=False)
    date_created = DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(user, on_delete=models.CASCADE, related_names='notes')
   
def __str__(self):
    return f"{self.note_title} {self.note_text}"