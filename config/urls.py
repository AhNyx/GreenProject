"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from greenbooks import views
from greenbooks.views import posting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path("gbook/mypage", views.mypage, name='mypage'),
    path("trade/", views.trade, name='trade'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('trade/<int:pk>', posting, name="posting"),
    path('common/', include('common.urls')),
]
