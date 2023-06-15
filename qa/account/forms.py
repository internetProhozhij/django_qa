from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 

from .models import AccountModel


class AccountCreationForm(UserCreationForm):
    """
    Форма регистрации
    """
    username = forms.CharField(required=True,
                               label="",
                               widget=forms.TextInput(attrs={"class": "d-flex w-75 text-center mb-3",
                                                             "placeholder": "логин"}))
    password1 = forms.CharField(required=True, 
                               label="",
                               widget=forms.PasswordInput(attrs={"class": "d-felx w-75 text-center mb-3",
                                                                 "placeholder": "пароль"}))
    password2 = forms.CharField(required=True, 
                                label="",
                                widget=forms.PasswordInput(attrs={"class": "d-felx w-75 text-center mb-3",
                                                                  "placeholder": "повтор пароля"}))
    class Meta:
        model = AccountModel
        # Не указано поле с паролем потому,
        # что оно используется по умолчанию
        fields = ["username"]


class AccountAuthForm(AuthenticationForm):
    """
    Форма авторизации
    """
    username = forms.CharField(required=True,
                               label="",
                               widget=forms.TextInput(attrs={"class": "d-flex w-75 text-center mb-3",
                                                             "placeholder": "логин"}))
    password = forms.CharField(required=True, 
                               label="",
                               widget=forms.PasswordInput(attrs={"class": "d-felx w-75 text-center mb-3",
                                                                 "placeholder": "пароль"}))
    class Meta:
        model = AccountModel
        fields = ["username", "password"]
