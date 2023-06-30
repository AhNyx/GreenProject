from django import forms

from tradebook.models import trade_post, Comment


# 포스트 폼 생성
class TradePostForm(forms.ModelForm):
    class Meta:
        model = trade_post
        fields = [
            'title',
            'content',
            'trade_category',
                  ]
        labels = {
            'title': '',
            'content': '',
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content':'댓글 내용'}