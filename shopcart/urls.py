from django.urls import path

from shopcart import views

app_name = 'shopcart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/<int:product_id>/', views.add, name='product_add'),
    path('remove/<int:product_id>/', views.remove, name='product_remove')
]