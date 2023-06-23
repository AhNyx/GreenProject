from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' ,'last_name', 'email']