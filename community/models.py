from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=40)
    created_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
