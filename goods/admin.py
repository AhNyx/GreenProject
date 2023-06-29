from django.contrib import admin
#모델을 관리자페이지에서 관리할 수 있도로 등록하는 곳
from .models import Goods, Category


# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

#상품등록
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category','price', 'stock', 'available_display','available_order' ,
                     'created', 'updated']
    list_filter = ['available_display','available_order', 'created', 'updated','category']
    preserve_filters = {'slug' : ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']