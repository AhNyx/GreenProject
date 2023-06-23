
from django.contrib import admin
from django.urls import path,include
from greenbooks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("gbook/mypage", views.mypage),
    path('common/', include('common.urls')),
    path('community/', include('community.urls')),  # 연결
    path('custom/', include('custom.urls')),  # 연결
]
