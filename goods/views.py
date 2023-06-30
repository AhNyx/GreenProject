from django.shortcuts import render, get_object_or_404
from. models import *
from shopcart.forms import AddProductForm

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
    add_to_cart = AddProductForm(initial={'quantity': 1})
    context = {'goods': goods, 'add_to_cart': add_to_cart}
    return render(request, 'goods/gdetail.html', context)






