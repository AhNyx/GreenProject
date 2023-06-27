from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# from mypage.models import Question
#
#
# class MyForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = (
#             'title', 'content'
#         )
#         label = [
#             {'제목': 'title'},
#             {'내용': 'content'},
#
#         ]
#
