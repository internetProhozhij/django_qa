from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse

from . import utils


HOME_TEMPLATE = "core/home.html"
QUESTION_TEMPLATE = "core/question.html"
ANSWER_TEMPLATE = "core/answer.html"


def home(request: HttpRequest) -> HttpResponse:
    """
    Представление домашней страницы.
    """
    # Кажется, что реализация удаления вопроса выполнена максимально
    # костыльно, но имеем то, что имеем.
    # При удалении вопроса в шаблоне HOME_TEMPLATE формируется url
    # следующего вида: domain/?del=<question_id>
    # Чтобы удалять вопросы мог только администратор, нужно проверять
    # авторизован ли пользователь и есть ли у него поле .is_god
    if request.GET.get("del", None) and utils.home.is_god(request.user):
        utils.home.delete_question(request.GET.get("del"))

    context = utils.home.build_context(request)
    return render(request, HOME_TEMPLATE, context)


def question(request: HttpRequest) -> HttpResponse:
    """
    Представление страницы создания вопроса.
    """
    context = utils.question.build_context(request)
    if request.method == "POST":
        # Когда пользователь публикует вопрос, его, наверно, стоит
        # перекинуть на главную страницу.
        return redirect("core:home")
    return render(request, QUESTION_TEMPLATE, context)


def answer(request: HttpRequest, qid: str=None) -> HttpResponse:
    """
    Представление страницы ответов.
    """
    context = utils.answer.build_context(request, qid, request.GET.get("answer", None))
    return render(request, ANSWER_TEMPLATE, context)

