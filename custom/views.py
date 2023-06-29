from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from custom.form import HelpForm
from .models import Help


# from custom.forms import PostForm
# from custom.models import Post


# qnalist
def qnalist(request):
    return render(request, 'custom/qnalist.html')
def qnalist2(request):
    return render(request, 'custom/qnalist2.html')
def qnalist3(request):
    return render(request, 'custom/qnalist3.html')

# helplist 목록
@login_required(login_url='common:login')
def help_list(request):
    if request.user.is_superuser:
        help_list = Help.objects.order_by('-pub_date')
    else:
        help_list = Help.objects.filter(author=request.user).order_by('-pub_date')

    context = {'help_list': help_list}
    return render(request, 'custom/help_list.html', context)

# 상세 페이지
@login_required(login_url='common:login')
def help_view(request, help_id):
    help = get_object_or_404(Help, id=help_id)
    help.views += 1  # 조회수 증가
    help.save()  # 변경된 조회수 저장  # 조회수 증가
    # help_view = Help.objects.get(id=help_id)

    context = {'help': help}
    return render(request, 'custom/help_view.html', context)

# 글쓰기

@login_required(login_url='common:login')
def help_write(request):
    if request.method == "POST":
        form = HelpForm(request.POST, request.FILES) #(일반속성, 파일)
        if form.is_valid(): #유효하다면
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # 현재 시간
            post.author = request.user  #로그인한 사람이 글쓴이임
            post.save()
            return redirect('custom:help_list')
    else:
        form = HelpForm()  #비어있는 폼
    context = {'form': form}
    return render(request, 'custom/help_write.html', context)

# 글 수정
def help_modify(request, help_id):
    help = get_object_or_404(Help, pk=help_id, author=request.user)
    if request.method == "POST":
        form = HelpForm(request.POST, instance=help)
        if form.is_valid():
            help = form.save(commit=False)
            help.modify_date = timezone.now()
            help.save()
            return redirect('custom:help_view', help_id=help_id)
    else:
        form = HelpForm(instance=help)
    context = {'form': form}
    return render(request, 'custom/help_write.html', context)


def help_notice(request):
    return render(request, 'custom/notice.html' )