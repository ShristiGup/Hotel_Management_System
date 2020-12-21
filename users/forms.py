from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email','mobile_no','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    mobile_no = forms.CharField(label='Mobile Number:',max_length=10)

    class Meta:
        model = CustomUser
        fields = ['username','email','mobile_no']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

