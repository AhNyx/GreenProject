from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
