from django.utils import timezone

from custom.forms import HelpForm, NoticeForm
from .models import Help, Notice

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# ...
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# qnalist
def qnalist(request):
    return render(request, 'custom/qnalist.html')


def qnalist2(request):
    return render(request, 'custom/qnalist2.html')


def qnalist3(request):
    return render(request, 'custom/qnalist3.html')


# help
# helplist 목록
# help_list

from django.db.models import Q


@login_required(login_url='common:login')
def help_list(request):
    query = request.GET.get('query', '')  # 검색어 가져오기

    if request.user.is_superuser:
        help_list = Help.objects.all().order_by('-pub_date')  # 최신순으로 정렬
        if query:
            help_list = help_list.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(content__icontains=query)
            )
    else:
        help_list = Help.objects.filter(author=request.user).order_by('-pub_date')  # 최신순으로 정렬

        if query:
            help_list = help_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )

    paginator = Paginator(help_list, 10, orphans=1)  # 한 페이지에 10개의 게시물 표시
    page_number = request.GET.get('page')

    try:
        page_obj = (paginator.get_page(page_number))
    except EmptyPage:
        page_obj = paginator.get_page(1)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'custom/help_list.html', context)


# 글쓰기

@login_required(login_url='common:login')
def help_write(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            help = form.save(commit=False)
            help.author = request.user
            help.views = 0  # 'views' 필드에 값을 설정
            help.save()
            return redirect('custom:help_list')
    else:
        form = HelpForm()

    context = {'form': form}
    return render(request, 'custom/help_write.html', context)


# 질문상세 페이지

@login_required(login_url='common:login')
def help_view(request, help_id):
    help = get_object_or_404(Help, id=help_id)

    if request.method == "POST":
        if 'answer_submit' in request.POST:  # 답변 작성
            return redirect('custom:help_answer', help_id=help_id)
        elif 'post_submit' in request.POST:  # 게시글 작성
            return redirect('custom:help_write')

    context = {'help': help}
    return render(request, 'custom/help_view.html', context)


# 글 수정
@login_required(login_url='common:login')
def help_modify(request, help_id):
    help = get_object_or_404(Help, id=help_id, author=request.user)
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
    return render(request, 'custom/help_modify.html', context)


# 질문삭제
@login_required(login_url='common:login')
def help_delete(request, help_id):
    help = get_object_or_404(Help, pk=help_id)
    help.delete()
    return redirect('custom:help_list')


# 답변작성 페이지#####################################

# ...

def help_answer(request, help_id):
    help = get_object_or_404(Help, id=help_id)
    if request.method == "POST":
        answer_content = request.POST['answer_content']
        help.answer = answer_content
        help.answered = True  # 답변이 작성되었으므로 answered 값을 True로 설정
        help.save()
        return redirect('custom:help_view', help_id=help_id)
    else:
        return render(request, 'custom/help_answer.html', {'help': help})


# 답변 수정
@login_required(login_url='common:login')
def answer_modify(request, help_id):
    help = get_object_or_404(Help, id=help_id)

    if request.method == "POST":
        answer_content = request.POST['answer_content']
        help.answer = answer_content
        help.save()
        return redirect('custom:help_view', help_id=help_id)

    context = {'help': help}
    return render(request, 'custom/answer_modify.html', context)


# 답변삭제
@login_required(login_url='common:login')
def answer_delete(request, help_id):
    help = get_object_or_404(Help, pk=help_id)
    help.answer = ''  # 답변 필드를 빈 문자열로 업데이트
    help.answered = False  # answered 필드를 False로 업데이트
    help.save()
    return redirect('custom:help_view', help_id=help_id)


############################ 여기부터 공지사항 #########

@login_required(login_url='common:login')
def notice_list(request):
    query = request.GET.get('query', '')  # 검색어 가져오기

    notice_list = Notice.objects.all().order_by('-pub_date')
    if query:
        notice_list = notice_list.filter(
            title__icontains=query
        )

    paginator = Paginator(notice_list, 10, orphans=1)  # 한 페이지에 10개의 게시물 표시
    page_number = request.GET.get('page')

    try:
        notice_page = paginator.get_page(page_number)
    except (EmptyPage, PageNotAnInteger):
        notice_page = paginator.get_page(1)

    context = {
        'notice_page': notice_page,
        'query': query,
    }
    return render(request, 'custom/notice_list.html', context)


@login_required(login_url='common:login')
def notice_write(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.pub_date = timezone.now()
            notice.author = request.user
            notice.save()
            return redirect('custom:notice_list')
    else:
        form = NoticeForm()
    context = {'form': form}
    return render(request, 'custom/notice_write.html', context)


@login_required(login_url='common:login')
def notice_view(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)

    context = {'notice': notice}
    return render(request, 'custom/notice_view.html', context)


@login_required(login_url='common:login')
def notice_modify(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id, author=request.user)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.modify_date = timezone.now()
            notice.save()
            return redirect('custom:notice_view', notice_id=notice_id)
    else:
        form = NoticeForm(instance=notice)
    context = {'form': form}
    return render(request, 'custom/notice_modify.html', context)


@login_required(login_url='common:login')
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return redirect('custom:notice_list')
