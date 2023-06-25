from django.shortcuts import render
from.models import *

def gdetail(request):   # 상세페이지
    return render(request,'goods/gdetail.html')
def goods(request):   #구매하기 페이지
    return render(request,'goods/goods.html')



