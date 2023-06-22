from django.contrib.auth.forms import UserCreationForm
from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username