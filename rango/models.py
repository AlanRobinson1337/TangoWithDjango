from django.db import models
from datetime import date

# Create your models here.


class News(models.Model):
    Headline = models.CharField(max_length=200)
    SotryDate = date.today()
    Plot = models.CharField(max_length=10000)
    def __str__(self):
        return self.Headline#, self.SotryDate, self.Plot