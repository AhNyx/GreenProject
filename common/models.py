from django.db import models

# Create your models here.
class Member(models.Model):
    userid = models.CharField(max_length=30, primary_key=True)
    userpw = models.IntegerField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=30)
    address = models.TextField()
    regdate = models.DateTimeField()