from django.db import models

# Create your models here.
class Notes(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255)
    when_created = models.DateTimeField(auto_now_add=True)
    when_edited = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_names='notes')
    categories = models.
