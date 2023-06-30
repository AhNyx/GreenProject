from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from custom.forms import HelpForm
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

#help
# helplist 목록



@login_required(login_url='common:login')
def help_list(request):
    if request.user.is_superuser:
        help_list = Help.objects.all().order_by('-pub_date')
    else:
        help_list = Help.objects.filter(
            Q(author=request.user) | Q(answers__author=request.user, answers__isnull=False)
        ).distinct().order_by('-pub_date')
    # # 게시물 번호 초기화
    # for i, help in enumerate(help_list):
    #     help.id = len(help_list) - i
    #     help.save()

    context = {'help_list': help_list}
    return render(request, 'custom/help_list.html', context)



# 질문상세 페이지
@login_required(login_url='common:login')
def help_view(request, help_id):
    help = get_object_or_404(Help, id=help_id)
    help.views += 1  # 조회수 증가
    help.save()  # 변경된 조회수 저장

    if request.method == "POST":
        if 'answer_submit' in request.POST:  # 답변 작성
            return redirect('custom:help_answer', help_id=help_id)
        elif 'post_submit' in request.POST:  # 게시글 작성
            return redirect('custom:help_write')

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
@login_required(login_url='common:login')
def help_modify(request, help_id):
    help = get_object_or_404(Help, id=help_id, author=request.user)
    if request.method == "POST":
        form = HelpForm(request.POST, instance=help)
        if form.is_valid():
            help = form.save(commit=False)
            help.modify_date = timezone.now()
            help.save()
            return redirect('custom:help_modify', help_id=help_id)
    else:
        form = HelpForm(instance=help)
    context = {'form': form} #저장되던 안되던 수정폼으로
    return render(request, 'custom/help_modify.html', context)

#질문삭제
@login_required(login_url='common:login') #로그인창으로 바록슛
def help_delete(request, help_id):
    #question = Question.objects.get(id=question_id)

    # 모델에서 데이터가있으면 가져오고 없으면 404페이지 오류 처리를함
    help = get_object_or_404(Help, pk=help_id)
    help.delete()
    return redirect('custom:help_list')


def help_notice(request):
    return render(request, 'custom/notice.html' )

# 답변상세 페이지
@login_required(login_url='common:login')
def help_aview(request, help_id):
    help = get_object_or_404(Help, id=help_id)
    help.views += 1  # 조회수 증가
    help.save()  # 변경된 조회수 저장

    if request.method == "POST":
        if 'answer_submit' in request.POST:  # 답변 작성
            return redirect('custom:help_answer', help_id=help_id)
        elif 'post_submit' in request.POST:  # 게시글 작성
            return redirect('custom:help_write')

    context = {'help': help}
    return render(request, 'custom/help_view.html', context)

# 답글 작성
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from custom.forms import HelpForm, AnswerForm
from custom.models import Help, Answer



@login_required(login_url='common:login')
def help_answer(request, help_id):
    parent_help = get_object_or_404(Help, id=help_id)

    if not request.user.is_superuser:
        return redirect('custom:help_view', help_id=help_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = parent_help
            answer.save()
            return redirect('custom:help_view', help_id=help_id)
    else:
        form = AnswerForm()

    context = {'form': form, 'help': parent_help}
    return render(request, 'custom/help_answer.html', context)