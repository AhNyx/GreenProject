import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from community.forms import PostForm, ReplyForm
from community.models import Post, Category, Reply


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


# 카테고리별 post 리스트 페이지
def category_list(request, slug):
    current_category = Category.objects.get(slug=slug)  # 현재 카테 정보 가져오기
    filter_list = Post.objects.filter(category=current_category)    # 현재 카테로 post 필터링
    post_list = filter_list.order_by('-create_date')    # 필터링된 post를 생성일 기준 내림차순 정렬
    categories = Category.objects.all()     # 전체 카테고리 정보
    today = date.today()                    # 작성일과 비교하기 위해 오늘날짜 준비
    page = request.GET.get('page', '1')     # 페이지 처리 - 여기에서도 해주어야 start_index를 받아 올 수 있음
    paginator = Paginator(post_list, 10)    # 1페이지당 10개씩 페이지처리
    page_obj = paginator.get_page(page)     # 페이지 처리한 리스트
    context = {'post_list': page_obj, 'categories': categories, 'today': today,
               # current_category는 리스트 사이드바에 카테적용
               'current_category': current_category,
               'cate_url': reverse('community:cate_post_create', args=[slug])}     # 카테글쓰기 링크처리(이렇게 안하면 오류남)
    return render(request, 'community/community.html', context)


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


# 카테고리별 리스트에서 post 생성하기
@login_required(login_url='common:login')
def cate_post_create(request, slug):
    categories = Category.objects.all()     # 셀렉트 옵션에서 고를 모든 카테고리 정보 가져오기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('community:cate_list', slug=slug)   # 해당 카테고리 리스트로
    else:
        form = PostForm()
    current_category = get_object_or_404(Category, slug=slug)   # 슬러그로 현재 카테 정보 가져오기
    context = {'form': form, 'categories': categories, 'current_category': current_category}
    return render(request, 'community/post_form_ck.html', context)


# post 수정하기(post_id 필요)
@login_required(login_url='common:login')
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함     # writer를 user로 지정->굳이 안하고 유지해도 될 듯
    categories = Category.objects.all()     # 카테고리 전체 정보 가져오기
    current_category = post.category        # post_id로 알아낸 포스트 카테고리
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)    # post의 정보를 가져옴
        if form.is_valid():                     # 유효성검사 후
            post = form.save(commit=False)      # 가저장
            post.modify_date = timezone.now()   # 수정일을 지정
            post.save()                         # 찐저장
            return redirect('community:detail', post_id=post_id)    # 수정한 post 페이지로 넘어가기
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'categories': categories, 'current_category': current_category}
    return render(request, 'community/detail_ck.html', context)


# post 삭제하기(post_id 필요)
@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    post.delete()                               # 삭제하기(장고명령어)
    return redirect('community:community')      # 목록페이지로 넘어가기


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
        post.liked_user.add(user)       # liked_user에 유저 추가
        liked = True
    context = {'likes_count': post.count_liked_user(), 'liked': liked}   # 해당 포스트 추천인 수 전달
    return HttpResponse(json.dumps(context), content_type='application/json')   # 정보를 json형태로 반환


# 댓글 등록
@login_required(login_url='common:login')
def reply_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id로 post 정보 갖고오기
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)     # content만 저장
            reply.writer = request.user         # 댓쓴이는 현재 로그인한 사용자
            reply.post = post  # 외래키 생성(post와 연결)
            form.save()
            return redirect('community:detail', post_id=post.id)
    else:
        form = ReplyForm()     # 빈 폼 생성
    context = {'form': form}
    return render(request, 'community/reply_form.html', context)


# 댓글 삭제
@login_required(login_url='common:login')
def reply_delete(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)   # reply_id로 댓글정보 가져오기
    reply.delete()
    return redirect('community:detail', post_id=reply.post.id)  # 댓글과 연결된 post 페이지로


# 댓글 수정- 수업중에 구현 x
def reply_edit(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)   # reply_id로 댓글정보 가져오기
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)  # 댓글 정보가 있는 폼
        if form.is_valid():
            reply = form.save(commit=False)
            reply.modify_date = timezone.now()  # 수정일 지정
            reply.save()
            return redirect('community:detail', post_id=reply.post.id)
    else:
        form = ReplyForm(instance=reply)
    context = {'form': form, 'reply': reply}
    return render(request, 'community/reply_form.html', context)
