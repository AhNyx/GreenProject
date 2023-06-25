from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.goods, name='goods'),  #상품구매페이지
    path('gdetail', views.gdetail, name='gdetail'), # 상품 상세페이지
]