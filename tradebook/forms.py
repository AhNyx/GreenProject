from django import forms

from tradebook.models import trade_post

# 포스트 폼 생성
class TradePostForm(forms.ModelForm):
    class Meta:
        model = trade_post
        fields = ['title',
                  'content',
                  'photo',
                  'status_choice',
                  ]