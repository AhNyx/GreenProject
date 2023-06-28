from django.contrib import admin
from . import models
from .models import Help
# 관리자 기능
admin.site.register(Help)
