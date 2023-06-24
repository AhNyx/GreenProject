from django.shortcuts import render


def index(request):
    return render(request, 'greenbooks/index.html')


def mypage(request):
    return render(request, 'greenbooks/mypage.html')

