from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    year = models.IntegerField(max_length=4, default=0)

#def get_image_path(instance, filename):
#    return os.path.join('photos', str(instance.id), filename)

class Shoe(models.Model):
    brand_model = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='photos', blank=True, null=True)
    description = models.TextField(default=0)
    #size = models.IntegerField(max_length=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return(self.brand_model)

class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True, blank=True, editable=False)
    body = models.TextField(default=0)
    publish_date = models.DateTimeField(default=timezone.now)

class Size(models.Model):
    shoeID = models.ForeignKey(Shoe, default='1')
    size = models.CharField(max_length=10, default='0')