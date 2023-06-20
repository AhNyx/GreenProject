from django.shortcuts import render, redirect
from django.utils import timezone

from community.forms import PostForm
from community.models import Post


def community(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'community/community.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'community/detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            form.save()
            return redirect('community:community')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'community/post_form.html', context)
