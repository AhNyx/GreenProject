
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.utils.datetime_safe import date

from common.forms import UserForm
from community.models import Post
from mypage.forms import MyForm
from mypage.models import Memo, Question, Category


# Create your views here.
def mypage(request, user_id):
    member_list = User.objects.get(id=user_id)
    return render(request, 'mypage/mypage.html', {'member':member_list})


def memberinfo(request, user_id):
    member_info = User.objects.get(id=user_id)

    return render(request, 'mypage/memberinfo.html', {'member_info': member_info})

def membermodify(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('/')
    return render(request,'mypage/memberinfo.html',)

def mypost(request):
    post = Post.objects.all().order_by('-create_date')
#    post_list = post.filter(writer_id=request.user.id)
    post_list = post.filter(liked_user=request.user.id)

    context = {'post_list': post_list}
    return render(request, 'mypage/mypost.html', context)

def memo_list(request):
    memo_list = Memo.objects.all().order_by('-created_date')
    context = {'memo_list':memo_list}
    return render(request, 'mypage/memo_list.html', context)


def memo_delete(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.delete()
    return redirect('mypage:memo_list')

def memo_create(request):
    content = request.POST.get('content')
    create_date = timezone.now()
    memo = Memo(content=content, created_date=create_date)
    memo.save()

    return redirect('mypage:memo_list')




def question(request):
    question_list = Question.objects.order_by('-create_date')


    categories = Category.objects.all()

    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    today = date.today()
    context = {'question_list':page_obj, 'today':today, 'categories':categories}
    return render(request, 'mypage/question.html', context)
def question_detail(request, question_id):

    board = get_object_or_404(Question, id=question_id)
    board.update_views
    categories = Category.objects.all()
    context = {'list':board, 'categories':categories}
    return render(request, 'mypage/question_detail.html', context)

def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)
    post_list = Question.objects.filter(category=current_category)
    post_list = post_list.order_by('-create_date')
    categories = Category.objects.all()
    context = {
        'current_category' : current_category,
        'question_list': post_list,
        'categories': categories
    }
    return render(request, 'mypage/question.html', context)
def question_post(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('mypage:question')
    else:
        form = MyForm()

    return render(request, 'mypage/question_post.html',{'form': form, 'categories': categories} )

@login_required(login_url='/')
def question_modify(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    categories = Category.objects.all()
    if request.method == "POST":
        form = MyForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('mypage:question_read', question_id = question_id)
    else:
        form = MyForm(instance=question)
    context = {'form':form, 'categories': categories}
    return render(request, 'mypage/question_post.html', context)

@login_required(login_url='/')
def question_delete(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect('mypage:question')