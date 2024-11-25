from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='wiki/images')
    element = models.CharField(max_length=40)
    path = models.CharField(max_length=40)
    rarity = models.BooleanField()
    url = models.URLField(blank=True)