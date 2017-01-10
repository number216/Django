from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    year = models.IntegerField(max_length=4, default=0)

class Shoe(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(default=0)
    size = models.IntegerField(max_length=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
