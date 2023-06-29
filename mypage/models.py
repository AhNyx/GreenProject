from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Memo(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(null=True, blank=True)


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def update_views(self):
        self.views += 1
        self.save()
        return self.views
