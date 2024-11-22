from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='wiki/images')
    url = models.URLField(blank=True)