from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# from custom.forms import PostForm
# from custom.models import Post


# Create your views here.

def main(request):
    return render(request, 'custom/hi.html')

def qnalist(request):
    return render(request, 'custom/qnalist.html')
def qnalist2(request):
    return render(request, 'custom/qnalist2.html')
def qnalist3(request):
    return render(request, 'custom/qnalist3.html')

