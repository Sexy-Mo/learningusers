from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserInfo
class UserForm (forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('password','email','username')
class UserInfoForm (forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=("portfoliosite",'profilepic')
