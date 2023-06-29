from django.urls import path

from . import views

app_name = 'goods'


urlpatterns = [
    path('', views.goods_in_category, name='goods'),  # 구매페이지
    path('<slug:category_slug>/', views.goods_in_category, name='goods_in_category'),
    path('<int:id>/<goods_slug>/', views.goods_detail, name='goods_detail'),



    ]