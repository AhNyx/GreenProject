from django import forms

from community.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
