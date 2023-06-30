from django import forms
from custom.models import Help, Answer


# 포스트 폼 생성
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help  # Help 객체 생성
        fields = ['title', 'email', 'content', ]
        labels = {
            'title': '제목',
            'email': '이메일',
            'content': '내용',


        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '답변 내용',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['title'].initial = f"Re: {self.instance.question.title}"

    def save(self, commit=True):
        self.instance.title = f"Re: {self.instance.question.title}"
        return super().save(commit)


