from django.shortcuts import render
from tradebook.models import trade_post

# Create your views here.
def tradebook_list(request):
    trade_list = trade_post.objects.all()
    context = {'trade_list':trade_list}
    return render(request, 'tradebook/tradebook_list.html',context)