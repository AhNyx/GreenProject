
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone

from common.forms import UserForm
from community.models import Post
from mypage.models import Memo


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
    post_list = post.filter(writer_id=request.user.id)
#    post_list = post.filter(liked_user=request.user.id)

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




# def question(request):
#     question_list = Question.objects.order_by('-create_date')
#
#     return render(request, 'mypage/question.html',{'question_list':question_list})
# def question_detail(request):
#     pass
#
# def question_post(request):
#
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.save()
#             return redirect('question/')
#     else:
#         form = MyForm()
#
#     return render(request, 'mypage/question_post.html',{'form': form})

#### def cart(request):
#     cart_list = Cart.objects.all()
#     context = {'cart_list':cart_list }
#     return render(request, 'mypage/cart.html', context)
#
# def add_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = get_object_or_404(Cart)
#      return render(request, 'mypage/cart.html')
