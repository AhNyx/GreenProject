from itertools import product

from django.contrib import admin

from mypage.models import Category_product, Product, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)

class CategoryProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category_product, CategoryProductAdmin)