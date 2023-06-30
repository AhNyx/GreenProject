from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class tradeCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)     # 카테고리 이름 - 중복불가
    slug = models.SlugField(max_length=200, null=True ,unique=True, allow_unicode=True)    # url과 연동, 중복불가, 유니코드(한글포함)가능
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return f'/community/category/{self.slug}'   # 카테고리에 해당하는 절대 slug형 url을 반환
        return reverse('tradebook:trade_category_page', args=[self.slug])     # reverse 방식으로 변경
    class Meta:     # 중첩모델
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # 복수형 단어 직접 지정

class trade_post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField('내용',blank=True,null=True)
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.PositiveIntegerField(default=0)
    trade_category = models.ForeignKey(tradeCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        return self.hit

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    post = models.ForeignKey(trade_post, null=True,blank=True,on_delete=models.CASCADE)


