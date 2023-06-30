from django.contrib import admin
from tradebook.models import trade_post,tradeCategory

admin.site.register(trade_post)

class TradeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(tradeCategory, TradeCategoryAdmin)
