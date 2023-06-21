from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from community.forms import PostForm
from community.models import Post


def community(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'community/community.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'community/detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            form.save()
            return redirect('community:community')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'community/post_form.html', context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('community:community')
