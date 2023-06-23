from django.urls import path

from . import views

app_name = 'tradebook'

urlpatterns = [
    path('', views.tradebook_list, name='tradebook_list'),
    path('<int:trade_post_detail_id>/', views.tradebook_post_detail, name='tradebook_detail'),
    path('create/', views.tradebook_create, name='tradebook_create'),
    path('delete/<int:trade_post_detail_id>', views.trade_post_delete, name='tradebook_delete'),
    path('modify/<int:trade_post_detail_id>', views.trade_post_modify, name='tradebook_modify'),
]