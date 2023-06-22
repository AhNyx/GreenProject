from django.contrib import admin
from django.urls import path,include
from . import views

app_name= 'mypage'


urlpatterns = [
    path("mypage/<int:user_id>/", views.mypage, name='mypage'),
    path("memberinfo/<int:user_id>/", views.memberinfo, name='memberinfo'),
]