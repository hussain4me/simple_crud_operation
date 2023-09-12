from django.db import models
# from .models import U

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.email

class User_Profile(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    track = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


