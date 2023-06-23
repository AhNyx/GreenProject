from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from tradebook.forms import TradePostForm
from tradebook.models import trade_post

# Create your views here.
def tradebook_list(request):
    trade_list = trade_post.objects.all()
    context = {'trade_list':trade_list}
    return render(request, 'tradebook/tradebook_list.html',context)

def tradebook_post_detail(request, trade_post_detail_id):
    trade_post_detail = trade_post.objects.get(id=trade_post_detail_id)
    context={'trade_post_detail':trade_post_detail}
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
def trade_post_delete(request, trade_post_detail_id):
    post = get_object_or_404(trade_post, pk=trade_post_detail_id)
    post.delete()
    return redirect('tradebook:tradebook_list')

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