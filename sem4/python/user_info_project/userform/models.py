from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    agreement = models.BooleanField()
