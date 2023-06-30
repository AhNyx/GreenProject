from itertools import product

from django.contrib import admin

from mypage.models import Memo, Question, Category

# Register your models here.
admin.site.register(Memo)

admin.site.register(Question)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)