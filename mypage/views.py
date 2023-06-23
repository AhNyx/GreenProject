from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from common.forms import UserForm
from community.models import Post
from mypage.forms import CustomUserChangeForm


# Create your views here.
def mypage(request, user_id):
    member_list = User.objects.get(id=user_id)
    return render(request, 'mypage/mypage.html', {'member':member_list})


def memberinfo(request, user_id):

    member_info = User.objects.get(id=user_id)

    if request.method == "POST":
        modify = get_object_or_404(User, id=user_id)
        print(modify)
        form = CustomUserChangeForm(request.POST, instance=modify)
        if form.is_valid():
            print('헬로')
            form.save()

    return render(request, 'mypage/memberinfo.html', {'member_info': member_info})


def mypost(request):
    post = Post.objects.all().order_by('-create_date')
    post_list = post.filter(writer_id=request.user.id)

    context = {'post_list': post_list}
    return render(request, 'mypage/mypost.html', context)