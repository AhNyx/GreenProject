from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class Memo(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(null=True, blank=True)









# class Question(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_date = models.DateTimeField(auto_now_add=True)
#     modify_date = models.DateTimeField(null=True, blank=True)
#     views = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title


# class Category_product(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return f'/product/category/{self.slug}'
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=300)
#     category = models.ForeignKey(Category_product, null=True, blank=True, on_delete=models.SET_NULL)
#     image = models.ImageField(upload_to='project/image/')
#     price = models.IntegerField(default=0)
#     description = models.TextField()
#     pub_date = models.DateTimeField()
#
#     def __str__(self):
#         return self.name
#
#
# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
