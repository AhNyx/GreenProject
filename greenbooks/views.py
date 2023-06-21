from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'greenbooks/index.html')
    #return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")


def qna(request):
    return render(request, 'greenbooks/Q&A.html')
    #return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")

def mypage(request):
    return render(request, 'greenbooks/mypage2.html')

