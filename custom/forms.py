from django import forms
from custom.models import Help,Notice


# 포스트 폼 생성
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help  # Help 객체 생성
        fields = ['title', 'email', 'content', 'answer']
        labels = {
            'title': '제목',
            'email': '이메일',
            'content': '내용',
            'answer': '답변'

        }
        exclude = ['views']
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice # Notice 객체 생성
        fields = ['title',  'content' ]
        labels = {
            'title': '제목',
            'content': '내용',

        }



