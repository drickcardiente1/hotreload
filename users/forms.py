from enum import unique
from typing import Type
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from core.models import client, Types


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control col-md-8','id':'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control',}))
    class Meta:
        model = client
        fields = ('email', 'username','first_name','last_name', 'password1', 'password2', 'type')
        exclude = ['type']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.instance.type = "CLIENTS"
