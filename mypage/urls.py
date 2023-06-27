from django.contrib import admin
from django.urls import path,include
from . import views

app_name= 'mypage'


urlpatterns = [
    path("mypage/<int:user_id>/", views.mypage, name='mypage'),
    path("memberinfo/<int:user_id>/", views.memberinfo, name='memberinfo'),
    path("membermodify/", views.membermodify, name='membermodify'),
    path("mypost/", views.mypost, name='mypost'),
    path("memo_list/", views.memo_list, name='memo_list'),
    path("memo_create/", views.memo_create, name='memo_create'),
    path("memo_delete/<int:memo_id>", views.memo_delete, name='memo_delete'),
    # path("question/", views.question, name='question'),
    # path("question_post", views.question_post, name='question_post'),
]