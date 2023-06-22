from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def mypage(request, user_id):
    member_list = User.objects.get(id=user_id)
    return render(request, 'mypage/mypage.html', {'member':member_list})

def memberinfo(request, user_id):
    member_info = User.objects.all()
    return render(request, 'mypage/memberinfo.html', {'member_info' : member_info})
