from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(), label='邮箱')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].label = '用户名'
    #     self.fields['email'].label = '邮箱'
    #     self.fields['password1'].label = '密码'
    #     self.fields['password2'].label = '重复密码'