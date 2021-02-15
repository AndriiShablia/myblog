from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    article = models.TextField()
    slug=models.SlugField()
    pubdate = models.DateTimeField("Published Date")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.city
    
    def snipet(self):
        return self.article[:50]+'...'
