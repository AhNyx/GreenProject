from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from goods.models import Goods
from shopcart.cart import Cart
from shopcart.forms import AddProductForm


# Create your views here.
def detail(request):
    cart = Cart(request)

    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'],'id_update':True})

    context = {'cart':cart}
    return render(request, 'mypage/bag_detail.html', context)

@require_POST
# def add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Goods, id=product_id)
#
#     form = AddProductForm(request.POST) # 입력된 수량
#     if form.is_valid():
#         cd = form.cleaned_data  # 유효성검사가 끝난 데이터
#         cart.add(product=product,quantity=cd['quantity'], is_update=cd['is_update'])
#         return redirect('shopcart:detail')

def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)

    form = AddProductForm(request.POST)  # 입력된 수량
    if form.is_valid():
        cd = form.cleaned_data  # 유효성검사가 끝난 데이터
        cart.add(product=product, quantity=cd['quantity'], is_update=cd.get('is_update', False))
        return redirect('shopcart:detail')

    # 유효성 검사 실패 시에도 장바구니 페이지로 리다이렉트
    return redirect('shopcart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    cart.remove(product)
    return redirect('shopcart:detail')

