from django.db import models
from datetime import datetime


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    year = models.TimeField(default=datetime.now().year)



    def __str__(self):
        return self.title
    