from django.db import models
from user.models import User

# Create your models here.
class Note(models.Model):
    text = models.TextField(max_length=1500, null=False, blank =False)
    title = models.CharField(max_length=255, null=False, blank=False)
    when_created = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(user, on_delete=models.CASCADE, related_names='notes')
   
def __str__(self):
    return f"{self.title} {self.text}"