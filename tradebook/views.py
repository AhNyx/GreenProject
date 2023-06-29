from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from tradebook.forms import TradePostForm
from tradebook.models import trade_post, tradeCategory


# Create your views here.
def tradebook_list(request):
    trade_list = trade_post.objects.order_by('-pub_date')
    trade_category = tradeCategory.objects.all()
    page = request.GET.get('page','1')
    paginator = Paginator(trade_list, 10)
    page_obj = paginator.get_page(page)
    context = {'trade_list':page_obj,'trade_category':trade_category}
    return render(request, 'tradebook/tradebook_list.html',context)

def trade_category_page(request, slug):
    current_category = tradeCategory.objects.get(slug=slug)  # 현재 카테고리 정보
    filter_list = trade_post.objects.filter(trade_category=current_category)    # 현재 카테고리로 post 필터링
    trade_list = filter_list.order_by('-pub_date')    # 필터링된 post를 생성일 기준 내림차순 정렬
    trade_category = tradeCategory.objects.all() # 전체 카테고리 정보
    page = request.GET.get('page', '1')
    paginator = Paginator(trade_list, 10)
    page_obj = paginator.get_page(page)
    context = {'current_category': current_category, 'trade_list': page_obj, 'trade_category': trade_category}
    return render(request, 'tradebook/tradebook_list.html', context)

def tradebook_post_detail(request, trade_post_detail_id):
    trade_post_detail = trade_post.objects.get(id=trade_post_detail_id)
    trade_category = tradeCategory.objects.all()
    context={'trade_post_detail':trade_post_detail,'trade_category':trade_category}
    return render(request, 'tradebook/tradebook_detail.html',context)


@login_required(login_url='common:login')
def tradebook_create(request):
    if request.method == "POST":
        form = TradePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_trade = form.save(commit=False)
            new_trade.writer = request.user
            new_trade.pub_date = timezone.now()
            new_trade.save()
            return redirect('tradebook:tradebook_list')
    else:
        form = TradePostForm()
    context = {'form': form}
    return render(request, 'tradebook/tradebook_form.html', context)

@login_required(login_url='common:login')
def trade_post_modify(request, trade_post_detail_id):
    # 수정을 위해 질문 가져옴
    modify_post = get_object_or_404(trade_post, pk=trade_post_detail_id)
    if request.method == "POST":
        form = TradePostForm(request.POST, instance=modify_post)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('tradebook:tradebook_detail', trade_post_detail_id=trade_post_detail_id)
    else:
        form = TradePostForm(instance=modify_post)
    context = {'form': form}
    return render(request, 'tradebook/tradebook_form.html', context)


@login_required(login_url='common:login')
def trade_post_delete(request, trade_post_detail_id):
    post = get_object_or_404(trade_post, pk=trade_post_detail_id)
    post.delete()
    return redirect('tradebook:tradebook_list')