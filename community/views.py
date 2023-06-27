import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST

from community.forms import PostForm
from community.models import Post, Category


# post 리스트 페이지
def community(request):
    post_list = Post.objects.order_by('-create_date')   # 내림차순, 새로운 글이 맨위로 가도록 설정
    categories = Category.objects.all()                 # 카테고리 가져오기
    today = date.today()                                # 작성일과 비교하기 위해 오늘날짜 준비
    page = request.GET.get('page', '1')                 # 페이지 처리 시작 - 페이지 가져오기
    paginator = Paginator(post_list, 10)                # 장고내장모듈을 통해 페이지처리. 10개가 1페이지
    page_obj = paginator.get_page(page)                 # 페이지 처리한 리스트
    context = {'post_list': page_obj, 'categories': categories, 'today': today}    # 보낼 준비
    return render(request, 'community/community.html', context)     # 가져와서, 템플릿에 연결, 가져와야 할 것


# post 상세보기(post_id 필요)
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    post.update_views                       # 조회수 증가
    categories = Category.objects.all()     # 카테고리 추가
    has_liked = request.user in post.liked_user.all() if request.user.is_authenticated else False
    context = {'post': post, 'categories': categories, 'has_liked': has_liked}    # 업데이트한 정보들 전달하기
    return render(request, 'community/detail_ck.html', context)


# post 생성하기
@login_required(login_url='common:login')   # 로그인요구-로그인페이지연결
def post_create(request):
    categories = Category.objects.all()     # 카테고리 가져오기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():     # 폼이 유효하면
            post = form.save(commit=False)  # 폼 가저장 후
            post.writer = request.user      # writer를 user로 지정하고
            form.save()     # 폼 저장
            return redirect('community:community')  # 목록페이지로 넘어가기
    else:   # get 방식으로 폼이 넘어왔을 때
        form = PostForm()   # 빈 폼 가져오기
    context = {'form': form, 'categories': categories}
    return render(request, 'community/post_form_ck.html', context)


# post 수정하기(post_id 필요)
@login_required(login_url='common:login')
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, writer=request.user)     # post_id를 pk로 함     # writer를 user로 지정
    categories = Category.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)    # post의 정보를 가져옴
        if form.is_valid():                     # 유효성검사 후
            post = form.save(commit=False)      # 가저장
            post.modify_date = timezone.now()   # 수정일을 지정
            post.save()                         # 찐저장
            return redirect('community:detail', post_id=post_id)    # 수정한 post 페이지로 넘어가기
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'categories':categories}    # 생성되었던 그대로의 post의 정보 form
    return render(request, 'community/post_form_ck.html', context)


# post 삭제하기(post_id 필요)
@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    post.delete()                               # 삭제하기(장고명령어)
    return redirect('community:community')      # 목록페이지로 넘어가기


# 카테고리 페이지 처리 메서드
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)  # 현재 카테고리 정보
    filter_list = Post.objects.filter(category=current_category)    # 현재 카테고리로 post 필터링
    post_list = filter_list.order_by('-create_date')    # 필터링된 post를 생성일 기준 내림차순 정렬
    categories = Category.objects.all()     # 전체 카테고리 정보
    page = request.GET.get('page', '1')     # 페이지 처리 시작 - 여기에서도 해주어야 start_index를 받아 올 수 있음
    paginator = Paginator(post_list, 10)    # 장고내장모듈을 통해 페이지처리. 10개가 1페이지
    page_obj = paginator.get_page(page)
    context = {'current_category': current_category, 'post_list': page_obj, 'categories': categories}
    return render(request, 'community/community.html', context)


@login_required(login_url='common:login')
@require_POST
def post_like(request):
    pk = request.POST.get('pk')
    post = get_object_or_404(Post, pk=pk)
    user = request.user                 # 유저: 현재 로그인한 유저
    if post.liked_user.filter(id=user.id).exists():  # 추천인 중에 유저가 존재할 때(이미 추천했을 때)
        post.liked_user.remove(user)    # liked_user에서 유저 제거
        liked = False
    else:   # 추천인 중에 유저가 없을 때(추천하지 않았을 때)
        post.liked_user.add(user)            # liked_user에 유저 추가
        liked = True
    context = {'likes_count': post.count_liked_user(), 'liked': liked}   # 해당 포스트 추천인 수 전달
    return HttpResponse(json.dumps(context), content_type='application/json')   # 정보를 json형태로 반환
