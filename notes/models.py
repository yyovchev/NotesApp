from django.db import models


# Create your models here.
class Note(models.Model):
    key = models.CharField(max_length=50, primary_key=True)
    text = models.TextField()
