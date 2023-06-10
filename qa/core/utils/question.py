from hashlib import sha256
from django.contrib import messages
from django.http import HttpRequest

from core.models import QuestionModel
from core.forms import QuestionForm
from account.models import AccountModel


def create_record(data: dict, user_obj: AccountModel) -> int:
    """
    Создание записи вопроса.
    """
    theme = data["theme"]
    header = data["header"]
    body = data["body"]
    qid = sha256(f"{header}-{body}".encode("utf-8")).hexdigest()
    question = QuestionModel.objects.create(qid=qid, 
                                            theme=theme, 
                                            header=header, 
                                            body=body, 
                                            uid=user_obj)
    question.save()
    return 0


def build_context(request: HttpRequest) -> dict:
    """
    Формирование контекста страницы.
    """
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            try:
                create_record(form.cleaned_data, request.user)
            except:
                messages.error(request, message="Такой вопрос уже существует")

    return {"form": form}

