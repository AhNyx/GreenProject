
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'common/signup.html', context)