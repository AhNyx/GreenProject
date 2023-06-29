from django import forms
from custom.models import Help


# 포스트 폼 생성
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help  # Help 객체 생성
        fields = ['title', 'content', ]
        labels = {
            'title': '제목',
            'content': '내용',


        }



