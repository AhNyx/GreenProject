from django.shortcuts import render, get_object_or_404

from shopcart.forms import AddProductForm
from. models import *


def gdetail(request, goods_id):   # 상세페이지
    #goods = get_object_or_404(Goods, pk=goods_id) #하나의 객체를 가져오는 것
    goods = Goods.objects.filter(pk=goods_id) #여러 개의 객체를 가져올때
    add_to_cart = AddProductForm(initial={'quantity': 1})
    context = {'goods': goods, 'add_to_cart':add_to_cart}
    return render(request, 'goods/gdetail.html', context)


def goods(request):   #구매하기 페이지
    goods = Goods.objects.all()
    context = {'goods': goods}
    return render(request, 'goods/goods.html' ,context)



