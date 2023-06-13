from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import AccountCreationForm
from .forms import AccountAuthForm


SIGNIN_TEMPLATE = "account/signin.html"
SIGNUP_TEMPLATE = "account/signup.html"


def signup(request: HttpRequest) -> HttpResponse:
    """
    Представление страницы регистрации.
    """
    form = AccountCreationForm()

    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:signin")

    context = {"title": "Регистрация", 
               "form": form}
    return render(request, SIGNUP_TEMPLATE, context)


def signin(request: HttpRequest) -> HttpResponse:
    """
    Представление страницы авторизации.
    """
    form = AccountAuthForm()

    if request.method == "POST":
        form = AccountAuthForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user=user)
            return redirect('core:home')

    context = {"title": "Авторизация",
               "form": form}
    return render(request, SIGNIN_TEMPLATE, context)


def signout(request: HttpRequest) -> HttpResponse:
    """
    Реализация функции выхода из аккаунта.
    """
    logout(request)
    return redirect("core:home")

