from django.db import models


# Create your models here.
class Task(models.Model):
    #id
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
