from django.db import models

# Create your models here.
class image_upload(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
