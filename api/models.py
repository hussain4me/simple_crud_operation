from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    track = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)




