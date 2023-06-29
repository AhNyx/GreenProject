from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse


#카테고리모델
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True) # 카테고리 이름 ex:만화책,소설,에세이
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True,
                               unique=True)  # 한글

    class Meta:
        ordering = ['name'] # 카테고리 이름으로 정렬!
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self): #페이지경로
        return reverse('goods:goods_in_category', args=[self.slug])

class Goods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='goods')
    name = models.CharField(max_length=100, db_index=True)        # 책 제목
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    writer = models.CharField(max_length=100, db_index=True)     # 작가
    image = models.ImageField(upload_to='goods/%Y/%m/%d',) # 책이미지
    description = models.TextField(blank=True)     # 상세내용
    price = models.DecimalField(max_digits=10, decimal_places=2) #10자리숫자까지 만듨 있음 / 소수리 2까지  총 8자리 금액임
    stock = models.PositiveIntegerField()   # 재고 (정수로)
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)
    created = models.DateTimeField(auto_now_add=True)  # 상품등록일
    updated = models.DateTimeField(auto_now=True)       # 수정일

    class Meta: #데이터베이스에 인덱스를 생성
        ordering = ['-created', '-updated']  # 내림차순 정렬
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self): # 상세페이지 경로
        return reverse('goods:goods_detail', args=[self.id,self.slug])
