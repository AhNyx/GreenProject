from django.shortcuts import render

from goods.models import Goods


def index(request):
    goods = Goods.objects.all()

    context = {'goods':goods}
    return render(request, 'greenbooks/index.html', context)


def mypage(request):
    return render(request, 'greenbooks/mypage3.html')

