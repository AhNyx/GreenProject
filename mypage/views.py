from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from common.forms import UserForm
from community.models import Post
from mypage.forms import MyForm
from mypage.models import Question


# Create your views here.
def mypage(request, user_id):
    member_list = User.objects.get(id=user_id)
    return render(request, 'mypage/mypage.html', {'member':member_list})


def memberinfo(request, user_id):
    member_info = User.objects.get(id=user_id)

    return render(request, 'mypage/memberinfo.html', {'member_info': member_info})

def membermodify(request):
    return render(request,'mypage/mypage.html')

def mypost(request):
    post = Post.objects.all().order_by('-create_date')
    post_list = post.filter(writer_id=request.user.id)

    context = {'post_list': post_list}
    return render(request, 'mypage/mypost.html', context)

def question(request):
    question_list = Question.objects.order_by('-create_date')

    return render(request, 'mypage/question.html',{'question_list':question_list})


def question_post(request):

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question/')
    else:
        form = MyForm()

    return render(request, 'mypage/question_post.html',{'form': form})