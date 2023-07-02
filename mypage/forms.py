from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from mypage.models import Question, CusComment


class MyForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'title', 'content', 'category'
        )
        label = [
            {'제목': 'title'},
            {'내용': 'content'},
            {'카테고리': 'category'}

        ]

class CusCommentForm(forms.ModelForm):

    class Meta:
        model = CusComment
        fields = ['content']
        labels = {'content' : '댓글 내용'}