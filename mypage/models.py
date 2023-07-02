from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

class Memo(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mypage:category_page', args=[self.slug])

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Question(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    @property
    def update_views(self):
        self.views += 1
        self.save()
        return self.views


class CusComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    post = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)