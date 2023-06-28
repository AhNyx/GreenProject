from django.shortcuts import render, get_object_or_404
from. models import *


# def gdetail(request, goods_id):   # 상세페이지
#     #goods = get_object_or_404(Goods, pk=goods_id) #하나의 객체를 가져오는 것
#     goods = Goods.objects.filter(pk=goods_id) #여러 개의 객체를 가져올때
#
#     context = {'goods': goods}
#     return render(request, 'goods/gdetail.html', context)
#
#
# def goods(request):   #구매하기 페이지
#     goods = Goods.objects.all()
#     context = {'goods': goods}
#     return render(request, 'goods/goods.html' ,context)


def goods_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    goods = Goods.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        goods = goods.filter(category=current_category)

    context = {
        'current_category': current_category,
        'categories': categories,
        'goods': goods
    }

    return render(request, 'goods/goods.html', context)

def goods_detail(request, id, goods_slug=None):
    goods = get_object_or_404(Goods, id=id, slug=goods_slug)
    #장바구니 추가해야함 add_to_cart
    context = {'goods': goods}
    return render(request, 'goods/gdetail.html', context)


