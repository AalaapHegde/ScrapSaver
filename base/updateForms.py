from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserInfo


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(max_length=100)

    class Meta:
        model = UserInfo
        fields = ("username", "email")

