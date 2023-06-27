from django.db import models

#카테고리모델
# class Category(models.Model):
#       name = models.CharField(max_length=50, unique=True) #카테고리 이름
#       slug = models.SlugField(max_length=200, unique=True, aloow_unicode=True)




class Goods(models.Model):
      objects = None
      name=models.CharField(max_length=100)        # 책 제목
      description = models.TextField()             # 책 내용 간단히
      image= models.ImageField(upload_to='goods/%Y/%m/%d',
                               null=True, blank=True)  # 책사진
      price = models.DecimalField(max_digits=10, decimal_places=2) #10자리숫자까지 만듨 있음 / 소수리 2까지  총 8자리 금액임
                                                                  # 금액 990,000


def __str__(self):
      return self.name
