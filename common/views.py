
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from common.models import People


# Create your views here.

def register(request):
    data = {}
    if request.method == "GET":
        return render(request, 'common/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password_ck = request.POST.get('password_ck', None)
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)


        if not (username and password and password_ck and name and phone and address):
            data = "입력하지 않은 란이 있습니다"

        elif password != password_ck:
            data = '비밀번호가 같지않습니다.'

        else:
            people = People(
                username = username,
                password = make_password(password),
                name = name,
                phone = phone,
                address = address
            )
            people.save()
            user = authenticate(username=username, password=password)  # 사용자 인증
            login(request, user)
            return redirect('/')
    return render(request, 'common/signup.html', {'data':data})
