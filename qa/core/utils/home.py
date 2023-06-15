from django.http import HttpRequest

from core.models import QuestionModel
from core.forms import SearchForm
from account.models import AccountModel


def is_god(user: AccountModel) -> bool:
    """
    Является ли опльзователь админом
    """
    try:
        return user.is_god
    except:
        return False


def get_username(request: HttpRequest) -> str:
    """
    Получение имени пользователя.
    """
    if not request.user:
        return "" 
    return request.user.username


def get_questions(theme: str="all", header: str="") -> list:
    """
    Получение вопрсов по заданной теме и заголовку.
    """
    if theme == "all":
        objs = QuestionModel.objects.all()
    else:
        objs = QuestionModel.objects.filter(theme=theme)
     
    return list(objs.filter(header__icontains=header))


def delete_question(qid: str) -> None:
    """
    Удаление вопроса.
    """
    try:
        question_obj = QuestionModel.objects.get(qid=qid)
        question_obj.delete()
    except:
        return


def build_context(request: HttpRequest) -> dict:
    """
    Формирование контекста страницы.
    """
    username = get_username(request)
    questions = get_questions(theme=request.GET.get("theme", "all"),
                              header=request.GET.get("textinput", ""))
    user_questions = list(QuestionModel.objects.filter(uid=username))
    # Я хочу схранять содержимое формы поиска
    form = SearchForm(request.GET)
    if not form.is_valid():
        form = SearchForm()

    return {"form": form,
            "questions": questions, 
            "username": username,
            "user_questions": user_questions,
            "is_god": is_god(username)}

