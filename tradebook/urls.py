from django.urls import path

from . import views

app_name = 'tradebook'

urlpatterns = [
    path('', views.tradebook_list, name='tradebook_list'),
    path('t_category/<str:slug>/', views.trade_category_page, name='trade_category_page'),
    path('<int:trade_post_detail_id>/', views.tradebook_post_detail, name='tradebook_detail'),
    path('create/', views.tradebook_create, name='tradebook_create'),
    path('delete/<int:trade_post_detail_id>', views.trade_post_delete, name='tradebook_delete'),
    path('modify/<int:trade_post_detail_id>', views.trade_post_modify, name='tradebook_modify'),
    path('comment/create/<int:pk>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('comment/modify/<int:pk>/', views.comment_modify, name='comment_modify')
]