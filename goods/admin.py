from django.contrib import admin
#모델을 관리자페이지에서 관리할 수 있도로 등록하는 곳
# Register your models here.

from .models import Goods
admin.site.register(Goods)