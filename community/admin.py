from django.contrib import admin


from community.models import Post, Category

# 관리자 페이지에서 post 관리 가능하도록
admin.site.register(Post)


# 관리자 페이지에서 category 관리 가능하도록
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
