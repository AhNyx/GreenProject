from django import forms

from tradebook.models import Post

# 포스트 폼 생성
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'photo',
                  ]