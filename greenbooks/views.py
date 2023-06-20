from django.http import HttpResponse
from django.shortcuts import render

from greenbooks.models import Post


# Create your views here.
def index(request):
    return render(request, 'greenbooks/index.html')
    #return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")

def mypage(request):
    return render(request, 'greenbooks/mypage.html')

def trade(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'greenbooks/trade.html',{'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'greenbooks/posting.html', {'post':post})

