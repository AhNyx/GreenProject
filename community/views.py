from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from community.forms import PostForm
from community.models import Post


def community(request):     # post 리스트 페이지
    post_list = Post.objects.order_by('-create_date')   # 내림차순, 새로운 글이 맨위로
    context = {'post_list': post_list}                  # post 리스트 가져오기
    return render(request, 'community/community.html', context)     # 가져와서, 템플릿에 연결, 가져와야 할 것


def detail(request, post_id):   # post 상세보기(post_id 필요)
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    context = {'post': post}    # post 가져오기
    return render(request, 'community/detail.html', context)


@login_required(login_url='common:login')   # 로그인요구-로그인페이지연결
def post_create(request):   # post 생성하기
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():     # 폼이 유효하면
            post = form.save(commit=False)  # 폼 가저장 후
            post.writer = request.user      # writer를 user로 지정하고
            form.save()     # 폼 저장
            return redirect('community:community')  # 목록페이지로 넘어가기
    else:
        form = PostForm()   # get 방식으로 폼이 넘어왔을 때
    context = {'form': form}    # 빈 폼 가져오기
    return render(request, 'community/post_form.html', context)


@login_required(login_url='common:login')
def post_delete(request, post_id):  # post 삭제하기(post_id필요)
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    post.delete()                               # 삭제하기(장고명령어)
    return redirect('community:community')      # 목록페이지로 넘어가기
