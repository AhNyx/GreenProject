from django import forms
from community.models import Post


class PostForm(forms.ModelForm):    # 폼 생성시 필요한 필드
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'attach']     # 카테고리, 파일첨부 추가
        labels = {  # 유효성 검사시 영어인 필드이름을 한글로 뜨도록
            'title': '제목',
            'content': '내용',
            'category': '분류',
            'attach': '첨부',
        }
