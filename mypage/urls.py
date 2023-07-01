from importlib.resources import path
from os import path

from django.contrib import admin
from django.urls import path,include
from . import views

app_name='mypage'


urlpatterns = [
    path("mypage/<int:user_id>/", views.mypage, name='mypage'),
    path("memberinfo/<int:user_id>/", views.memberinfo, name='memberinfo'),
    path("membermodify/", views.membermodify, name='membermodify'),
    path("mypost/", views.mypost, name='mypost'),
    path("memo_list/", views.memo_list, name='memo_list'),
    path("memo_create/", views.memo_create, name='memo_create'),
    path("memo_delete/<int:memo_id>/", views.memo_delete, name='memo_delete'),
    path("question/", views.question, name='question'),
    path("question/<int:question_id>/", views.question_detail,name='question_read'),
    path("question_post/", views.question_post, name='question_post'),
    path("question_modify/<int:question_id>/", views.question_modify, name='question_modify'),
    path("question_delete/<int:question_id>/", views.question_delete, name='question_delete'),
    path('category/<str:slug>/', views.category_page,name='category_page'),
    path('comment/create/<int:pk>/',views.comment_create,name='comment_create'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('comment/modify/<int:pk>/', views.comment_modify, name='comment_modify'),
]