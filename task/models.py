from django.db import models
from django.forms import ModelForm

# Create your models here.

class Task(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('description')

