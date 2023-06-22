from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from community.models import Post


# Create your views here.
def mypage(request, user_id):
    member_list = User.objects.get(id=user_id)
    return render(request, 'mypage/mypage.html', {'member':member_list})

def memberinfo(request, user_id):
    member_info = User.objects.all()
    return render(request, 'mypage/memberinfo.html', {'member_info' : member_info})

def mypost(request):
    post = Post.objects.all().order_by('-create_date')
    post_list = post.filter(writer_id=request.user.id)

    context = {'post_list': post_list}
    return render(request, 'mypage/mypost.html', context)