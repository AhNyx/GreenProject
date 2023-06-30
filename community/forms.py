from django import forms
from .models import Post, Reply


# 포스트폼
class PostForm(forms.ModelForm):    # 폼 생성시 필요한 필드
    class Meta:
        model = Post
        fields = ['title', 'category', 'description']     # 편집기 버전
        labels = {  # 유효성 검사시 영어인 필드이름을 한글로 뜨도록
            'title': '제목',
            'category': '분류',
            'description': '내용',
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply  # import
        fields = ['content']
        labels = {
            'content': '댓글 내용'
        }
