from django.db import models

# Create your models here.

class Marks(models.Model):
    id=models.IntegerField(primary_key=True)
    image=models.ImageField(upload_to='images')