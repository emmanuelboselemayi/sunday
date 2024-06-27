from django.db import models

class Slider (models.Model):
    id = models.AutoField (primary_key=True)
    link = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="slides/")
    tagline = models.CharField(max_length=100, blank=True)
